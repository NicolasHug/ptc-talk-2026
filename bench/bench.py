"""Benchmarks from the "From Bytes to Tensors" talk, PyTorch Conference 2026.

    python bench.py              # run all benchmarks
    python bench.py seek_mode    # run some of them

Test videos are generated on first use in ./videos, with an ffmpeg that
supports libx264.
"""

import io
import queue
import subprocess
import sys
import threading
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from pathlib import Path
from time import perf_counter_ns

import torch
from torchcodec.decoders import (
    AudioDecoder,
    ColorConverter,
    Demuxer,
    VideoDecoder,
    WavDecoder,
    get_nvdec_cache_capacity,
    set_nvdec_cache_capacity,
)
from torchcodec.samplers import clips_at_regular_indices

VIDEO_DIR = Path("videos")


def bench(f, *args, num_exp=100, warmup=0, **kwargs):

    for _ in range(warmup):
        f(*args, **kwargs)

    times = []
    for _ in range(num_exp):
        start = perf_counter_ns()
        f(*args, **kwargs)
        if torch.cuda.is_available():
            torch.cuda.synchronize()
        end = perf_counter_ns()
        times.append(end - start)
    return torch.tensor(times).float()


def report_stats(times, unit="ms"):
    mul = {
        "ns": 1,
        "µs": 1e-3,
        "ms": 1e-6,
        "s": 1e-9,
    }[unit]
    times = times * mul
    std = times.std().item()
    med = times.median().item()
    print(f"{med = :.2f}{unit} +- {std:.2f}")
    return med


def make_video(duration_seconds, resolution):
    path = VIDEO_DIR / f"{duration_seconds}s_{resolution}.mp4"
    if not path.exists():
        print(f"Generating {path} ...")
        VIDEO_DIR.mkdir(exist_ok=True)
        subprocess.run(
            [
                "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
                "-f", "lavfi", "-i", f"testsrc2=size={resolution}:rate=30:duration={duration_seconds}",
                "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p",
                str(path),
            ],
            check=True,
        )
    return path


class CountingFile(io.RawIOBase):
    """File-like object that counts the bytes read: what a remote file would download."""

    def __init__(self, path):
        self.f = open(path, "rb")
        self.bytes_read = 0

    def read(self, size=-1):
        data = self.f.read(size)
        self.bytes_read += len(data)
        return data

    def seek(self, offset, whence=io.SEEK_SET):
        return self.f.seek(offset, whence)

    def tell(self):
        return self.f.tell()


def make_image(resolution):
    path = VIDEO_DIR / f"image_{resolution}.jpg"
    if not path.exists():
        VIDEO_DIR.mkdir(exist_ok=True)
        subprocess.run(
            [
                "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
                "-f", "lavfi", "-i", f"testsrc2=size={resolution}:duration=1",
                "-frames:v", "1", "-q:v", "2", str(path),
            ],
            check=True,
        )
    return path


def make_wav(duration_seconds, sample_rate, num_channels):
    path = VIDEO_DIR / f"{duration_seconds}s_{sample_rate}hz_{num_channels}ch.wav"
    if not path.exists():
        VIDEO_DIR.mkdir(exist_ok=True)
        subprocess.run(
            [
                "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
                "-f", "lavfi", "-i", f"sine=frequency=440:sample_rate={sample_rate}:duration={duration_seconds}",
                "-ac", str(num_channels), "-c:a", "pcm_s16le", str(path),
            ],
            check=True,
        )
    return path


def seek_mode():
    video = make_video(duration_seconds=600, resolution="1280x720")
    print(f"Bytes read from a 10min 720p video ({video.stat().st_size / 1e6:.0f} MB)")
    for mode in ("exact", "approximate"):
        source = CountingFile(video)
        decoder = VideoDecoder(source, seek_mode=mode)
        created = source.bytes_read / 1e6
        clips_at_regular_indices(decoder, num_clips=16)
        total = source.bytes_read / 1e6
        print(f"  {mode:<12} create: {created:6.1f} MB   create + decode 16 frames: {total:6.1f} MB")


def gpu_decoding():
    configs = {"cpu": dict(device="cpu"), "gpu": dict(device="cuda")}
    for resolution, name in (("1920x1080", "1080p"), ("3840x2160", "4K")):
        video = make_video(duration_seconds=10, resolution=resolution)
        print(f"Decode all 300 frames of a 10s {name} video")
        for label, kwargs in configs.items():

            def f():
                for _ in VideoDecoder(video, seek_mode="approximate", **kwargs):
                    pass

            print(f"  {label:<5}", end="")
            # warmup=1 also fills the NVDEC decoder cache, so the timed runs reuse it.
            report_stats(bench(f, num_exp=10, warmup=1))


def nvdec_cache():
    video = make_video(duration_seconds=10, resolution="1920x1080")
    print("Create GPU decoder + decode 10 frames, 10s 1080p video")

    def f():
        VideoDecoder(video, device="cuda", seek_mode="approximate").get_frames_in_range(0, 10)

    default_capacity = get_nvdec_cache_capacity()
    for label, capacity in (("no cache", 0), ("warm cache", default_capacity)):
        set_nvdec_cache_capacity(capacity)
        print(f"  {label:<11}", end="")
        report_stats(bench(f, num_exp=20, warmup=1))


def decode_range(video, start, stop, num_ffmpeg_threads=1):
    decoder = VideoDecoder(video, seek_mode="approximate", num_ffmpeg_threads=num_ffmpeg_threads)
    for i in range(start, stop):
        decoder[i]


def parallel_decoding():
    video = make_video(duration_seconds=600, resolution="1280x720")
    num_frames = VideoDecoder(video).metadata.num_frames
    n = 4
    starts = [i * num_frames // n for i in range(n)]
    stops = [(i + 1) * num_frames // n for i in range(n)]

    def chunks(executor_class):
        with executor_class(n) as executor:
            list(executor.map(decode_range, [video] * n, starts, stops))

    strategies = {
        "sequential": lambda: decode_range(video, 0, num_frames),
        f"{n} FFmpeg threads": lambda: decode_range(video, 0, num_frames, num_ffmpeg_threads=n),
        f"{n} threads": lambda: chunks(ThreadPoolExecutor),
        f"{n} processes": lambda: chunks(ProcessPoolExecutor),
    }
    print(f"Decode all {num_frames} frames of a 10min 720p video")
    for label, f in strategies.items():
        print(f"  {label:<18}", end="")
        report_stats(bench(f, num_exp=3), unit="s")


def demux(demuxer):
    yield from demuxer


def decode(packet_decoder, packets):
    for packet in packets:
        yield from packet_decoder.decode(packet)
    yield from packet_decoder.drain()


def color_convert(color_converter, raw_frames):
    for raw_frame in raw_frames:
        yield color_converter.convert(raw_frame)


def prefetch(upstream, buffer_size=8):
    """Run the upstream generator on a background thread, through a bounded queue."""
    q = queue.Queue(maxsize=buffer_size)
    done = object()

    def producer():
        for item in upstream:
            q.put(item)
        q.put(done)

    threading.Thread(target=producer, daemon=True).start()
    while (item := q.get()) is not done:
        yield item


def low_level_pipeline():
    video = make_video(duration_seconds=10, resolution="1920x1080")

    def stages():
        demuxer = Demuxer(video)
        return demuxer, demuxer.streams[0].make_decoder(), ColorConverter()

    def video_decoder():
        for _ in VideoDecoder(video, seek_mode="approximate"):
            pass

    def sequential():
        demuxer, packet_decoder, color_converter = stages()
        for _ in color_convert(color_converter, decode(packet_decoder, demux(demuxer))):
            pass

    def producer_consumer():
        demuxer, packet_decoder, color_converter = stages()
        raw_frames = prefetch(decode(packet_decoder, demux(demuxer)))
        for _ in color_convert(color_converter, raw_frames):
            pass

    print("Decode all 300 frames of a 10s 1080p video, CPU")
    for label, f in (
        ("VideoDecoder", video_decoder),
        ("low-level, sequential", sequential),
        ("low-level, producer/consumer", producer_consumer),
    ):
        print(f"  {label:<29}", end="")
        report_stats(bench(f, num_exp=10, warmup=1))


def image_pipeline():
    # For the Pillow-SIMD numbers, install it in place of Pillow, built with optimizations on:
    #   CC="cc -mavx2" CFLAGS="-O3" pip install --no-binary pillow-simd pillow-simd
    # Setting CC/CFLAGS drops Python's default -O2/-O3, so -O3 must be passed explicitly.
    import PIL
    from PIL import Image
    from torchcodec.decoders import decode_image
    from torchvision.transforms import v2

    torch.set_num_threads(1)
    data = make_image("1920x1080").read_bytes()
    normalize = v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    resize = v2.Resize(size=(224, 224), antialias=True)
    pil_transforms = v2.Compose([resize, v2.ToImage(), v2.ToDtype(torch.float32, scale=True), normalize])
    tensor_transforms = v2.Compose([resize, v2.ToDtype(torch.float32, scale=True), normalize])

    def pil_pipeline():
        image = Image.open(io.BytesIO(data))
        image.load()  # Decodes. Avoid .convert("RGB") here: it's a full extra copy.
        pil_transforms(image)

    def torchcodec_torchvision_pipeline():
        tensor_transforms(decode_image(data))

    print("Decode + resize + normalize a 1080p JPEG, 1 thread")
    for label, f in (
        (f"PIL {PIL.__version__}", pil_pipeline),
        ("TorchCodec + TorchVision", torchcodec_torchvision_pipeline),
    ):
        print(f"  {label:<26}", end="")
        report_stats(bench(f, num_exp=100, warmup=5))


def wav_decoding():
    short = make_wav(duration_seconds=5, sample_rate=16000, num_channels=1)
    long = make_wav(duration_seconds=600, sample_rate=48000, num_channels=2)
    cases = {
        "5s 16kHz mono, all samples": lambda decoder_class: decoder_class(short).get_all_samples(),
        "10min 48kHz stereo, all samples": lambda decoder_class: decoder_class(long).get_all_samples(),
        "10min 48kHz stereo, 1s at 5min": lambda decoder_class: decoder_class(long).get_samples_played_in_range(300, 301),
    }
    print("Decode WAV files (create decoder + decode)")
    for case, f in cases.items():
        print(f"  {case}")
        for decoder_class in (AudioDecoder, WavDecoder):
            print(f"    {decoder_class.__name__:<13}", end="")
            report_stats(bench(f, decoder_class, num_exp=50, warmup=2))


BENCHMARKS = [seek_mode, gpu_decoding, nvdec_cache, parallel_decoding, low_level_pipeline, image_pipeline, wav_decoding]

if __name__ == "__main__":
    names = sys.argv[1:] or [b.__name__ for b in BENCHMARKS]
    for b in BENCHMARKS:
        if b.__name__ in names:
            b()
