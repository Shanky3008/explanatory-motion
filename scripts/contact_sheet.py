#!/usr/bin/env python3
"""Contact sheet from a folder (or list) of still images, with a label under each cell.

usage:
  python contact_sheet.py DIR_OR_FILES... --out sheet.png [--cols 4] [--cell 480] [--max 48]

Needs Pillow (pip install pillow). Sorts files by name. Each cell is scaled to fit CELL pixels wide, keeping the
aspect ratio, on a mid-grey ground, with the file name under it. Long lists are split into several sheets of --max cells
(sheet_01.png, sheet_02.png, ...). Look at the sheet at a size where labels are readable: that is the point.
"""
import argparse, os, sys

try:
    from PIL import Image, ImageDraw
except ImportError:
    sys.exit("Pillow is required: pip install pillow")

EXT = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}


def collect(items):
    files = []
    for it in items:
        if os.path.isdir(it):
            files += [os.path.join(it, f) for f in sorted(os.listdir(it)) if os.path.splitext(f)[1].lower() in EXT]
        elif os.path.isfile(it):
            files.append(it)
        else:
            sys.exit(f"not found: {it}")
    return files


def make_sheet(files, out, cols, cell):
    imgs = []
    for f in files:
        try:
            im = Image.open(f).convert("RGB")
        except Exception as e:
            sys.exit(f"cannot read image {f}: {e.__class__.__name__}")
        h = max(1, round(im.height * cell / im.width))
        imgs.append((os.path.basename(f), im.resize((cell, h), Image.LANCZOS)))
    rows = (len(imgs) + cols - 1) // cols
    pad, label_h = 8, 18
    row_h = []
    for r in range(rows):
        row = imgs[r * cols:(r + 1) * cols]
        row_h.append(max(i.height for _, i in row) + label_h + pad)
    W = cols * (cell + pad) + pad
    H = sum(row_h) + pad
    sheet = Image.new("RGB", (W, H), (110, 110, 110))
    d = ImageDraw.Draw(sheet)
    y = pad
    for r in range(rows):
        for c, (name, im) in enumerate(imgs[r * cols:(r + 1) * cols]):
            x = pad + c * (cell + pad)
            sheet.paste(im, (x, y))
            d.text((x, y + im.height + 3), name[: cell // 6], fill=(255, 255, 255))
        y += row_h[r]
    sheet.save(out)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inputs", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--cell", type=int, default=480)
    ap.add_argument("--max", type=int, default=48)
    a = ap.parse_args()
    if a.cols < 1 or a.cell < 16 or a.max < 1:
        sys.exit("--cols and --max must be at least 1 and --cell at least 16")
    files = collect(a.inputs)
    if not files:
        sys.exit("no images found")
    base, ext = os.path.splitext(a.out)
    chunks = [files[i:i + a.max] for i in range(0, len(files), a.max)]
    outs = []
    for k, ch in enumerate(chunks, 1):
        out = a.out if len(chunks) == 1 else f"{base}_{k:02d}{ext or '.png'}"
        outs.append(make_sheet(ch, out, a.cols, a.cell))
    for o in outs:
        print(o)


if __name__ == "__main__":
    main()
