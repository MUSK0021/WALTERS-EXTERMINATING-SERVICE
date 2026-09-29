"""Self test for the built Walters site.

    python3 src/build.py && python3 src/check.py

Checks every built page for: broken internal links, missing images and assets,
dead anchors, heading structure, empty alt text, meta length, and any wording
left over from the old site or from the project this generator came from.
Exit code 1 if anything is wrong.
"""
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get('OUT') or os.path.dirname(ROOT)
PUBLIC = os.path.join(OUT, 'public')

problems = []
notes = []


def bad(page, msg):
    problems.append(f'{page}: {msg}')


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.srcs, self.ids = [], [], []
        self.headings, self.imgs = [], []
        self.title, self.desc, self.canonical = '', '', ''
        self.heading_text = []
        self._h = None
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.ids.append(a['id'])
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])
        if tag == 'img':
            self.srcs.append(a.get('src', ''))
            self.imgs.append((a.get('src', ''), a.get('alt'), a.get('width'), a.get('height')))
        if tag in ('link', 'script') and (a.get('href') or a.get('src')):
            self.srcs.append(a.get('href') or a.get('src'))
        if tag in ('h1', 'h2', 'h3', 'h4'):
            self.headings.append(int(tag[1]))
            self._h = len(self.heading_text)
            self.heading_text.append([tag, ''])
        if tag == 'title':
            self._in_title = True
        if tag == 'meta' and a.get('name') == 'description':
            self.desc = a.get('content', '')
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical = a.get('href', '')

    def handle_endtag(self, tag):
        if tag == 'title':
            self._in_title = False
        if tag in ('h1', 'h2', 'h3', 'h4'):
            self._h = None

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._h is not None:
            self.heading_text[self._h][1] += data


def route_for(path):
    """Map an href to the file that should serve it."""
    clean = path.split('#')[0].split('?')[0]
    if not clean or clean.startswith(('http', 'mailto:', 'tel:')):
        return None
    rel = clean.lstrip('/')
    if clean.endswith('/') or clean == '/':
        return os.path.join(PUBLIC, rel, 'index.html')
    return os.path.join(PUBLIC, rel)


def main():
    if not os.path.isdir(PUBLIC):
        print('no build found, run python3 build.py first')
        return 1

    pages = {}
    for dirpath, _, files in os.walk(PUBLIC):
        for f in files:
            if f.endswith('.html'):
                full = os.path.join(dirpath, f)
                url = '/' + os.path.relpath(full, PUBLIC).replace('index.html', '')
                url = url.replace('//', '/')
                p = Page()
                p.feed(open(full, encoding='utf-8').read())
                pages[url] = p

    print(f'{len(pages)} pages\n')

    for url, p in sorted(pages.items()):
        # links
        for href in p.links:
            target = route_for(href)
            if target and not os.path.exists(target):
                bad(url, f'dead link {href}')
            if href.startswith('#') and len(href) > 1 and href[1:] not in p.ids:
                bad(url, f'dead anchor {href}')
            if '#' in href and href.split('#')[0] in ('', '/'):
                continue

        # cross page anchors
        for href in p.links:
            if '#' in href and not href.startswith('#'):
                base, frag = href.split('#', 1)
                if base in pages and frag and frag not in pages[base].ids:
                    bad(url, f'dead anchor {href}')

        # assets
        for src in p.srcs:
            target = route_for(src)
            if target and not os.path.exists(target):
                bad(url, f'missing asset {src}')

        # headings
        h1s = [h for h in p.headings if h == 1]
        if len(h1s) != 1:
            bad(url, f'{len(h1s)} h1 tags, expected exactly 1')
        prev = 0
        for h in p.headings:
            if prev and h > prev + 1:
                bad(url, f'heading jumps from h{prev} to h{h}')
            prev = h

        # a page that opens by saying the same sentence twice reads as unfinished
        norm = [(t, ' '.join(x.split()).strip().lower().rstrip('.')) for t, x in p.heading_text]
        for i in range(len(norm) - 1):
            if norm[i][1] and norm[i][1] == norm[i + 1][1]:
                bad(url, f'{norm[i][0]} and {norm[i + 1][0]} repeat the same text: "{p.heading_text[i][1].strip()[:60]}"')

        # images
        for src, alt, w, h in p.imgs:
            if alt is None or not alt.strip():
                bad(url, f'image with no alt text: {src}')
            if not w or not h:
                bad(url, f'image with no width/height (layout shift): {src}')

        # meta
        t = p.title.strip()
        if len(t) > 70:
            bad(url, f'title too long ({len(t)}): {t}')
        if not 50 <= len(p.desc) <= 170:
            bad(url, f'meta description is {len(p.desc)} chars, want 50 to 170')
        if not p.canonical and 'thank-you' not in url and '404' not in url:
            bad(url, 'no canonical')

    # wording that must never ship
    banned = {
        'samson': 'leftover from the generator this was adapted from',
        'Enter content here': 'web.com SiteBuilder placeholder',
        'Enter subhead': 'web.com SiteBuilder placeholder',
        'E.P.A required': 'the false 1967 EPA claim',
        'Intergrating': 'typo from the old site',
        'Handleing': 'typo from the old site',
        'Commericial': 'typo from the old site',
        'Agiculture': 'typo from the old site',
        'confidentially': 'should be confidentiality',
        'Penn State Department of Agriculture': 'not a real organisation',
        'BBB': 'there is no BBB profile for this business',
        '63rd Year': 'hard coded year count that goes stale',
    }
    for dirpath, _, files in os.walk(PUBLIC):
        for f in files:
            if not f.endswith('.html'):
                continue
            full = os.path.join(dirpath, f)
            text = open(full, encoding='utf-8').read()
            url = '/' + os.path.relpath(full, PUBLIC).replace('index.html', '')
            for word, why in banned.items():
                if re.search(re.escape(word), text, re.I):
                    bad(url, f'contains "{word}" ({why})')

    # things a human still has to resolve
    for dirpath, _, files in os.walk(PUBLIC):
        for f in files:
            if f.endswith('.html'):
                full = os.path.join(dirpath, f)
                url = '/' + os.path.relpath(full, PUBLIC).replace('index.html', '')
                n = open(full, encoding='utf-8').read().count('ASK NOLAN')
                if n:
                    notes.append(f'{url}: {n} "ASK NOLAN" placeholder(s) still visible on the page')

    # The serverless function is not HTML, so the scan above never saw it. It was
    # copied from the project this generator came from and defaulted to that
    # company's mailbox, which would have sent every enquiry to the wrong firm.
    api = os.path.join(os.path.dirname(PUBLIC), 'api')
    for d, _, fs in os.walk(api) if os.path.isdir(api) else []:
        for f in fs:
            if not f.endswith('.js'):
                continue
            text = open(os.path.join(d, f), encoding='utf-8').read()
            for word, why in banned.items():
                if re.search(re.escape(word), text, re.I):
                    bad(f'api/{f}', f'contains "{word}" ({why})')
            for route in re.findall(r"^\s*\w+: '(/[^'?#]*)", text, re.M):
                target = route_for(route)
                if target and not os.path.exists(target):
                    bad(f'api/{f}', f'redirects to {route}, which this build does not serve')

    if notes:
        print('TO RESOLVE BEFORE LAUNCH')
        for n in notes:
            print('  ' + n)
        print()

    if problems:
        print(f'{len(problems)} PROBLEMS')
        for p in problems:
            print('  ' + p)
        return 1

    print('NO PROBLEMS')
    return 0


if __name__ == '__main__':
    sys.exit(main())
