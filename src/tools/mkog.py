"""Build the social share image.

    python3 tools/mkog.py          # writes static/og.jpg (1200x630)

The card is the van photo, darkened the same way the hero is, with the real oval
badge on it rather than a typeset approximation. The badge is rendered from the
same outlines the site uses (logo_paths.py) by way of a headless Chrome pass, so
the logo on a shared link is the identical artwork.
"""
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PIL import Image, ImageDraw, ImageFont  # noqa: E402

from logo_paths import LETTERS, OVAL_H, OVAL_W  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
SRC = os.path.join(ROOT, '_source-photos', '004.jpg')
OUT = os.path.join(ROOT, 'static', 'og.jpg')

W, H = 1200, 630
GREEN = (65, 80, 79)
BADGE_W = 400


def badge_png(width):
    """Rasterise the oval badge, white on transparent, via headless Chrome."""
    height = round(width * OVAL_H / OVAL_W)
    html = (f'<!doctype html><meta charset=utf-8>'
            f'<style>html,body{{margin:0;background:transparent}}</style>'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {OVAL_W} {OVAL_H}">'
            f'<ellipse cx="{OVAL_W / 2}" cy="{OVAL_H / 2}" rx="{OVAL_W / 2}" ry="{OVAL_H / 2}" fill="#fff"/>'
            f'<g fill="#41504f">{LETTERS}</g></svg>')
    with tempfile.TemporaryDirectory() as d:
        page = os.path.join(d, 'b.html')
        png = os.path.join(d, 'b.png')
        open(page, 'w').write(html)
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
                        '--default-background-color=00000000',
                        f'--window-size={width},{height}', f'--screenshot={png}',
                        '--virtual-time-budget=2500', page],
                       capture_output=True, timeout=60)
        return Image.open(png).convert('RGBA').copy()


def main():
    photo = Image.open(SRC).convert('RGB')
    # cover-crop to 1200x630
    scale = max(W / photo.width, H / photo.height)
    photo = photo.resize((round(photo.width * scale), round(photo.height * scale)), Image.LANCZOS)
    left = (photo.width - W) // 2
    top = max(0, (photo.height - H) // 2)
    card = photo.crop((left, top, left + W, top + H))

    # the same left-weighted wedge the hero uses, so the two read as one design
    scrim = Image.new('RGBA', (W, H))
    d = ImageDraw.Draw(scrim)
    for x in range(W):
        t = x / W
        # near solid under the words, easing off only in the last third so the
        # van and its own lettering still read
        a = int(240 - 168 * min(1.0, max(0.0, (t - 0.36) / 0.56)) ** 1.7)
        d.line([(x, 0), (x, H)], fill=(8, 11, 10, max(a, 66)))
    card = Image.alpha_composite(card.convert('RGBA'), scrim)

    badge = badge_png(BADGE_W)
    card.alpha_composite(badge, (72, 64))

    d = ImageDraw.Draw(card)
    def font(path, size):
        return ImageFont.truetype(path, size)

    fr = os.path.join(ROOT, 'static', 'assets', 'fonts', 'fraunces.woff2')
    # Pillow cannot read woff2, so use the system serif for the headline and
    # Helvetica for the supporting lines. Close enough at this size.
    head = font('/System/Library/Fonts/Supplemental/Georgia Bold.ttf', 62)
    sub = font('/System/Library/Fonts/Supplemental/Arial.ttf', 30)
    small = font('/System/Library/Fonts/Supplemental/Arial.ttf', 26)

    d.text((74, 318), 'Two generations of', font=head, fill=(255, 255, 255))
    d.text((74, 388), 'getting rid of them.', font=head, fill=(186, 205, 201))
    d.text((78, 484), 'Family owned since 1963  ·  Northeast Philadelphia',
           font=sub, fill=(255, 255, 255))
    d.text((78, 528), '(215) 947-8818  ·  PA licence BU0014', font=small, fill=(196, 208, 205))

    # a thin brand rule along the bottom, the one place the green is solid
    d.rectangle([0, H - 9, W, H], fill=GREEN)

    card.convert('RGB').save(OUT, quality=86, optimize=True)
    print(f'wrote static/og.jpg ({os.path.getsize(OUT) // 1024} KB, {W}x{H})')


if __name__ == '__main__':
    sys.exit(main())
