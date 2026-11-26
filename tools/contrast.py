#!/usr/bin/env python3
"""VIXEN contrast measurement (rubric v1.1).

Usage:
  python contrast.py boxes.json [--out contrast_final.json] [--montage montage.png]

boxes.json format:
{
  "image_dir": "/path/to/images",
  "images": {
    "01": {"file": "name.jpeg",
           "boxes": [ {"element": "Name", "role": "primary", "box": [x0,y0,x1,y1], "pad": 3} ]}
  }
}
role: "primary" | "secondary" | "icon". "pad" is optional (default 3; use 0 for tight boxes).
Boxes are pixel coordinates of the ORIGINAL image. ALWAYS check the montage (and zoom crops of
doubtful boxes) before trusting any number: several boxes in earlier batches missed their text.
Measure gradient/photo backgrounds one text line at a time.
"""
import sys, json, argparse
import numpy as np
from PIL import Image, ImageDraw

def lum(c):
    c = np.array(c, float) / 255
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]

def cr(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

hx = lambda c: '#%02X%02X%02X' % tuple(int(round(v)) for v in c)

def measure(imarr, box, pad=3):
    """Returns (bg_hex, fg_hex, ratio_low, ratio_est, assumed)."""
    H, W = imarr.shape[:2]
    x0, y0, x1, y1 = box
    x0 = max(0, x0 - pad); y0 = max(0, y0 - pad); x1 = min(W, x1 + pad); y1 = min(H, y1 + pad)
    p = imarr[y0:y1, x0:x1].reshape(-1, 3).astype(float)
    q = (p // 16).astype(int)
    keys = q[:, 0] * 256 + q[:, 1] * 16 + q[:, 2]
    vals, cnt = np.unique(keys, return_counts=True)
    bg = p[keys == vals[cnt.argmax()]].mean(0)               # dominant color in the box
    L = np.array([lum(c) for c in p])
    d = np.abs(L - lum(bg))
    order = np.argsort(d)
    n = len(d)
    lo_n = max(6, int(n * 0.04)); hi_n = max(3, int(n * 0.015))
    fg_low = p[order[-lo_n:]].mean(0)                          # conservative: top ~4% most distant pixels
    fg_est = p[order[-hi_n:]].mean(0)                          # best estimate: top ~1.5%
    assumed = None
    sat = (bg.max() - bg.min()) / max(bg.max(), 1)
    if sat >= 0.4 and fg_est.min() >= 170 and lum(fg_est) > lum(bg):
        fg_est = np.array([255., 255, 255]); assumed = 'white'   # small white text on saturated bg
    elif sat >= 0.4 and fg_est.max() <= 60 and lum(fg_est) < lum(bg):
        fg_est = np.array([0., 0, 0]); assumed = 'black'
    r_low = round(float(cr(fg_low, bg)), 2)
    r_est = round(float(cr(fg_est, bg)), 2)
    if assumed:
        r_low = r_est                                           # when assumed, both values are equal
    return hx(bg), hx(fg_est), r_low, r_est, assumed

def run(cfg_path, out_path, montage_path=None):
    cfg = json.load(open(cfg_path))
    base = cfg.get('image_dir', '.').rstrip('/\\')
    res = {}
    for key, spec in cfg['images'].items():
        im = np.array(Image.open(f"{base}/{spec['file']}").convert('RGB'))
        out = []
        for b in spec['boxes']:
            bg, fg, rl, re, ass = measure(im, b['box'], b.get('pad', 3))
            out.append(dict(element=b['element'], role=b['role'], bg=bg, fg=fg, ratio=re, ratio_low=rl, fg_assumed=ass))
        res[key] = out
    json.dump(res, open(out_path, 'w'), indent=1)
    if montage_path:
        W = 360; tiles = []
        for key, spec in cfg['images'].items():
            im = Image.open(f"{base}/{spec['file']}").convert('RGB'); d = ImageDraw.Draw(im)
            for b in spec['boxes']: d.rectangle(b['box'], outline=(255, 0, 255), width=2)
            r = W / im.size[0]; tiles.append(im.resize((W, int(im.size[1] * r))))
        cols = 4; rows = [tiles[i:i + cols] for i in range(0, len(tiles), cols)]
        H = [max(t.size[1] for t in r) for r in rows]
        M = Image.new('RGB', (W * cols, sum(H)), (40, 40, 40)); y = 0
        for r, h in zip(rows, H):
            for i, t in enumerate(r): M.paste(t, (i * W, y))
            y += h
        M.save(montage_path)
    return res

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('config'); ap.add_argument('--out', default='contrast_final.json'); ap.add_argument('--montage')
    a = ap.parse_args()
    res = run(a.config, a.out, a.montage)
    for k, v in res.items():
        for o in v:
            flag = ' <-- below 3' if o['ratio'] < 3 else ''
            print(k, o['element'], o['role'], 'low', o['ratio_low'], 'est', o['ratio'], flag)
