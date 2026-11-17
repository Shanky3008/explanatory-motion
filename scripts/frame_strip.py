#!/usr/bin/env python3
"""Frame strip from a clip: N frames evenly spaced between two times, tiled into one picture, using ffmpeg only.

usage:
  python frame_strip.py CLIP --out strip.png [--t0 0] [--t1 END] [--n 16] [--cols 4] [--width 360]

t0 and t1 are seconds INTO THE CLIP (not story or timeline time). The script prints the time of every cell, left to
right, top to bottom, and writes the same list next to the picture as strip.png.txt. Needs ffmpeg and ffprobe on PATH.
Use a short window (2-6 s) for motion, and a denser window (0.2 s apart) around an event such as a tag appearing.
"""
import argparse, os, shutil, subprocess, sys, tempfile


def need(tool):
    if not shutil.which(tool):
        sys.exit(f"{tool} not found on PATH")


def duration(clip):
    v = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=codec_type",
                        "-of", "csv=p=0", clip], capture_output=True, text=True)
    if v.returncode == 0 and "video" not in v.stdout:
        sys.exit("the file has no video stream (audio only?): " + clip)
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", clip],
                       capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        sys.exit("could not read the clip duration: " + r.stderr.strip())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("clip")
    ap.add_argument("--out", required=True)
    ap.add_argument("--t0", type=float, default=0.0)
    ap.add_argument("--t1", type=float, default=None)
    ap.add_argument("--n", type=int, default=16)
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--width", type=int, default=360)
    a = ap.parse_args()
    need("ffmpeg"); need("ffprobe")
    if a.n < 1 or a.cols < 1 or a.width < 16:
        sys.exit("--n and --cols must be at least 1 and --width at least 16")
    dur = duration(a.clip)
    t1 = dur if a.t1 is None else a.t1
    if not (0 <= a.t0 < t1 <= dur + 1e-6):
        sys.exit(f"window {a.t0}..{t1} is outside the clip (0..{dur:.2f})")
    n = max(1, a.n)
    step = (t1 - a.t0) / n
    # take the middle of each of n equal slices, so the last cell is not past the end of the clip
    times = [a.t0 + step * (i + 0.5) for i in range(n)]
    cols = max(1, min(a.cols, n))
    rows = (n + cols - 1) // cols
    tmp = tempfile.mkdtemp(prefix="strip_")
    try:
        for i, t in enumerate(times):
            r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", a.clip, "-frames:v", "1",
                                "-vf", f"scale={a.width}:-2", os.path.join(tmp, f"f_{i:03d}.png")],
                               capture_output=True, text=True)
            if r.returncode != 0:
                sys.exit("ffmpeg failed: " + r.stderr.strip())
        r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", "1", "-i", os.path.join(tmp, "f_%03d.png"),
                            "-vf", f"tile={cols}x{rows}:padding=4:color=gray", "-frames:v", "1", a.out],
                           capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit("ffmpeg tile failed: " + r.stderr.strip())
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    lines = [f"cell {i + 1}: {t:.3f} s" for i, t in enumerate(times)]
    with open(a.out + ".txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(a.out)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
