"""Generate the favicon and app icon from the same outlines as the badge.

    python3 tools/mkicons.py

Writes static/favicon.svg (vector) and static/apple-touch-icon.png (180px).
At favicon size the full oval lockup is unreadable, so the icon is the W from
the mark on a brand-green tile: same face, same shear, same green.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logo_paths import MONO, MONO_W, MONO_X0  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC = os.path.join(ROOT, 'static')
GREEN = '#41504f'
CAP = 100.0  # the MONO path is drawn at cap height 100 with its baseline at y=0


def favicon(size=64, cap_ratio=0.60, radius=0.1875):
    """Square tile, W centred optically (a hair high, because the shear reads low)."""
    cap = size * cap_ratio
    k = cap / CAP
    w = MONO_W * k
    dx = (size - w) / 2 - MONO_X0 * k
    dy = (size + cap) / 2 - size * 0.015
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" '
        f'role="img" aria-label="Walters Exterminating Service">\n'
        f'  <rect width="{size}" height="{size}" rx="{size * radius:g}" fill="{GREEN}"/>\n'
        f'  <g fill="#fff" transform="translate({dx:.3f} {dy:.3f}) scale({k:.5f})">{MONO}</g>\n'
        f'</svg>\n'
    )


def apple_touch(size=180):
    """Same tile as a PNG. Drawn from the font directly, then supersampled."""
    from PIL import Image, ImageDraw, ImageFont

    ss = 4  # supersample, then downscale, so the sheared edges stay clean
    S = size * ss
    tile = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(tile)
    d.rounded_rectangle([0, 0, S - 1, S - 1], radius=int(S * 0.1875),
                        fill=tuple(int(GREEN[i:i + 2], 16) for i in (1, 3, 5)) + (255,))

    cap = S * 0.60
    f = ImageFont.truetype('/System/Library/Fonts/Supplemental/Impact.ttf', int(cap * 1.365))
    letter = Image.new('L', (S, S), 0)
    ld = ImageDraw.Draw(letter)
    # anchor 'ls' = left baseline, so the cap sits where we expect
    ld.text((0, int(S * 0.5 + cap / 2)), 'W', font=f, fill=255, anchor='ls')

    slant = 0.205
    letter = letter.transform((S, S), Image.AFFINE, (1, slant, -slant * S * 0.42, 0, 1, 0),
                              resample=Image.BICUBIC)
    bbox = letter.getbbox()
    shift = ((S - (bbox[2] - bbox[0])) // 2 - bbox[0], 0)
    letter = letter.transform((S, S), Image.AFFINE, (1, 0, -shift[0], 0, 1, -shift[1]),
                              resample=Image.BICUBIC)

    white = Image.new('RGBA', (S, S), (255, 255, 255, 255))
    tile = Image.composite(white, tile, letter.point(lambda v: 255 if v > 127 else 0))
    tile.putalpha(Image.new('L', (S, S), 255))
    tile = tile.resize((size, size), Image.LANCZOS).convert('RGB')
    return tile


def main():
    svg_path = os.path.join(STATIC, 'favicon.svg')
    with open(svg_path, 'w') as f:
        f.write(favicon())
    print('wrote static/favicon.svg')

    png_path = os.path.join(STATIC, 'apple-touch-icon.png')
    apple_touch().save(png_path, optimize=True)
    print(f'wrote static/apple-touch-icon.png ({os.path.getsize(png_path) // 1024} KB)')


if __name__ == '__main__':
    sys.exit(main())
