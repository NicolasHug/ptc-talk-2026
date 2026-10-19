---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: "Inter", "Helvetica Neue", Arial, sans-serif;
    font-size: 28px;
    padding: 50px 70px;
  }
  h1 { color: #ee4c2c; font-size: 46px; }
  h2 { color: #222; font-size: 40px; }
  h1 strong, h2 strong { color: #ee4c2c; }
  code { font-size: 0.85em; }
  code, pre, pre code { font-family: "Liberation Mono", "Courier New", monospace; }
  pre { font-size: 20px; border-radius: 8px; }
  .columns { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }
  .three { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 30px; }
  .card { background: #f6f7f9; border-radius: 12px; padding: 20px 26px; }
  .libs { display: flex; justify-content: center; gap: 30px; margin: 10px 0 30px; }
  .lib { border: 3px solid #ee4c2c; border-radius: 999px; padding: 12px 34px; font-size: 30px; font-weight: bold; text-align: center; }
  .lib small { display: block; font-size: 18px; font-weight: normal; color: #777; }
  .card h3 { margin-top: 0; color: #ee4c2c; }
  .muted { color: #777; font-size: 0.8em; }
  section.dense { font-size: 24px; }
  section.dense pre { font-size: 17px; }
  section.dense table { font-size: 19px; }
  section.dense .statement { font-size: 28px; margin: 6px 0 12px; }
  section.lead {
    color: #fff;
    text-align: center;
    justify-content: flex-start;
    padding-top: 350px;
    background:
      url(img/template/logo.png) center 16px / 534px auto no-repeat,
      url(img/template/background.png) center / cover no-repeat;
  }
  section.lead h1 { color: #fff; font-size: 44px; }
  section.divider { justify-content: center; text-align: center; }
  section.divider h1 { font-size: 64px; }
  .pipeline { display: flex; align-items: center; justify-content: center; gap: 10px; margin: 30px 0; }
  .stage { background: #f6f7f9; border: 2px solid #ddd; border-radius: 10px; padding: 14px 18px; font-size: 24px; text-align: center; }
  .stage.hl { background: #fde8e3; border-color: #ee4c2c; font-weight: bold; }
  .stage small { display: block; font-size: 16px; color: #777; font-weight: normal; }
  .arrow { color: #999; font-size: 28px; text-align: center; }
  .arrow small { display: block; font-size: 14px; color: #777; }
  section.top { place-content: start !important; }
  .short .stage { width: 170px; }
  .short.pipeline { margin: 10px 0 0; }
  .zoom-funnel { height: 40px; background: #fde8e3; clip-path: polygon(calc(50% - 85px) 0, calc(50% + 85px) 0, 100% 100%, 0 100%); }
  .zoom-box { border: 3px solid #ee4c2c; border-radius: 12px; background: #fff7f5; padding: 0 20px; margin-bottom: 16px; }
  .zoom-box .pipeline { margin: 28px 0; gap: 14px; }
  .zoom-box .stage { background: #fff; border: 3px solid #ee4c2c; padding: 18px 22px; font-size: 30px; font-weight: bold; }
  .zoom-box .stage small { font-size: 20px; font-weight: normal; color: #444; font-family: "Liberation Mono", "Courier New", monospace; margin-top: 6px; }
  .zoom-box .arrow { font-size: 40px; color: #888; }
  .zoom-box .arrow small { font-size: 18px; color: #444; font-family: "Liberation Mono", "Courier New", monospace; }
  .orange { color: #ee4c2c; }
  .statement { text-align: center; font-size: 30px; margin: 10px 0 20px; }
  .strategies { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
  .strategy { border: 2px solid #ddd; border-radius: 12px; padding: 2px 16px 10px; font-size: 22px; }
  .strategy p { margin: 6px 0; }
  .vlabel { font-size: 14px; color: #555; margin-bottom: 2px; }
  .vbar { display: flex; border: 2px solid; border-radius: 8px; overflow: hidden; }
  .vbar.c1 { border-color: #ee4c2c; background: #fde8e3; }
  .vbar.c2 { border-color: #3b6fd8; background: #e3ebfb; }
  .vbar.c3 { border-color: #2a9d5c; background: #e0f3e8; }
  .vbar.c4 { border-color: #9b4dca; background: #f1e6f8; }
  .vbar .seg { flex: 1; text-align: center; font-size: 16px; padding: 6px 0; color: #222; }
  .vbar .seg + .seg { border-left: 2px dashed; border-color: inherit; }
  .vids { display: flex; gap: 12px; }
  .vids .vbar { flex: 1; }
  .decs { display: flex; gap: 12px; margin-top: 4px; }
  .decs div { flex: 1; text-align: center; font-size: 14px; }
  .decs div::before { content: '↓'; display: block; color: #999; font-size: 20px; line-height: 1.1; }
  .decs span { display: block; border: 2px solid #555; border-radius: 6px; background: #f6f7f9; padding: 4px 0; font-family: "Liberation Mono", "Courier New", monospace; }
  p.spaced { margin: 10px 0 8px !important; }
  .pkts-label { text-align: center; font-size: 18px; color: #555; }
  .pkts { display: flex; gap: 6px; justify-content: center; margin: 4px 0 4px; }
  .lanes.arrows { margin-bottom: 4px; }
  .lanes.arrows div { text-align: center; font-size: 18px; color: #555; }
  .pkt { width: 44px; height: 34px; border-radius: 5px; font-size: 18px; font-weight: bold; text-align: center; line-height: 32px; color: #222; }
  .pkt.v { background: #fde8e3; border: 2px solid #ee4c2c; }
  .pkt.a { background: #e3ebfb; border: 2px solid #3b6fd8; }
  .lanes { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 8px; }
  .lane { border-radius: 10px; padding: 8px 14px; font-size: 19px; text-align: center; font-family: "Liberation Mono", "Courier New", monospace; }
  .lane.v { border: 2px solid #ee4c2c; background: #fff7f5; }
  .lane.a { border: 2px solid #3b6fd8; background: #f4f7fd; }
  .cuts { display: flex; align-items: center; justify-content: center; margin: 10px 0 18px; }
  .cuts .cut { width: 80px; }
  .cuts .stage { font-size: 26px; padding: 12px 18px; }
  .cuts .stage small { font-size: 17px; font-family: "Liberation Mono", "Courier New", monospace; }
  .cut { height: 90px; display: flex; justify-content: center; align-items: center; position: relative; }
  .cut::before { content: ''; position: absolute; top: 0; bottom: 0; left: 50%; border-left: 3px dashed #ee4c2c; }
  .cut span { position: relative; background: #fff; color: #ee4c2c; font-size: 30px; line-height: 1.2; }
  .branch { display: grid; grid-template-columns: auto 50px auto 70px auto; grid-template-rows: auto auto; align-items: center; justify-content: center; column-gap: 6px; row-gap: 10px; margin: 6px 0 16px; }
  .branch .stage { font-size: 26px; padding: 12px 18px; }
  .branch .stage small { font-size: 17px; }
  .branch .arrow small { font-size: 16px; font-family: "Liberation Mono", "Courier New", monospace; }
  .b-demux { grid-column: 1; grid-row: 1 / span 2; }
  .b-a1 { grid-column: 2; grid-row: 1 / span 2; }
  .b-decode { grid-column: 3; grid-row: 1 / span 2; }
  .b-a2 { grid-column: 4; grid-row: 1; font-size: 36px; }
  .b-cc { grid-column: 5; grid-row: 1; }
  .b-a3 { grid-column: 4; grid-row: 2; font-size: 36px; color: #ee4c2c; }
  .b-kernel { grid-column: 5; grid-row: 2; }
  .stage.dim { color: #aaa; background: #fafafa; border: 2px dashed #ccc; }
  .stage.dim small { color: #bbb; }
  .vchain { display: flex; flex-direction: column; align-items: center; gap: 2px; }
  .vchain .stage { width: 260px; font-size: 22px; padding: 4px 12px; }
  .vchain .stage small { display: inline; margin-left: 6px; }
  .varrow { color: #999; font-size: 20px; text-align: center; line-height: 1.15; }
  .varrow small { font-size: 16px; color: #555; }
  .cost { display: block; font-size: 14px; font-weight: bold; color: #ee4c2c; text-transform: uppercase; letter-spacing: 0.5px; }
  .cost.cheap { color: #999; }
  .big-statement { text-align: center; font-size: 38px; font-weight: bold; color: #ee4c2c; margin-top: 18px; }
  .new { background: #ee4c2c; color: #fff; border-radius: 6px; padding: 2px 10px; font-size: 18px; font-weight: bold; margin-right: 6px; }
  .knobs-line { text-align: center; font-size: 28px; margin-top: 10px; }
  .landed { display: grid; grid-template-columns: 1fr 1fr 1fr; grid-template-rows: auto 1fr; gap: 16px 20px; margin-top: 4px; align-items: start; }
  .c-codec { grid-column: 1; grid-row: 1; }
  .c-vision { grid-column: 2; grid-row: 1; }
  .c-audio { grid-column: 3; grid-row: 1 / span 2; }
  .lcard { border: 2px solid #ddd; border-radius: 14px; padding: 14px 16px 16px; }
  .lname { font-size: 32px; font-weight: bold; text-align: center; margin-bottom: 6px; }
  .row { border-radius: 10px; padding: 6px 14px; margin-top: 8px; font-size: 24px; font-weight: bold; }
  .row small { display: block; font-size: 17px; font-weight: normal; margin-top: 2px; }
  .row.active { background: #e0f3e8; border: 2px solid #2a9d5c; color: #1e5c3a; }
  .row.moved { background: #fff; border: 2px dashed #ee4c2c; color: #999; }
  .row.moved small { color: #ee4c2c; font-weight: bold; }
  .row.maint { background: #f3f3f3; border: 2px solid #ddd; color: #888; }
  a.gh { color: inherit; text-decoration: none; }
  a.plain { color: inherit; text-decoration: none; }
  .landed.big { grid-template-rows: auto; margin-top: 12px; }
  .landed.big .c-audio { grid-row: 1; }
  .landed.big .lname { font-size: 38px; margin-bottom: 8px; }
  .landed.big .row { font-size: 27px; padding: 10px 14px; margin-top: 12px; }
  .landed.big .row small { font-size: 20px; }
  .landed.mini { grid-template-rows: auto; gap: 18px; margin: 6px 0 4px; }
  .landed.mini .lcard { padding: 8px 14px 12px; }
  .landed.mini .lname { font-size: 30px; margin-bottom: 4px; }
  .landed.mini .row { font-size: 25px; padding: 8px 14px; margin-top: 6px; }
  .landed.mini .row small { font-size: 18px; }
  .why-big { font-size: 34px; margin-top: 10px; }
  .why-big li { margin: 6px 0; }
  .strategies.big { gap: 18px; }
  .strategies.big .strategy { font-size: 28px; padding: 10px 22px; }
  .landed.two { grid-template-columns: 1fr 1fr; grid-template-rows: auto; gap: 28px; margin: 8px 0 16px; }
  .landed.two .lname { font-size: 34px; margin-bottom: 6px; }
  .landed.two .row { font-size: 27px; padding: 8px 16px; margin-top: 10px; }
  .landed.two .row small { font-size: 21px; }
  .newcard { background: #fff7f5; border: 2px solid #ee4c2c; border-radius: 12px; padding: 12px 24px; margin-top: 18px; }
  .newtitle { font-size: 30px; }
  .newtitle span { font-size: 24px; color: #777; margin-left: 8px; }
  .newcard ul { columns: 3; column-gap: 24px; margin: 6px 0 0; font-size: 23px; }
  .pipeline.tight { margin: 12px 0; }
  .abi { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin: 8px 0 18px; }
  .abi-card { border-radius: 14px; padding: 12px 18px; text-align: center; font-size: 24px; font-weight: bold; display: flex; flex-direction: column; justify-content: center; gap: 4px; }
  .abi-card.before { background: #f3f3f3; border: 2px solid #ddd; color: #777; }
  .abi-card.now { background: #e0f3e8; border: 2px solid #2a9d5c; color: #1e5c3a; }
  .abi-label { font-size: 18px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
  .abi-arrow { font-size: 26px; font-weight: normal; line-height: 1.2; }
  .result { background: #fff4d6; border: 2px solid #e0a800; border-radius: 10px; padding: 12px 22px; font-size: 24px; }
  .result table { font-size: 20px; margin: 4px 0 0; }
  .result tr, .result th, .result td { background: transparent !important; border-color: #e0c060; padding: 4px 14px; }
  .result .label { font-size: 18px; color: #8a6d00; margin-bottom: 6px; }
  .todo { background: #fff4d6; border: 2px dashed #e0a800; border-radius: 10px; padding: 18px 24px; color: #8a6d00; font-size: 22px; }
  .small { font-size: 22px; }
  table { font-size: 22px; }
  .tuto { position: absolute; bottom: 24px; left: 70px; font-size: 18px; color: #777; }
  .tuto a { color: #ee4c2c; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

# From Bytes to Tensors: Efficient Media Processing with PyTorch in 2026

Nicolas Hug (META), Scott Schneider (META)

---

## Plan

<div class="libs">
<div class="lib"><a class="gh" href="https://github.com/meta-pytorch/torchcodec">TorchCodec</a><small>decode &amp; encode</small></div>
<div class="lib"><a class="gh" href="https://github.com/pytorch/vision">TorchVision</a><small>image &amp; video transforms</small></div>
<div class="lib"><a class="gh" href="https://github.com/pytorch/audio">TorchAudio</a><small>audio transforms</small></div>
</div>

<div class="columns">
<div class="card">

### Part 1: The landscape
Where these three libraries landed: who does what, and how they fit together

</div>
<div class="card">

### Part 2: Going fast
How to make your media pipeline fast with these three libraries, using existing and new features

</div>
</div>

<p class="muted" style="text-align: center">All benchmarks: <a href="https://github.com/NicolasHug/ptc-talk-2026">github.com/NicolasHug/ptc-talk-2026</a></p>

---

<!-- _class: top -->
## <a class="gh" href="https://github.com/meta-pytorch/torchcodec">TorchCodec</a>: all media decoding &amp; encoding

<div class="three">
<div class="card">

### Images
**Decode**: JPEG, PNG, WebP, GIF, AVIF, HEIC
**Encode**: JPEG, PNG
CPU and **CUDA**

</div>
<div class="card">

### Video
**Decode** and **encode**
All **FFmpeg** codecs
CPU and **CUDA**
HDR, samplers

</div>
<div class="card">

### Audio
**Decode** and **encode**
All **FFmpeg** codecs
Resampling, remixing
Fast `WavDecoder`

</div>
</div>

---

<!-- _class: top -->
## <a class="gh" href="https://github.com/meta-pytorch/torchcodec">TorchCodec</a>: all media decoding &amp; encoding

<div class="three">
<div class="card">

### Images
**Decode**: JPEG, PNG, WebP, GIF, AVIF, HEIC
**Encode**: JPEG, PNG
CPU and **CUDA**

</div>
<div class="card">

### Video
**Decode** and **encode**
All **FFmpeg** codecs
CPU and **CUDA**
HDR, samplers

</div>
<div class="card">

### Audio
**Decode** and **encode**
All **FFmpeg** codecs
Resampling, remixing
Fast `WavDecoder`

</div>
</div>


<div class="newcard">
<div class="newtitle"><strong class="orange">New in 0.17: low-level decoding APIs</strong> <span>→ more in Part 2</span></div>
<ul>
<li>multi-threaded pipelines</li>
<li>audio + video in one pass</li>
<li>raw YUV access &amp; custom kernels</li>
<li>keyframe positions</li>
<li>container-free decoding</li>
</ul>
</div>

---

## <a class="gh" href="https://github.com/pytorch/vision">TorchVision</a> and <a class="gh" href="https://github.com/pytorch/audio">TorchAudio</a>: performant transforms

<div class="landed two">
<div class="lcard">
<div class="lname"><a class="gh" href="https://github.com/pytorch/vision">TorchVision</a></div>
<div class="row active"><a class="plain" href="https://docs.pytorch.org/vision/stable/transforms.html">Transforms</a><small>resize, crop, flip, color jitter, AutoAugment, …<br><strong>images, videos, boxes, masks</strong></small></div>
<div class="row moved"><s>Decoding &amp; encoding</s><small>→ moved to TorchCodec</small></div>
<div class="row maint">Models, datasets<small>maintenance mode</small></div>
</div>
<div class="lcard">
<div class="lname"><a class="gh" href="https://github.com/pytorch/audio">TorchAudio</a></div>
<div class="row active"><a class="plain" href="https://docs.pytorch.org/audio/stable/transforms.html">Transforms</a><small>mel spectrogram, MFCC, resample, masking, …</small></div>
<div class="row moved"><s>Decoding &amp; encoding</s><small>→ moved to TorchCodec</small></div>
<div class="row maint">Models, datasets, pipelines<small>maintenance mode</small></div>
</div>
</div>

<span class="muted">Still on `torchvision.io` / `torchaudio` decoding? → <a class="gh" href="https://github.com/meta-pytorch/torchcodec">TorchCodec</a> [migration guide](https://meta-pytorch.org/torchcodec/main/generated_examples/migration/torchvision_migration.html)</span>

<!--
Before: decoding/encoding scattered and duplicated across TV and TA.
TV: io.read_video, io.VideoReader, 3 backends (PyAV, C++ FFmpeg, CUDA) - only PyAV out of the box.
TA: StreamReader/StreamWriter + audio utils on FFmpeg / libsoundfile / libsox.
Now: one job per library.
-->

<div class="tuto">📖 Blog post: <a href="https://pytorch.org/blog/evolution-of-the-pytorch-media-processing-landscape/">Evolution of the PyTorch media processing landscape</a></div>

---

## How they fit together

<a class="gh" href="https://github.com/meta-pytorch/torchcodec">TorchCodec</a>'s <strong class="orange">output</strong> is <a class="gh" href="https://github.com/pytorch/vision">TorchVision</a>'s <strong class="orange">input</strong>

<div class="pipeline tight">
<div class="stage">encoded media<small>files, bytes</small></div><div class="arrow">→</div>
<div class="stage hl"><a class="gh" href="https://github.com/meta-pytorch/torchcodec">TorchCodec</a><small>decode</small></div><div class="arrow">→</div>
<div class="stage">tensors</div><div class="arrow">→</div>
<div class="stage hl"><a class="gh" href="https://github.com/pytorch/vision">TorchVision</a><small>transform</small></div>
</div>

```python
import torch
from torchcodec.decoders import VideoDecoder
from torchvision.transforms import v2

clip = VideoDecoder("video.mp4")[10:20]   # uint8 tensor, (10, C, H, W)

transform = v2.Compose([
    v2.RandomResizedCrop(224),
    v2.ToDtype(torch.float32, scale=True),
])
batch = transform(clip)
```

**Same for audio**: `AudioDecoder` → <a class="gh" href="https://github.com/pytorch/audio">TorchAudio</a> transforms (e.g. `MelSpectrogram`)
Encoding goes the other way: `VideoEncoder`, `AudioEncoder`, …

---

## All three libraries are ABI stable!

- A release <strong class="orange">keeps working with the PyTorch versions that come after it</strong>

<div class="abi">
<div class="abi-card before"><div class="abi-label">Before</div><div>…</div><div><a class="gh" href="https://github.com/pytorch/audio">TorchAudio</a> 2.9 → PyTorch 2.9 <strong>only</strong></div><div><a class="gh" href="https://github.com/pytorch/audio">TorchAudio</a> 2.10 → PyTorch 2.10 <strong>only</strong></div></div>
<div class="abi-card now"><div class="abi-label">Now</div><div><a class="gh" href="https://github.com/pytorch/audio">TorchAudio</a> 2.11 → PyTorch 2.11, 2.12, <strong>…</strong></div></div>
</div>

- No rebuild for every PyTorch release → release cadences no longer match PyTorch's, <strong class="orange">and that's expected</strong>

<p class="muted">Earlier talk: <em>Clearing the Path Towards an ABI Stable PyTorch C++ Extension Ecosystem</em> - Sean McGovern, Chris Leonard, Jane Xu</p>

<!--
TorchAudio 2.10 release builds pinned torch==<version>; 2.11 is built on the stable libtorch API and drops the pin
(current main declares torch>=2.11).
-->

---

<!-- _class: divider -->
<!-- _paginate: false -->

# Part 2: Going fast

<div class="pipeline">
<div class="stage">open<small>read headers, index the file</small></div><div class="arrow">→</div>
<div class="stage">decode<small>encoded bytes → RGB tensors</small></div><div class="arrow">→</div>
<div class="stage">transform<small>resize, crop, normalize…</small></div>
</div>

Every stage can be the bottleneck. Let's go through them in order.

---

<!-- _class: divider -->

<div class="pipeline">
<div class="stage hl">open</div><div class="arrow">→</div>
<div class="stage">decode</div><div class="arrow">→</div>
<div class="stage">transform</div>
</div>

# Opening the video

---

## Open from anywhere

```python
decoder = VideoDecoder("video.mp4")   # path, URL, bytes, tensor of bytes
```


But also <strong class="orange">file-like objects.</strong> Don't download the whole file!


```python
import fsspec

with fsspec.open("https://.../video.mp4") as f:   # or s3://, gs://, ...
    decoder = VideoDecoder(f, seek_mode="approximate")
    frame = decoder[1000]
```

Only downloads the bytes around frame `1000`.

<!--
A direct URL also downloads only what's needed (FFmpeg's HTTP uses Range requests): frame 1000 of the 209 MB test video
= 7.5 MB with a URL, 16.1 MB with fsspec (default 5 MB blocks), 209 MB if downloading first. The server must support
Range requests (S3, GCS, CDNs, nginx... do). The point of file-like objects is generality: any storage, not just FFmpeg's protocols.
-->

<div class="tuto">📖 Tutorial: <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/decoding/file_like.html">Streaming data through file-like support</a></div>

---

<!-- _class: dense -->

## Exact vs approximate seek mode

```python
decoder = VideoDecoder("long_video.mp4", seek_mode="approximate")
```


A tradeoff: <strong class="orange">seek accuracy</strong> vs <strong class="orange">decoder creation speed</strong>

| | `"exact"` (default) | `"approximate"` |
|---|---|---|
| **Creation** | scans the whole file: slow on long videos | reads the header: fast |
| **Seeking** | frame-accurate | may be slightly off on some files |

<div class="result">
<div class="label">📊 <a href="https://github.com/NicolasHug/ptc-talk-2026/blob/main/bench/bench.py">Benchmark</a>: remote 10 min 720p video (209 MB), create decoder + decode 16 frames</div>
<div><code>"exact"</code>: <strong>236 MB</strong> downloaded</div>
<div><code>"approximate"</code>: <strong>28 MB</strong> downloaded</div>
</div>

<!--
bench.py seek_mode: bytes read from the source, 10 min 720p H.264 (209 MB).
exact: 209.1 MB to create, 236.4 MB to create + decode 16 equally spaced frames.
approximate: 0.3 MB to create, 27.5 MB to create + decode 16 frames.
Local file, page-cached: creation 40 ms (exact) vs 4.4 ms (approximate).
-->

<div class="tuto">📖 Tutorial: <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/decoding/approximate_mode.html">Exact vs approximate seek mode</a></div>

---

## Custom frame mappings: exact *and* fast

Pre-compute the index offline, reuse it every time you decode.

```bash
ffprobe -i video.mp4 -select_streams 0 -show_frames \
        -show_entries frame=pts,duration,key_frame -of json > mappings.json
```

```python
with open("mappings.json") as f:
    decoder = VideoDecoder("video.mp4", custom_frame_mappings=f)
```

**The best of both worlds:**
- Seek accuracy like `"exact"`
- Creation speed like `"approximate"`

<div class="tuto">📖 Tutorial: <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/decoding/custom_frame_mappings.html">Custom frame mappings</a></div>

---

<!-- _class: divider -->

<div class="pipeline">
<div class="stage">open</div><div class="arrow">→</div>
<div class="stage hl">decode</div><div class="arrow">→</div>
<div class="stage">transform</div>
</div>

# Decoding

---

<!-- _class: dense -->

## GPU decoding: `device="cuda"`

```python
decoder = VideoDecoder("video.mp4", device="cuda")
frames = decoder.get_frames_at([0, 10, 20])   # already on the GPU
print(decoder.cpu_fallback)                   # did we silently fall back to CPU?
```

Why it's (usually!) faster:
- **Fast raw decoding** on NVDEC, a dedicated hardware chip separate from the CUDA cores
- **Less PCIe traffic**: encoded packets are much smaller than decoded frames
- **YUV → RGB conversion**: expensive on CPU, extremely fast on GPU

<div class="result">
<div class="label">📊 <a href="https://github.com/NicolasHug/ptc-talk-2026/blob/main/bench/bench.py">Benchmark</a>: decode all 300 frames of a 10s video (laptop: RTX 4080)</div>
<div style="display: flex; gap: 40px; align-items: center">
<table>
<tr><th></th><th>CPU</th><th>GPU</th><th>Speedup</th></tr>
<tr><td><strong>1080p</strong></td><td>1466 ms</td><td>370 ms</td><td><strong>4×</strong></td></tr>
<tr><td><strong>4K</strong></td><td>4394 ms</td><td>1430 ms</td><td><strong>3×</strong></td></tr>
</table>
<div style="font-size: 26px"><strong>On a warm cache!</strong></div>
</div>
</div>

<!--
bench.py gpu_decoding, median of 10 runs, NVDEC cache warm. CPU = 1 FFmpeg thread.
GPU decoding barely uses the CPU.
The laptop GPU has 1 NVDEC; GB200 / B200 / H100 have 7, A100 has 5.
-->

<div class="tuto">📖 Tutorials: <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/decoding/basic_cuda_example.html">CUDA decoding</a> · <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/decoding/image_decoding.html">Image decoding</a></div>

---

## GPU decoding: the NVDEC decoder cache

Creating and destructing a `VideoDecoder(..., device="cuda")` is very expensive!
<a class="gh" href="https://github.com/meta-pytorch/torchcodec">TorchCodec</a> **caches and reuses** the underlying hardware resources.

```python
from torchcodec.decoders import set_nvdec_cache_capacity

set_nvdec_cache_capacity(64)   # default: 20 decoders per GPU
```

- A cached decoder is reused for a new video with the same codec and frame dimensions (LRU eviction)
- **tune the capacity!**

<div class="result">
<div class="label">📊 <a href="https://github.com/NicolasHug/ptc-talk-2026/blob/main/bench/bench.py">Benchmark</a>: create GPU decoder + decode 10 frames, 10s 1080p video (laptop: RTX 4080)</div>
<div style="display: flex; gap: 40px; align-items: center">
<table>
<tr><th>No cache</th><th>Warm cache</th><th>Speedup</th></tr>
<tr><td>272 ms</td><td>24 ms</td><td><strong>11×</strong></td></tr>
</table>
<div style="font-size: 24px"><strong>Matters even more when decoding many videos in parallel</strong></div>
</div>
</div>

<!--
bench.py nvdec_cache, median of 20 runs. "No cache" = set_nvdec_cache_capacity(0).
-->

---

<!-- _class: dense -->

## Parallel decoding: 4 strategies

<div class="strategies">
<div class="strategy">

**① One long video**: one decoder per chunk

<div class="vlabel">video 1</div>
<div class="vbar c1"><div class="seg">chunk 1</div><div class="seg">chunk 2</div><div class="seg">chunk 3</div><div class="seg">chunk 4</div></div>
<div class="decs"><div><span>VideoDecoder</span></div><div><span>VideoDecoder</span></div><div><span>VideoDecoder</span></div><div><span>VideoDecoder</span></div></div>

</div>
<div class="strategy">

**② Many videos**: one decoder per video

<div class="vlabel">&nbsp;</div>
<div class="vids"><div class="vbar c1"><div class="seg">video 1</div></div><div class="vbar c2"><div class="seg">video 2</div></div><div class="vbar c3"><div class="seg">video 3</div></div><div class="vbar c4"><div class="seg">video 4</div></div></div>
<div class="decs"><div><span>VideoDecoder</span></div><div><span>VideoDecoder</span></div><div><span>VideoDecoder</span></div><div><span>VideoDecoder</span></div></div>

</div>
<div class="strategy">

**③ FFmpeg threads**: decode upcoming frames ahead, into a buffer

`VideoDecoder(path, num_ffmpeg_threads=4)`

</div>
<div class="strategy">

**④ Low-level APIs**: parallelize stage by stage. Next slides!

</div>
</div>

<p class="spaced"><strong class="orange">All strategies compose!</strong> ① and ② run on threads or processes: decoding releases the GIL.</p>

<div class="result">
<div class="label">📊 <a href="https://github.com/NicolasHug/ptc-talk-2026/blob/main/bench/bench.py">Benchmark</a>: decode all 18000 frames of a 10min 720p video (laptop CPU, 4 workers)</div>
<table>
<tr><th>Sequential</th><th>① 4 threads</th><th>① 4 processes</th><th>③ 4 FFmpeg threads</th></tr>
<tr><td>32.7 s</td><td>8.7 s (<strong>3.7×</strong>)</td><td>9.3 s (<strong>3.5×</strong>)</td><td>15.3 s (<strong>2.1×</strong>)</td></tr>
</table>
</div>

<!--
bench.py parallel_decoding, median of 3 runs, pinned to 4 performance cores (taskset -c 0,2,4,6).
① = 4 chunks, one single-threaded decoder per chunk. Chunking scales ~linearly on uniform cores (2 workers: 1.98x, 4: 3.91x).
FFmpeg threads plateau: ~19% of the work stays serial (consistent with single-threaded color conversion).
-->

<div class="tuto">📖 Tutorial: <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/decoding/parallel_decoding.html">Parallel video decoding</a></div>

---

<!-- _class: top -->

## Low-level decoding APIs: new in TorchCodec 0.17

<div class="short pipeline">
<div class="stage">open</div><div class="arrow">→</div>
<div class="stage hl">decode</div><div class="arrow">→</div>
<div class="stage">transform</div>
</div>

<div class="tuto">📖 Tutorial: <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/low_level/basics.html">Build your own decoding pipeline</a></div>

---

<!-- _class: top -->

## Low-level decoding APIs: new in TorchCodec 0.17

<div class="short pipeline">
<div class="stage">open</div><div class="arrow">→</div>
<div class="stage hl">decode</div><div class="arrow">→</div>
<div class="stage">transform</div>
</div>
<div class="zoom-funnel"></div>
<div class="zoom-box">
<div class="pipeline">
<div class="stage">demux<small>Demuxer</small></div><div class="arrow">→<small>Packet</small></div>
<div class="stage">decode<small>VideoPacketDecoder</small></div><div class="arrow">→<small>RawFrame (YUV)</small></div>
<div class="stage">color convert<small>ColorConverter</small></div><div class="arrow">→<small>Frame (RGB)</small></div>
</div>
</div>

<div class="knobs-line"><code>VideoDecoder</code>: everything in one call. Low-level APIs: <strong class="orange">more knobs to hill-climb on</strong>.</div>
<div class="tuto">📖 Tutorial: <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/low_level/basics.html">Build your own decoding pipeline</a></div>

---

## Low-level APIs: the basic loop

<div class="zoom-box">
<div class="pipeline">
<div class="stage">demux<small>Demuxer</small></div><div class="arrow">→<small>Packet</small></div>
<div class="stage">decode<small>VideoPacketDecoder</small></div><div class="arrow">→<small>RawFrame (YUV)</small></div>
<div class="stage">color convert<small>ColorConverter</small></div><div class="arrow">→<small>Frame (RGB)</small></div>
</div>
</div>

```python
from torchcodec.decoders import ColorConverter, Demuxer

demuxer = Demuxer("video.mp4", streams="video")
packet_decoder = demuxer.streams[0].make_decoder()
color_converter = ColorConverter()

for packet in demuxer:
    for raw_frame in packet_decoder.decode(packet):
        frame = color_converter.convert(raw_frame)

# Same as VideoDecoder("video.mp4").get_all_frames()
```

<div class="tuto">📖 Tutorial: <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/low_level/basics.html">Build your own decoding pipeline</a></div>

---


## What the low-level APIs enable

<div class="strategies big">
<div class="strategy">

**① Multi-threaded pipelines**: run the stages concurrently

</div>
<div class="strategy">

**② Multi-stream decoding**: audio + video in a single pass

</div>
<div class="strategy">

**③ Raw YUV frames**: custom color conversion, fused kernels, 10-bit HDR

</div>
<div class="strategy">

**④ Keyframe positions**: cheap frames, great for sampling

</div>
</div>

<p class="spaced" style="text-align: center">Also: endless sources (live streams, pipes)</p>

<div class="big-statement">Let's go over them!</div>

---

## Low-level APIs: multi-threaded pipelines

Each stage **releases the GIL** → cut the pipeline into threads at any stage boundary:

<div class="cuts">
<div class="stage">demux<small>Demuxer</small></div>
<div class="cut"><span>✂</span></div>
<div class="stage">decode<small>VideoPacketDecoder</small></div>
<div class="cut"><span>✂</span></div>
<div class="stage">color convert<small>ColorConverter</small></div>
</div>

```python
# prefetch(): run the upstream stages on a background thread, through a bounded queue
raw_frames = prefetch(decode(packet_decoder, demux(demuxer)))   # producer
frames = color_convert(color_converter, raw_frames)             # consumer
```

<div class="result">
<div class="label">📊 <a href="https://github.com/NicolasHug/ptc-talk-2026/blob/main/bench/bench.py">Benchmark</a>: decode all 300 frames of a 10s 1080p video (laptop CPU)</div>
<table>
<tr><th>VideoDecoder</th><th>Low-level, sequential</th><th>Low-level, producer / consumer</th></tr>
<tr><td>1457 ms</td><td>1458 ms</td><td>940 ms (<strong>1.5×</strong>)</td></tr>
</table>
</div>

<!--
bench.py low_level_pipeline, median of 10 runs, pinned to 2 performance cores (taskset -c 0,2).
Producer = demux + decode, consumer = color conversion.
-->

<div class="tuto">📖 Tutorial: <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/low_level/pipelines.html">Multi-threaded decoding pipelines</a></div>

---

<!-- _class: dense -->

## Low-level APIs: audio + video in one pass

<div class="pkts-label">Demuxer: interleaved packets from one file</div>
<div class="pkts"><div class="pkt v">V</div><div class="pkt a">A</div><div class="pkt v">V</div><div class="pkt v">V</div><div class="pkt a">A</div><div class="pkt v">V</div><div class="pkt a">A</div><div class="pkt v">V</div><div class="pkt v">V</div><div class="pkt a">A</div><div class="pkt v">V</div><div class="pkt a">A</div></div>
<div class="lanes arrows"><div>↓ video packets</div><div>↓ audio packets</div></div>
<div class="lanes">
<div class="lane v">VideoPacketDecoder → ColorConverter → frames</div>
<div class="lane a">AudioPacketDecoder → AudioConverter → samples</div>
</div>

```python
demuxer = Demuxer("video.mp4", streams=("video", "audio"))
video_stream, audio_stream = demuxer.streams
decoders = {s.index: s.make_decoder() for s in demuxer.streams}
color_converter, audio_converter = ColorConverter(), AudioConverter()

for packet in demuxer:
    for raw in decoders[packet.stream_index].decode(packet):
        if packet.stream_index == video_stream.index:
            frame = color_converter.convert(raw)
        else:
            samples = audio_converter.convert(raw)
```

- **Read the file once**, instead of once per stream
- Also works for several video streams or audio tracks: `streams="all"`

<div class="tuto">📖 Tutorial: <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/low_level/basics.html">Build your own decoding pipeline</a></div>

---

## Low-level APIs: raw YUV frames

<div class="branch">
<div class="stage b-demux">demux</div>
<div class="arrow b-a1">→</div>
<div class="stage b-decode">decode<small>→ RawFrame (YUV)</small></div>
<div class="arrow b-a2">↗</div>
<div class="stage b-cc dim">ColorConverter<small>default</small></div>
<div class="arrow b-a3">↘</div>
<div class="stage hl b-kernel">your own kernel<small>YUV → RGB + resize, fused</small></div>
</div>

```python
for raw_frame in packet_decoder.decode(packet):
    Y, U, V = raw_frame.planes        # the decoder's own planes: no conversion, no copy
    out = my_yuv_to_rgb_and_resize(Y, U, V, size=(224, 224))   # e.g. a Triton kernel
```

- **Fuse** color conversion with your transforms (e.g. resize) in one kernel, or train directly in YUV
- Or just train on YUV!
- 10-bit HDR → `uint16` planes, every bit intact

<div class="tuto">📖 Tutorial: <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/low_level/raw_data.html">Raw frames and raw audio samples</a></div>

---


## Low-level APIs: keyframe positions

```python
demuxer = Demuxer("video.mp4")
index = demuxer.streams[0].scan()   # one pass over the packets, no decoding

index.key_frame_indices             # exact keyframe positions
index.pts_seconds[index.key_frame_indices]
```

- Keyframes are the **cheapest frames to decode**
- Great for **samplers** and thumbnails: sample at or near keyframes for fast training data

<div class="tuto">📖 Tutorial: <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/low_level/basics.html">Build your own decoding pipeline</a></div>

---

<!-- _class: divider -->

<div class="pipeline">
<div class="stage">open</div><div class="arrow">→</div>
<div class="stage">decode</div><div class="arrow">→</div>
<div class="stage hl">transform</div>
</div>

# Transforming

(mostly images, but this applies to videos too!)

---

<!-- _class: dense -->

## The bare minimum for an image pipeline

<div class="columns" style="grid-template-columns: 2fr 3fr; align-items: center">
<div class="vchain">
<div class="stage hl">decode_image<small><a class="gh" href="https://github.com/meta-pytorch/torchcodec">TorchCodec</a></small><span class="cost">expensive</span></div>
<div class="varrow">↓ <small>uint8 tensor, channels-last</small></div>
<div class="stage hl">resize<small><a class="gh" href="https://github.com/pytorch/vision">TorchVision</a> v2</small><span class="cost">expensive</span></div>
<div class="varrow">↓</div>
<div class="stage">ToDtype<small>float32</small><span class="cost cheap">cheap</span></div>
<div class="varrow">↓</div>
<div class="stage">Normalize<span class="cost cheap">cheap</span></div>
</div>
<div>

What fast resizing needs:
- **SIMD kernels** (AVX2, NEON), which need:
  - `uint8` input
  - <code>torchvision.transforms.<strong>v2</strong></code>
  - **tensors**, not PIL images → <a class="gh" href="https://github.com/meta-pytorch/torchcodec">TorchCodec</a> image decoders
- **Channels-last** memory

</div>
</div>

<div class="big-statement"><a class="gh" href="https://github.com/meta-pytorch/torchcodec">TorchCodec</a> + <a class="gh" href="https://github.com/pytorch/vision">TorchVision</a> give you all this by default!</div>

<div class="tuto">📖 Docs: <a href="https://docs.pytorch.org/vision/stable/transforms.html#performance-considerations">TorchVision transforms performance considerations</a></div>

---

<!-- _class: dense -->

## <a class="gh" href="https://github.com/meta-pytorch/torchcodec">TorchCodec</a> + <a class="gh" href="https://github.com/pytorch/vision">TorchVision</a>: fast by default

```python
from torchcodec.decoders import decode_image
from torchvision.transforms import v2

img = decode_image("image.jpg")             # uint8 CHW, channels-last memory

transforms = v2.Compose([                   # use v2!
    v2.Resize(size=(224, 224)),             # on uint8: SIMD fast path!
    v2.ToDtype(torch.float32, scale=True),  # convert to float *after* resizing
    v2.Normalize(mean=..., std=...),
])
out = transforms(img)
```

<div class="result">
<div class="label">📊 <a href="https://github.com/NicolasHug/ptc-talk-2026/blob/main/bench/bench.py">Benchmark</a>: decode + resize + normalize a 1080p JPEG (laptop CPU, 1 thread)</div>
<table>
<tr><th>PIL pipeline</th><th>PIL-SIMD pipeline</th><th><a class="gh" href="https://github.com/meta-pytorch/torchcodec">TorchCodec</a> + <a class="gh" href="https://github.com/pytorch/vision">TorchVision</a> (above)</th></tr>
<tr><td>10.0 ms</td><td>4.4 ms</td><td><strong>4.0 ms</strong></td></tr>
</table>
</div>


<!--
bench.py image_pipeline, median of 100 runs, torch.set_num_threads(1), pinned to one core.
PIL pipeline: Image.open + load(), v2.Resize on the PIL image, ToImage + ToDtype, Normalize.
Pillow-SIMD 12.1.1.post0 built from source with CC="gcc -mavx2" CFLAGS="-O3".
JPEG decoding itself is the same speed (PIL 3.3 ms vs TorchCodec 2.9 ms) and gives bitwise-identical pixels.
Resize to 224: PIL 5.5 ms, Pillow-SIMD 0.59 ms, TorchVision uint8 0.66 ms.
The common Image.open(...).convert("RGB") idiom (e.g. ImageFolder) adds a full copy: ~5 ms more for PIL pipelines.
-->

- PIL-SIMD: x86 only (no NEON SIMD), and still pays the `PIL → tensor` copy.
- `decode_image`: JPEG (CPU **and CUDA!**), PNG, WebP, GIF, AVIF, HEIC

---

## Results are the same as PIL's!

- Use `antialias=True` (the default)
- vs PIL: mean absolute error <strong class="orange">≈ 0.01</strong> at most (out of 255), max difference <strong class="orange">1-2</strong>
- <strong class="orange">Bitwise identical</strong> to PIL-SIMD
- What matters for models: **consistent** interpolation mode and antialias between training and inference

<span class="new">NEW</span> in `TorchVision 0.27`: **Lanczos interpolation!** Alongside bilinear and bicubic

<!--
vs Pillow 12.2, uint8, antialias=True:
6 natural images (TorchVision gallery + COCO sample) downscaled to 224x224: MAE 0.0012 (bilinear), 0.0022 (bicubic), 0.0039 (Lanczos); max diff 1.
Grace Hopper 517x606: downscaling max diff 1; upscaling to 1024x1024 / 1200x800: bilinear max 1, bicubic and Lanczos max 2; MAE <= 0.0051 everywhere.
Random-noise images (worst case), 256x276 -> 120x128 / 500x480: max diff 1-2, <= 1% of pixels differ, MAE <= 0.0102 (Lanczos upscaling).
vs Pillow-SIMD 12.1.1: bitwise identical for all three modes.
antialias defaults to True since TorchVision 0.17. Lanczos: TorchVision 0.27 (April 2026).
-->

---

## Audio: `WavDecoder`

```python
from torchcodec.decoders import WavDecoder

samples = WavDecoder("audio.wav").get_all_samples()
```

- Reads WAV data directly, **bypassing FFmpeg** entirely

<div class="result">
<div class="label">📊 <a href="https://github.com/NicolasHug/ptc-talk-2026/blob/main/bench/bench.py">Benchmark</a>: create decoder + decode a WAV file (laptop CPU)</div>
<table>
<tr><th></th><th>AudioDecoder</th><th>WavDecoder</th><th>Speedup</th></tr>
<tr><td><strong>5s clip</strong>, 16kHz mono</td><td>2.7 ms</td><td>0.05 ms</td><td><strong>50×</strong></td></tr>
<tr><td><strong>10min</strong>, 48kHz stereo</td><td>202 ms</td><td>81 ms</td><td><strong>2.5×</strong></td></tr>
<tr><td><strong>1s from a 10min file</strong></td><td>16.7 ms</td><td>0.06 ms</td><td><strong>280×</strong></td></tr>
</table>
</div>

<!--
bench.py wav_decoding, median of 50 runs, pinned to one core. 16-bit PCM WAV files.
Last row: get_samples_played_in_range(300, 301) on the 10min 48kHz stereo file.
-->

<div class="tuto">📖 Tutorial: <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/decoding/performance_tips.html">Performance tips</a></div>

---

## And on the way out: encoding

```python
from torchcodec.encoders import Encoder

encoder = Encoder()
video = encoder.add_video(height=1080, width=1920, frame_rate=30, device="cuda")
audio = encoder.add_audio(sample_rate=44100, num_channels=2)

with encoder.open_file("output.mp4"):
    video.add_frames(frames)
    audio.add_samples(samples)
```

- Multiple video and audio streams in one container
- Mix CPU and CUDA video streams, feed data incrementally
- Simpler one-shot encoders too: `VideoEncoder`, `AudioEncoder`, `JpegEncoder`, `PngEncoder`

<div class="tuto">📖 Tutorials: <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/encoding/multi_stream_encoding.html">Multi-stream encoding</a> · <a href="https://meta-pytorch.org/torchcodec/main/generated_examples/encoding/video_encoding.html">Video encoding</a></div>

---

## <a class="gh" href="https://github.com/meta-pytorch/torchcodec">TorchCodec</a> 1.0 is coming!

<div class="big-statement">Tell us what you need</div>

<p style="text-align: center">Feedback and feature requests: <a href="https://github.com/meta-pytorch/torchcodec/issues">TorchCodec</a> · <a href="https://github.com/pytorch/vision/issues">TorchVision</a> · <a href="https://github.com/pytorch/audio/issues">TorchAudio</a></p>

<div class="columns">
<div class="card">

### Docs and tutorials
- [TorchCodec docs](https://meta-pytorch.org/torchcodec/) · [tutorials](https://meta-pytorch.org/torchcodec/main/generated_examples/index.html)
- [TorchVision transforms](https://docs.pytorch.org/vision/stable/transforms.html)
- [TorchAudio docs](https://docs.pytorch.org/audio/stable/)

</div>
<div class="card">

### From this talk
- [Benchmarks](https://github.com/NicolasHug/ptc-talk-2026)
- [Blog post: the media processing landscape](https://pytorch.org/blog/evolution-of-the-pytorch-media-processing-landscape/)
- [TorchCodec performance tips](https://meta-pytorch.org/torchcodec/main/generated_examples/decoding/performance_tips.html)

</div>
</div>

<!-- First slides must be high energy
don't apologize
Celebrate
ABI stability should be own slide (ref Jane's talk)


CUDA 4k why slower??
dont rush or skip slides


lost on decoder cache
lost on SIMD kernel "complex but we do it all for you"

max pixel value not clear

call to action on last slide -->