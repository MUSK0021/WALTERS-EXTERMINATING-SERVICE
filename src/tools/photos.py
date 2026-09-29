"""Prepare the site photos.

    python3 tools/photos.py

Two sources:
  local  - the real Walters Exterminating photos saved from their old site (_source-photos/).
           These are the good stuff: the van, the team, the 1970s archive shots.
  pexels - stock, cached in _photos/px-<id>.jpg, used only where no real photo exists.

Output: static/assets/img/photos/<name>.webp, plus <name>-sm.webp where a smaller
file actually saves bytes, and photos.json with the dimensions build.py needs.

crop is (left, top, right, bottom) as fractions of the original, applied before resizing,
so a tall phone photo can become a wide hero without squashing anyone's head.
"""
import concurrent.futures
import json
import os
import urllib.request

from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, '_photos')
SOURCE = os.path.join(ROOT, '_source-photos')
OUT = os.path.join(ROOT, 'static', 'assets', 'img', 'photos')

# name, source ('local:<file>' or a pexels id), large width, small width or None, quality, crop or None
#
# Every photo on this site is a real Walters Exterminating photo, saved from their
# own site. No stock. The pest library uses icons instead of generic bug photography,
# which keeps the imagery honest and the page fast.
PHOTOS = [
    # hero slideshow (wide)
    ('hero-van', 'local:004.jpg', 1600, 900, 76, None),
    ('hero-porch', 18326826, 2000, 1100, 66, (0.0, 0.04, 1.0, 0.92)),
    ('hero-street', 37487174, 2000, 1100, 64, (0.0, 0.12, 1.0, 0.80)),

    # services
    ('service-bedbug', 'local:001.jpg', 1400, 800, 74, None),
    ('service-commercial', 'local:012.jpg', 1200, 700, 76, None),
    ('service-wildlife', 'local:web10.JPG', 1100, 740, 60, (0.0, 0.08, 1.0, 0.92)),
    ('service-foundation', 'local:006.jpg', 1200, 700, 76, None),
    ('service-ladder', 'local:037.jpg', 1200, 700, 74, None),

    # people and proof
    ('nolan-van', 'local:walters.jpg', 700, None, 80, None),
    ('nolan-glove', 'local:IMG_0160.jpg', 900, None, 78, None),
    ('team-inspect', 'local:web7.jpg', 900, None, 78, None),
    ('nolan-training', 'local:IMG_2541.jpg', 900, None, 78, None),
    ('team-group', 'local:IMG_2563.jpg', 900, None, 78, (0.0, 0.22, 1.0, 0.78)),
    ('cage-trap', 'local:095.jpg', 1000, None, 76, None),

    # archive. Low resolution on purpose, these are old photographs.
    ('archive-1977', 'local:18E6F653.jpg', 500, None, 82, None),
    ('archive-shirt', 'local:4CAD5239.jpg', 500, None, 82, None),
    ('archive-harvey', 'local:9CCE713E.jpg', 1100, None, 78, None),
    # Page hero banners. Wide crops, because they sit behind the page title.
    # Where the company's own photograph is the stronger picture it is used;
    # stock fills the gaps they have no photograph of (a commercial kitchen,
    # a wasp nest, a macro of a roach).
    ('banner-services', 26872245, 1800, 1000, 66, (0.0, 0.06, 1.0, 0.92)),
    ('banner-commercial', 27685507, 1800, 1000, 64, (0.0, 0.16, 1.0, 0.70)),
    ('banner-wasps', 38680283, 1800, 1000, 66, None),
    ('banner-rodents', 38688419, 1900, 1040, 68, (0.0, 0.20, 1.0, 0.57)),
    ('banner-bedbugs', 8089268, 1800, 1000, 66, None),
    ('banner-home', 20185458, 1800, 1000, 58, (0.0, 0.24, 1.0, 0.61)),
    ('banner-pests', 27033323, 1800, 1000, 66, None),
    ('banner-about', 16075970, 1900, 1040, 68, (0.0, 0.28, 1.0, 0.69)),
    ('banner-area', 18280833, 1800, 1000, 64, (0.0, 0.10, 1.0, 0.92)),
    ('banner-contact', 8364960, 1800, 1000, 64, (0.0, 0.22, 1.0, 0.72)),
    ('banner-costs', 39462463, 1800, 1000, 64, (0.0, 0.18, 1.0, 0.74)),
    ('banner-pictures', 16202346, 1800, 1000, 64, (0.0, 0.30, 1.0, 0.72)),

]


def fetch(pid):
    path = os.path.join(CACHE, f'px-{pid}.jpg')
    if not os.path.exists(path):
        url = f'https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg?auto=compress&cs=tinysrgb&w=2400'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with open(path, 'wb') as f:
            f.write(urllib.request.urlopen(req, timeout=90).read())
    return path


def source_path(src):
    return os.path.join(SOURCE, src[6:]) if str(src).startswith('local:') else fetch(src)


def save(im, width, path, q):
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(path, 'WEBP', quality=q, method=6)
    return im.size


def main():
    os.makedirs(CACHE, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    remote = [p[1] for p in PHOTOS if not str(p[1]).startswith('local:')]
    if remote:
        with concurrent.futures.ThreadPoolExecutor(8) as ex:
            list(ex.map(fetch, remote))
    manifest, total = {}, 0
    for name, src, lg, sm, q, crop in PHOTOS:
        im = ImageOps.exif_transpose(Image.open(source_path(src))).convert('RGB')
        if crop:
            w, h = im.size
            im = im.crop((round(crop[0] * w), round(crop[1] * h), round(crop[2] * w), round(crop[3] * h)))
        w, h = save(im, lg, os.path.join(OUT, f'{name}.webp'), q)
        manifest[name] = {'w': w, 'h': h, 'src': src}
        small = os.path.join(OUT, f'{name}-sm.webp')
        if sm:
            manifest[name]['sw'], manifest[name]['sh'] = save(im, sm, small, q)
        elif os.path.exists(small):
            os.remove(small)
        kb = os.path.getsize(os.path.join(OUT, f'{name}.webp')) // 1024
        total += kb
        print(f'{name:24} {w}x{h:<5} {kb:>4} KB' + (f'  sm {os.path.getsize(small) // 1024} KB' if sm else ''))
    with open(os.path.join(ROOT, 'photos.json'), 'w') as f:
        json.dump(manifest, f, indent=1)
    print(f'{len(PHOTOS)} photos, {total} KB total')


if __name__ == '__main__':
    main()
