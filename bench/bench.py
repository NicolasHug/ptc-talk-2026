"""Benchmarks from the "From Bytes to Tensors" talk, PyTorch Conference 2026.

    python bench.py              # run all benchmarks
    python bench.py seek_mode    # run some of them

Test videos are generated on first use in ./videos, with an ffmpeg that
supports libx264.
"""

import io
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from pathlib import Path
from time import perf_counter_ns

import torch
from torchcodec.decoders import VideoDecoder, get_nvdec_cache_capacity, set_nvdec_cache_capacity
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


BENCHMARKS = [seek_mode, gpu_decoding, nvdec_cache, parallel_decoding]

if __name__ == "__main__":
    names = sys.argv[1:] or [b.__name__ for b in BENCHMARKS]
    for b in BENCHMARKS:
        if b.__name__ in names:
            b()
