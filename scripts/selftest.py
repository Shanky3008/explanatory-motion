#!/usr/bin/env python3
"""Run every script on tiny synthetic inputs and check the results.  usage: python scripts/selftest.py
Needs: python 3.8+, node 18+ (easing test), Pillow (contact sheet), ffmpeg + ffprobe (frame strip).
Creates its files in a temporary folder and removes it. Exit code 0 only if every check passes."""
import json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
results = []


def check(name, ok, detail=""):
    results.append(ok)
    print(("PASS " if ok else "FAIL ") + name + (("  " + detail) if detail and not ok else ""))


def run(args, **kw):
    return subprocess.run(args, capture_output=True, text=True, **kw)


# 1. easing helper
if shutil.which("node"):
    r = run(["node", os.path.join(HERE, "easing.test.mjs")])
    check("easing.mjs self-test", r.returncode == 0 and "all checks passed" in r.stdout, r.stdout + r.stderr)
else:
    print("SKIP easing.mjs self-test (node not found)")

# 2. timing linter
fx = os.path.join(HERE, "selftest")
good = run([PY, "-I", os.path.join(HERE, "timing_lint.py"), os.path.join(fx, "cues_good.json"), os.path.join(fx, "words.json"), "--audience", "adult"])
check("timing_lint: clean cues pass (exit 0, no warnings)", good.returncode == 0 and "0 error(s), 0 warning(s)" in good.stdout, good.stdout)
bad = run([PY, "-I", os.path.join(HERE, "timing_lint.py"), os.path.join(fx, "cues_bad.json"), os.path.join(fx, "words.json"), "--audience", "adult"])
expect = ["tag appears 0.30 s before its word", "under the 1.5 s minimum", "anchored to mention 2", "not found in the timings",
          "reading time is 2.27 s", "before its first word", "3 lines", "more than two tags"]
missing = [e for e in expect if e not in bad.stdout]
check("timing_lint: broken cues fail (exit 1) with every expected finding", bad.returncode == 1 and not missing, f"missing: {missing}\n{bad.stdout}")

if shutil.which("node"):
    r = run(["node", os.path.join(HERE, "sync_easing.mjs"), "--check"])
    check("example pages carry exactly the easing.mjs code (no drift)", r.returncode == 0, r.stdout + r.stderr)

tmp = tempfile.mkdtemp(prefix="motion_selftest_")
try:
    # 2b. timing linter on bad input: a clean message and exit 1, never a traceback
    def lint(cues, words, *extra):
        cp, wp = os.path.join(tmp, "c.json"), os.path.join(tmp, "w.json")
        open(cp, "w", encoding="utf-8").write(cues)
        open(wp, "w", encoding="utf-8").write(words)
        return run([PY, "-I", os.path.join(HERE, "timing_lint.py"), cp, wp, *extra])
    W2 = json.dumps([{"word": "fat", "start": 1.0, "end": 1.3}, {"word": "floats", "start": 1.3, "end": 1.8}])
    r = lint("", W2)
    check("timing_lint: an empty cues file is refused cleanly", r.returncode == 1 and "Traceback" not in r.stderr, r.stderr)
    r = lint("[]", json.dumps([{"word": "floats", "start": 1.3, "end": 1.8}, {"word": "fat", "start": 1.0, "end": 1.3}]))
    r2 = lint(json.dumps([{"kind": "tag", "text": "fat", "start": 1.0, "end": 3.0}]), json.dumps([{"word": "floats", "start": 1.3, "end": 1.8}, {"word": "fat", "start": 1.0, "end": 1.3}]))
    check("timing_lint: word timings out of order are refused", r2.returncode == 1 and "out of order" in r2.stderr, r2.stderr)
    W3 = json.dumps([{"word": "café,", "start": 1.0, "end": 1.3}, {"word": "दिल", "start": 2.0, "end": 2.4}])
    r = lint(json.dumps([{"id": "a", "kind": "tag", "text": "café", "start": 1.0, "end": 3.0}, {"id": "b", "kind": "tag", "text": "दिल", "start": 2.0, "end": 4.0}]), W3)
    check("timing_lint: accented and Devanagari words are matched", r.returncode == 0 and "0 error(s)" in r.stdout, r.stdout + r.stderr)
    LONG = json.dumps([{"id": "s", "kind": "subtitle", "text": "x " * 16 + "end", "start": 1.0, "end": 9.0}])
    W4 = json.dumps([{"word": w, "start": 1.0 + i * 0.4, "end": 1.3 + i * 0.4} for i, w in enumerate(["x"] * 16 + ["end"])])
    r_wide = lint(LONG, W4)
    r_port = lint(LONG, W4, "--portrait")
    check("timing_lint: --portrait applies the 32-character line limit (wide default 42 does not flag a 35-character line)",
          "longest line" not in r_wide.stdout and "limit 32" in r_port.stdout, r_wide.stdout + r_port.stdout)

    # 3. contact sheet
    try:
        from PIL import Image
        d = os.path.join(tmp, "stills"); os.makedirs(d)
        for i, c in enumerate([(200, 60, 60), (60, 60, 200), (60, 160, 60), (220, 180, 40), (120, 120, 120)]):
            Image.new("RGB", (320 if i % 2 == 0 else 200, 180 if i % 2 == 0 else 300), c).save(os.path.join(d, f"shot_{i:02d}.png"))
        out = os.path.join(tmp, "sheet.png")
        r = run([PY, "-I", os.path.join(HERE, "contact_sheet.py"), d, "--out", out, "--cols", "3", "--cell", "160"])
        ok = r.returncode == 0 and os.path.exists(out)
        if ok:
            im = Image.open(out); ok = im.width >= 3 * 160 and im.height > 2 * 100
        check("contact_sheet: 5 mixed-size stills in 3 columns", ok, r.stdout + r.stderr)
        r = run([PY, "-I", os.path.join(HERE, "contact_sheet.py"), d, "--out", os.path.join(tmp, "split.png"), "--max", "2"])
        check("contact_sheet: --max splits into several sheets", r.returncode == 0 and len(r.stdout.split()) == 3, r.stdout + r.stderr)
    except ImportError:
        print("SKIP contact_sheet test (Pillow not installed)")

    # 4. frame strip
    if shutil.which("ffmpeg") and shutil.which("ffprobe"):
        clip = os.path.join(tmp, "clip.mp4")
        r = run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "testsrc2=size=320x180:rate=30:duration=4", "-pix_fmt", "yuv420p", clip])
        out = os.path.join(tmp, "strip.png")
        r2 = run([PY, "-I", os.path.join(HERE, "frame_strip.py"), clip, "--out", out, "--t0", "1", "--t1", "3", "--n", "8", "--cols", "4", "--width", "160"])
        ok = r.returncode == 0 and r2.returncode == 0 and os.path.exists(out) and os.path.exists(out + ".txt")
        if ok:
            times = [float(l.split(":")[1].split()[0]) for l in open(out + ".txt").read().split("\n") if l]
            ok = len(times) == 8 and abs(times[0] - 1.125) < 1e-6 and abs(times[-1] - 2.875) < 1e-6
            try:
                from PIL import Image
                im = Image.open(out); ok = ok and im.width >= 4 * 160 and im.height >= 2 * 90
            except ImportError:
                pass
        check("frame_strip: 8 cells from a 4 s synthetic clip, times 1.125 .. 2.875", ok, r.stderr + r2.stdout + r2.stderr)
        r3 = run([PY, "-I", os.path.join(HERE, "frame_strip.py"), clip, "--out", out, "--t0", "3", "--t1", "9"])
        check("frame_strip: a window outside the clip is refused", r3.returncode != 0, r3.stdout)
        aud = os.path.join(tmp, "a.m4a")
        run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "sine=duration=1", aud])
        r4 = run([PY, "-I", os.path.join(HERE, "frame_strip.py"), aud, "--out", out])
        check("frame_strip: a file with no video frames is refused with a clear message", r4.returncode != 0 and "no video stream" in (r4.stdout + r4.stderr), r4.stdout + r4.stderr)
    else:
        print("SKIP frame_strip test (ffmpeg not found)")
finally:
    shutil.rmtree(tmp, ignore_errors=True)

print(f"{sum(results)} of {len(results)} checks passed")
sys.exit(0 if all(results) else 1)
