#!/usr/bin/env python3
"""WCAG 2.x contrast ratio between two sRGB colors.

Accepts #rgb, #rrggbb, #rrggbbaa, rgb(r, g, b), and rgba(r, g, b, a), the
forms browsers return as computed styles. A translucent color is composited
over --over <color> (default: the background argument, then white).

Usage:
  contrast.py <fg> <bg> [--over <color>]
  contrast.py "rgba(0, 0, 0, 0.6)" "#fff"
  contrast.py --self-test
"""
import re
import sys

THRESHOLDS = [
    ("1.4.3 AA text", 4.5),
    ("1.4.3 AA large text", 3.0),
    ("1.4.6 AAA text", 7.0),
    ("1.4.6 AAA large text", 4.5),
    ("1.4.11 AA non-text UI", 3.0),
]

FUNC_RE = re.compile(r"rgba?\(\s*([\d.]+)[\s,]+([\d.]+)[\s,]+([\d.]+)(?:[\s,/]+([\d.]+%?))?\s*\)", re.I)


def parse(value):
    """Return (r, g, b, alpha) with r, g, b in 0..255 and alpha in 0..1."""
    v = value.strip()
    m = FUNC_RE.fullmatch(v)
    if m:
        r, g, b = (float(x) for x in m.group(1, 2, 3))
        a = m.group(4)
        alpha = 1.0 if a is None else (float(a[:-1]) / 100 if a.endswith("%") else float(a))
        if not all(0 <= c <= 255 for c in (r, g, b)) or not 0 <= alpha <= 1:
            raise ValueError(f"out of range: {value!r}")
        return r, g, b, alpha
    h = v.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) not in (6, 8) or any(c not in "0123456789abcdefABCDEF" for c in h):
        raise ValueError(f"not a #rgb, #rrggbb, #rrggbbaa, rgb() or rgba() color: {value!r}")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    alpha = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
    return r, g, b, alpha


def composite(color, under):
    r, g, b, a = color
    ur, ug, ub, _ = under
    return (r * a + ur * (1 - a), g * a + ug * (1 - a), b * a + ub * (1 - a), 1.0)


def channel(c8):
    c = c8 / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (channel(c) for c in rgb[:3])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg, over="#fff"):
    base = parse(over)
    if base[3] < 1:
        raise ValueError("--over must be opaque")
    b = parse(bg)
    b = composite(b, base) if b[3] < 1 else b
    f = parse(fg)
    f = composite(f, b) if f[3] < 1 else f
    hi, lo = sorted((luminance(f), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def self_test():
    assert round(ratio("#000", "#fff"), 2) == 21.0, "black on white is 21:1"
    assert ratio("#fff", "#fff") == 1.0, "same color is 1:1"
    assert ratio("#767676", "#fff") >= 4.5, "#767676 on white passes AA text"
    assert ratio("#777777", "#fff") < 4.5, "#777777 on white fails AA text"
    assert ratio("#000", "#fff") == ratio("#fff", "#000"), "order does not matter"
    assert ratio("rgb(118, 118, 118)", "rgb(255,255,255)") == ratio("#767676", "#fff"), "rgb() equals hex"
    assert ratio("rgba(0, 0, 0, 1)", "#fff") == ratio("#000", "#fff"), "opaque rgba equals hex"
    assert ratio("rgb(0 0 0 / 50%)", "#fff") == ratio("rgba(0,0,0,0.5)", "#fff"), "css4 syntax matches"
    half = ratio("rgba(0, 0, 0, 0.5)", "#fff")
    assert ratio("#808080", "#fff") * 0.98 < half < ratio("#808080", "#fff") * 1.02, "50% black over white is mid gray"
    assert abs(ratio("#00000080", "#fff") - half) < 0.05, "#rrggbbaa alpha works"
    assert ratio("rgba(255,255,255,0.5)", "rgba(0,0,0,0)", over="#000") == ratio("rgba(255,255,255,0.5)", "#000"), \
        "transparent background falls through to --over"
    for bad in ("#12", "rgb(300, 0, 0)", "hsl(0, 0%, 0%)"):
        try:
            parse(bad)
            raise AssertionError(f"bad color accepted: {bad}")
        except ValueError:
            pass
    print("contrast.py self-test: ok")


def main(argv):
    args = argv[1:]
    if args == ["--self-test"]:
        self_test()
        return 0
    over = "#fff"
    if "--over" in args:
        i = args.index("--over")
        over = args[i + 1]
        del args[i:i + 2]
    if len(args) != 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    r = ratio(args[0], args[1], over)
    print(f"{args[0]} on {args[1]}: {r:.2f}:1")
    for name, need in THRESHOLDS:
        print(f"  {'PASS' if r >= need else 'FAIL'}  {name} (needs {need}:1)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
