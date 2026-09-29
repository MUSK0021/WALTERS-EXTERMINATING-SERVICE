"""Colour illustrations of the pests, drawn as SVG.

The line icons that were here first read as generic bug shapes: at tile size a
cockroach and a beetle and a tick were the same grey outline. These are proper
little portraits instead, in the colour each thing actually is, so somebody
scanning the page recognises what they have got without reading the label.

House style, so twenty drawings look like one set:
  * 64x64 box, the creature filling roughly 46 of it, on a soft tinted disc
  * two tone bodies, light from the top left, one soft highlight, no outlines
  * real colours, not brand colours: a roach is chestnut, a mouse is warm grey
  * legs and antennae are strokes with round caps, always darker than the body
  * nothing cute, nothing gory. These sit next to the words "bed bugs" on a
    page somebody reads when they are already unhappy.

Gradient ids are namespaced per slug because a page can show many at once.
"""

# body, shadow, detail, and the disc behind
PALETTE = {
    'roach':      ('#b4703a', '#7d4520', '#5a3117', '#f3e6d8'),
    'ant':        ('#a4472c', '#6e2b18', '#4a1d10', '#f4e3dc'),
    'mouse':      ('#a99a8c', '#7c6e61', '#584d43', '#efebe6'),
    'rat':        ('#8d8378', '#625950', '#443d36', '#ebe9e6'),
    'bed-bugs':   ('#b0603c', '#7c3d22', '#552615', '#f5e4dc'),
    'wasps':      ('#e0a92b', '#b07c14', '#2f2a20', '#faeed2'),
    'hornets':    ('#c9932f', '#8f6516', '#2c2721', '#f7ead0'),
    'bees':       ('#d9a53a', '#a3761d', '#3a3228', '#f9eed6'),
    'spiders':    ('#6b5546', '#453429', '#2a1f18', '#ece7e2'),
    'fleas':      ('#8a4b2c', '#5d2f19', '#3d1d0f', '#f2e4dc'),
    'ticks':      ('#9a5a33', '#6b3a1e', '#4a2612', '#f3e6de'),
    'silverfish': ('#a7adb4', '#7b838b', '#565d64', '#eceef0'),
    'earwigs':    ('#8e5a34', '#61391e', '#412512', '#f1e6dd'),
    'crickets':   ('#7a6a3f', '#54492a', '#38301b', '#efece0'),
    'millipedes': ('#7a5236', '#523420', '#361f12', '#efe7e0'),
    'pantry':     ('#c2a06a', '#8f7343', '#5f4c2b', '#f6eede'),
    'groundhogs': ('#9a7b57', '#6e5639', '#4b3a26', '#f0e9e0'),
    'raccoons':   ('#8d8d92', '#5f5f66', '#37373d', '#eaeaee'),
    'squirrels':  ('#a3764a', '#75522f', '#4e371f', '#f2e9de'),
    'flies':      ('#5c6168', '#3a3e44', '#23262a', '#e9ebed'),
}

# every pest slug maps to one of the drawings above
ALIAS = {'pantry-pests': 'pantry', 'roaches': 'roach', 'ants': 'ant',
         'mice': 'mouse', 'rats': 'rat'}


def _defs(key, body, shade):
    return (f'<linearGradient id="g-{key}" x1="0" y1="0" x2="0.35" y2="1">'
            f'<stop offset="0" stop-color="{body}"/><stop offset="1" stop-color="{shade}"/>'
            f'</linearGradient>')


def _shell(key, disc, inner, defs=''):
    """Disc, then the drawing. The disc keeps the tiles even when shapes differ."""
    return (f'<svg class="pest-art" viewBox="0 0 64 64" role="img" aria-hidden="true" focusable="false">'
            f'<defs>{defs}</defs>'
            f'<circle cx="32" cy="32" r="31" fill="{disc}"/>{inner}</svg>')


def _gloss(cx, cy, rx, ry, rot=0, o=0.28):
    t = f' transform="rotate({rot} {cx} {cy})"' if rot else ''
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#fff" opacity="{o}"{t}/>'


def _legs(d, colour, w=2.1):
    return f'<path d="{d}" fill="none" stroke="{colour}" stroke-width="{w}" stroke-linecap="round"/>'


def _art(slug):
    key = ALIAS.get(slug, slug)
    body, shade, dark, disc = PALETTE[key]
    g = f'url(#g-{key})'
    defs = _defs(key, body, shade)

    if key == 'roach':
        inner = (
            _legs('M22 26 12 20M21 33 10 33M23 40 13 47', dark)
            + _legs('M42 26 52 20M43 33 54 33M41 40 51 47', dark)
            + _legs('M28 19C24 12 20 9 15 8', dark, 1.7)
            + _legs('M36 19C40 12 44 9 49 8', dark, 1.7)
            + f'<ellipse cx="32" cy="36" rx="13" ry="16" fill="{g}"/>'
            + f'<path d="M32 20c6 0 10 4 10 8 0 3-4 5-10 5s-10-2-10-5c0-4 4-8 10-8z" fill="{shade}"/>'
            + f'<ellipse cx="32" cy="20" rx="5.6" ry="4.4" fill="{dark}"/>'
            + f'<path d="M32 25v26" stroke="{dark}" stroke-width="1.3" opacity=".55"/>'
            + _gloss(27, 31, 4.2, 7, -16))
    elif key == 'ant':
        inner = (
            _legs('M25 30 14 22M24 34 12 34M25 38 15 46', dark)
            + _legs('M39 30 50 22M40 34 52 34M39 38 49 46', dark)
            + _legs('M27 20C23 14 20 12 16 11', dark, 1.7)
            + _legs('M37 20C41 14 44 12 48 11', dark, 1.7)
            + f'<ellipse cx="32" cy="43" rx="11" ry="12" fill="{g}"/>'
            + f'<ellipse cx="32" cy="30" rx="6" ry="5.5" fill="{shade}"/>'
            + f'<circle cx="32" cy="21" r="7" fill="{dark}"/>'
            + f'<circle cx="29.4" cy="19.6" r="1.5" fill="#fff" opacity=".8"/>'
            + _gloss(28, 40, 3.4, 5.4, -14))
    elif key in ('mouse', 'rat'):
        big = key == 'rat'
        tail = ('M46 42c9 2 12-3 10-9' if big else 'M45 40c7 2 10-2 8-7')
        inner = (
            _legs(tail, shade, 2.6)
            + f'<circle cx="41" cy="24" r="{9 if big else 8.4}" fill="{shade}"/>'
            + f'<circle cx="41" cy="24" r="{5 if big else 4.6}" fill="#e0a9a4"/>'
            + f'<path d="M13 40c0-9 8-16 18-16h4c8 0 13 5 13 12 0 8-7 14-16 14H24c-6 0-11-4-11-10z" fill="{g}"/>'
            + f'<circle cx="21.5" cy="36.5" r="2.1" fill="{dark}"/>'
            + f'<circle cx="20.9" cy="35.8" r=".7" fill="#fff"/>'
            + f'<circle cx="13.6" cy="41.4" r="2" fill="#e0a9a4"/>'
            + _legs('M14 44 8 47M17 46 12 50', shade, 1.4)
            + _gloss(27, 31, 6.5, 3.6, -18))
    elif key == 'bed-bugs':
        inner = (
            _legs('M22 28 13 23M21 34 11 34M23 40 14 45', dark)
            + _legs('M42 28 51 23M43 34 53 34M41 40 50 45', dark)
            + _legs('M28 21C25 16 22 14 19 13', dark, 1.6)
            + _legs('M36 21C39 16 42 14 45 13', dark, 1.6)
            + f'<ellipse cx="32" cy="36" rx="14" ry="13" fill="{g}"/>'
            + ''.join(f'<path d="M20 {30 + i * 5}q12 {3.4 if i else 3} 24 0" stroke="{dark}" '
                      f'stroke-width="1.3" fill="none" opacity=".5"/>' for i in range(3))
            + f'<ellipse cx="32" cy="22" rx="6.4" ry="4.6" fill="{shade}"/>'
            + _gloss(26, 31, 4.6, 3.4, -12))
    elif key in ('wasps', 'hornets', 'bees'):
        wing = '#ffffff'
        inner = (
            f'<ellipse cx="22" cy="28" rx="10" ry="5" fill="{wing}" opacity=".5" transform="rotate(-28 22 28)"/>'
            + f'<ellipse cx="42" cy="28" rx="10" ry="5" fill="{wing}" opacity=".5" transform="rotate(28 42 28)"/>'
            + _legs('M26 38 19 46M32 40 32 48M38 38 45 46', dark, 1.8)
            + f'<ellipse cx="32" cy="41" rx="9.5" ry="12" fill="{g}"/>'
            + ''.join(f'<path d="M23 {36 + i * 5.5}q9 {3.2} 18 0" stroke="{dark}" stroke-width="2.6" '
                      f'fill="none" opacity=".9"/>' for i in range(3))
            + f'<ellipse cx="32" cy="27" rx="6" ry="5" fill="{shade}"/>'
            + f'<circle cx="32" cy="18.5" r="6" fill="{dark}"/>'
            + _legs('M29 13 25 7M35 13 39 7', dark, 1.6)
            + _gloss(28, 38, 3, 5, -12))
    elif key == 'spiders':
        inner = (
            _legs('M24 30 12 20 6 24M23 35 9 34 4 40M24 40 12 48 9 54M27 44 20 54 21 60', dark, 2)
            + _legs('M40 30 52 20 58 24M41 35 55 34 60 40M40 40 52 48 55 54M37 44 44 54 43 60', dark, 2)
            + f'<ellipse cx="32" cy="38" rx="11" ry="12" fill="{g}"/>'
            + f'<circle cx="32" cy="25" r="7" fill="{shade}"/>'
            + f'<circle cx="29.5" cy="23.5" r="1.5" fill="#fff" opacity=".85"/>'
            + f'<circle cx="34.5" cy="23.5" r="1.5" fill="#fff" opacity=".85"/>'
            + _gloss(28, 35, 3.4, 5, -14))
    elif key == 'ticks':
        inner = (
            _legs('M24 30 14 24M23 35 12 35M24 40 14 46', dark, 1.9)
            + _legs('M40 30 50 24M41 35 52 35M40 40 50 46', dark, 1.9)
            + f'<ellipse cx="32" cy="37" rx="13" ry="14" fill="{g}"/>'
            + f'<path d="M32 23c6 0 9 3 9 7s-4 6-9 6-9-2-9-6 3-7 9-7z" fill="{dark}"/>'
            + f'<path d="M30 17h4l-1 6h-2z" fill="{dark}"/>'
            + _gloss(27, 33, 3.6, 5, -14))
    elif key == 'fleas':
        inner = (
            f'<path d="M40 28 52 34" stroke="{shade}" stroke-width="5.5" stroke-linecap="round"/>'
            + f'<path d="M52 34 44 50" stroke="{shade}" stroke-width="4" stroke-linecap="round"/>'
            + _legs('M44 50 50 57', dark, 2)
            + _legs('M27 40 20 50M33 43 30 54', dark, 1.9)
            + f'<path d="M36 17c9 5 12 16 7 25-4 8-14 10-21 5s-8-16-2-23c4-5 10-8 16-7z" fill="{g}"/>'
            + ''.join(f'<path d="M{20 + i * 5} {26 + i * 2}q6 8 10 12" stroke="{dark}" stroke-width="1.2" '
                      f'fill="none" opacity=".4"/>' for i in range(3))
            + _legs('M35 13 41 6M40 16 48 12', dark, 1.6)
            + f'<circle cx="35" cy="22" r="1.6" fill="#fff" opacity=".7"/>'
            + _gloss(26, 26, 3.2, 5.2, -32))
    elif key == 'silverfish':
        inner = (
            f'<path d="M50 32c0 6-8 10-18 10s-18-4-18-10 8-10 18-10 18 4 18 10z" fill="{g}"/>'
            + ''.join(f'<path d="M{24 + i * 6} 23q2 9 0 18" stroke="{dark}" stroke-width="1.2" '
                      f'fill="none" opacity=".45"/>' for i in range(4))
            + _legs('M50 32 60 26M50 32h10M50 32 60 38', dark, 1.6)
            + _legs('M15 27 6 21M15 37 6 43', dark, 1.6)
            + f'<circle cx="47" cy="29.5" r="1.4" fill="#fff" opacity=".75"/>'
            + _gloss(28, 27, 7, 2.6, -8))
    elif key == 'earwigs':
        inner = (
            _legs('M24 28 15 22M23 33 13 33M24 38 15 44', dark, 1.8)
            + _legs('M38 28 47 22M39 33 49 33M38 38 47 44', dark, 1.8)
            + f'<ellipse cx="31" cy="33" rx="14" ry="8" fill="{g}"/>'
            + f'<circle cx="17" cy="33" r="6" fill="{shade}"/>'
            + _legs('M14 29 7 24M14 37 7 42', dark, 1.6)
            + f'<path d="M45 27c8 2 10 4 10 6M45 39c8-2 10-4 10-6" fill="none" stroke="{dark}" '
              f'stroke-width="2.6" stroke-linecap="round"/>'
            + _gloss(27, 30, 5, 2.6, -8))
    elif key == 'crickets':
        inner = (
            _legs('M26 32 16 25M25 37 14 39', dark, 1.8)
            + f'<path d="M40 34 52 27" stroke="{shade}" stroke-width="6.5" stroke-linecap="round"/>'
            + f'<path d="M52 27 47 47" stroke="{shade}" stroke-width="4.5" stroke-linecap="round"/>'
            + _legs('M47 47 54 55', dark, 2.2)
            + f'<ellipse cx="29" cy="36" rx="14" ry="8.5" fill="{g}"/>'
            + f'<path d="M18 30q12 2 22 3" stroke="{dark}" stroke-width="1.3" fill="none" opacity=".45"/>'
            + f'<circle cx="16" cy="31" r="6.6" fill="{shade}"/>'
            + _legs('M12 26 3 17M17 25 14 14', dark, 1.6)
            + f'<circle cx="13.8" cy="29.4" r="1.5" fill="#fff" opacity=".85"/>'
            + _gloss(26, 32, 5.4, 2.8, -10))
    elif key == 'millipedes':
        inner = (
            f'<path d="M32 44a12 12 0 1 1 12-12 17 17 0 1 1-17 17" fill="none" stroke="{g}" '
            f'stroke-width="6" stroke-linecap="round"/>'
            + _legs('M13 27 6 23M14 38 7 41M20 46 17 53M30 50 30 57M39 48 43 55M47 42 54 46', dark, 1.7)
            + f'<circle cx="44" cy="32" r="3.2" fill="{shade}"/>'
            + _legs('M46 29 52 25M46 35 52 38', dark, 1.5)
            + _gloss(22, 20, 3.6, 2, -34, 0.34))
    elif key == 'pantry':
        inner = (
            f'<path d="M24 14h16v6H24z" fill="{shade}"/>'
            + f'<path d="M22 20h20a4 4 0 0 1 4 4v22a4 4 0 0 1-4 4H22a4 4 0 0 1-4-4V24a4 4 0 0 1 4-4z" fill="{g}"/>'
            + f'<path d="M18 30h28" stroke="{dark}" stroke-width="1.6" opacity=".45"/>'
            + f'<ellipse cx="28" cy="38" rx="2.6" ry="1.8" fill="{dark}" opacity=".7"/>'
            + f'<ellipse cx="36" cy="43" rx="2.6" ry="1.8" fill="{dark}" opacity=".7"/>'
            + _gloss(25, 32, 2.6, 8, 0, 0.3))
    elif key in ('groundhogs', 'raccoons', 'squirrels'):
        # the three mammals shared one face and were hard to tell apart, so each
        # now gets the feature people actually name it by: the squirrel's tail,
        # the raccoon's mask, the groundhog's teeth
        pointy = key == 'squirrels'
        ear = 6 if pointy else 7
        if pointy:
            ears = (f'<path d="M15 24 18 11l8 7z" fill="{shade}"/><path d="M49 24 46 11l-8 7z" fill="{shade}"/>'
                    f'<path d="M17.5 21.5 19 15l4 3.4z" fill="#e0a9a4" opacity=".8"/>'
                    f'<path d="M46.5 21.5 45 15l-4 3.4z" fill="#e0a9a4" opacity=".8"/>')
            head = 'M32 17c9 0 15 8 15 17s-6 15-15 15-15-6-15-15 6-17 15-17z'
        else:
            ears = (f'<circle cx="20" cy="21" r="{ear}" fill="{shade}"/><circle cx="44" cy="21" r="{ear}" fill="{shade}"/>'
                    f'<circle cx="20" cy="21" r="{ear - 2.8}" fill="#e0a9a4" opacity=".8"/>'
                    f'<circle cx="44" cy="21" r="{ear - 2.8}" fill="#e0a9a4" opacity=".8"/>')
            head = 'M32 15c10 0 17 8 17 18s-7 17-17 17-17-7-17-17 7-18 17-18z'

        inner = ''
        if pointy:
            inner += (f'<path d="M48 50c9-3 13-13 10-22-2-7-9-11-15-9" fill="none" stroke="{shade}" '
                      f'stroke-width="8" stroke-linecap="round"/>'
                      f'<path d="M48 50c6-3 9-11 7-18" fill="none" stroke="{body}" '
                      f'stroke-width="3" stroke-linecap="round" opacity=".55"/>')
        inner += ears + f'<path d="{head}" fill="{g}"/>'
        if key == 'raccoons':
            inner += (f'<path d="M16 31c4-4 10-6 16-6s12 2 16 6c-2 6-8 9-16 9s-14-3-16-9z" fill="{dark}" opacity=".85"/>'
                      f'<path d="M32 14c2 4 2 8 0 11-2-3-2-7 0-11z" fill="{dark}" opacity=".5"/>')
        eye_y = 33 if not pointy else 34
        inner += (f'<circle cx="26" cy="{eye_y}" r="2.5" fill="{dark}"/><circle cx="25.2" cy="{eye_y - .9}" r=".85" fill="#fff"/>'
                  f'<circle cx="38" cy="{eye_y}" r="2.5" fill="{dark}"/><circle cx="37.2" cy="{eye_y - .9}" r=".85" fill="#fff"/>'
                  f'<ellipse cx="32" cy="{eye_y + 7}" rx="3" ry="2.2" fill="{dark}"/>')
        if key == 'groundhogs':
            inner += (f'<path d="M29.4 43h5.2v6a2.6 2.6 0 0 1-5.2 0z" fill="#fff"/>'
                      f'<path d="M32 43v6" stroke="{dark}" stroke-width="1" opacity=".4"/>')
        else:
            inner += f'<path d="M32 {eye_y + 9}v3M28 {eye_y + 12}h8" stroke="{dark}" stroke-width="1.6" fill="none" stroke-linecap="round"/>'
        inner += _gloss(26, 26, 4.4, 3, -20)
    elif key == 'flies':
        inner = (
            f'<ellipse cx="19" cy="29" rx="11" ry="5.4" fill="#fff" opacity=".45" transform="rotate(-26 19 29)"/>'
            + f'<ellipse cx="45" cy="29" rx="11" ry="5.4" fill="#fff" opacity=".45" transform="rotate(26 45 29)"/>'
            + _legs('M26 40 19 49M32 42 32 51M38 40 45 49', dark, 1.8)
            + f'<ellipse cx="32" cy="38" rx="9.5" ry="12" fill="{g}"/>'
            + f'<path d="M24 34q8 3 16 0M24 40q8 3 16 0" stroke="{dark}" stroke-width="1.3" '
              f'fill="none" opacity=".5"/>'
            + f'<circle cx="32" cy="22" r="7.5" fill="{shade}"/>'
            + f'<circle cx="27.5" cy="21" r="3.6" fill="#a8483a"/>'
            + f'<circle cx="36.5" cy="21" r="3.6" fill="#a8483a"/>'
            + _gloss(28, 35, 3, 5, -12))
    else:
        raise KeyError(slug)

    return _shell(key, disc, inner, defs)


_CACHE = {}


def pest_art(slug):
    """SVG for a pest slug. Falls back to the roach drawing for anything unknown."""
    key = ALIAS.get(slug, slug)
    if key not in PALETTE:
        key = 'roach'
    if key not in _CACHE:
        _CACHE[key] = _art(key)
    return _CACHE[key]


def has_art(slug):
    return ALIAS.get(slug, slug) in PALETTE

# ---------------------------------------------------------------- services

# The service cards had grey line icons in grey tiles, which read as filler next
# to the colour drawings. These are in the same style: tinted disc, two tone
# shapes, light from the top left. Three are drawn here; the other three reuse
# the creature the service is about, which is more use than a generic symbol.

SERVICE_PALETTE = {
    'house':   ('#c26b4a', '#94472c', '#5f2c1a', '#f6e8e0'),
    'shop':    ('#5c8390', '#3d5d68', '#26404a', '#e4eef0'),
    'glass':   ('#7f8f7c', '#5a6a58', '#3a473a', '#e9efe7'),
}

SERVICE_MAP = {
    'home-pest-control': 'house',
    'commercial-pest-control': 'shop',
    'bed-bugs': 'bed-bugs',
    'rodents-and-wildlife': 'mouse',
    'bees-wasps-hornets': 'wasps',
}


def _service_art(key):
    body, shade, dark, disc = SERVICE_PALETTE[key]
    g = f'url(#g-{key})'
    defs = _defs(key, body, shade)

    if key == 'house':
        inner = (
            f'<path d="M10 32 32 14l22 18v20a3 3 0 0 1-3 3H13a3 3 0 0 1-3-3z" fill="#f1e7dc"/>'
            + f'<path d="M6 33 32 12l26 21" fill="none" stroke="{g}" stroke-width="7" '
              f'stroke-linecap="round" stroke-linejoin="round"/>'
            + f'<rect x="27" y="40" width="10" height="15" rx="1.5" fill="{dark}"/>'
            + f'<circle cx="34.6" cy="47.6" r="1" fill="#f1e7dc"/>'
            + f'<rect x="15" y="38" width="8" height="8" rx="1.2" fill="#9fb6bd"/>'
            + f'<rect x="41" y="38" width="8" height="8" rx="1.2" fill="#9fb6bd"/>'
            + f'<path d="M19 38v8M15 42h8M45 38v8M41 42h8" stroke="#f1e7dc" stroke-width="1.2"/>'
            + _gloss(21, 26, 5, 2.6, -40, 0.35))
    elif key == 'shop':
        inner = (
            f'<rect x="11" y="24" width="42" height="31" rx="2.5" fill="#e7edef"/>'
            + f'<path d="M9 24h46l-4-9H13z" fill="{g}"/>'
            + ''.join(f'<rect x="{13 + i * 8}" y="15" width="4" height="9" fill="#fff" opacity=".25"/>'
                      for i in range(3))
            + f'<rect x="16" y="30" width="13" height="11" rx="1.2" fill="#9fb6bd"/>'
            + f'<rect x="35" y="30" width="13" height="11" rx="1.2" fill="#9fb6bd"/>'
            + f'<rect x="25" y="44" width="14" height="11" rx="1.2" fill="{dark}"/>'
            + f'<circle cx="36.4" cy="50" r="1" fill="#e7edef"/>'
            + _gloss(20, 33, 4, 2.2, -30, 0.4))
    elif key == 'glass':
        inner = (
            f'<circle cx="28" cy="28" r="14" fill="none" stroke="{g}" stroke-width="6"/>'
            + f'<circle cx="28" cy="28" r="10.5" fill="#cfe0e4" opacity=".55"/>'
            + f'<path d="M38.5 38.5 52 52" stroke="{shade}" stroke-width="7" stroke-linecap="round"/>'
            + f'<path d="M22 22a8 8 0 0 1 6-3" stroke="#fff" stroke-width="2.4" fill="none" '
              f'stroke-linecap="round" opacity=".8"/>')
    else:
        raise KeyError(key)
    return _shell(key, disc, inner, defs)


def service_art(slug):
    """Colour drawing for a service card. Falls back to the magnifier."""
    key = SERVICE_MAP.get(slug)
    if key in SERVICE_PALETTE:
        ck = 'svc-' + key
        if ck not in _CACHE:
            _CACHE[ck] = _service_art(key)
        return _CACHE[ck]
    if key and has_art(key):
        return pest_art(key)
    if 'svc-glass' not in _CACHE:
        _CACHE['svc-glass'] = _service_art('glass')
    return _CACHE['svc-glass']
