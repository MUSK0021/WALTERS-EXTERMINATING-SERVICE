"""Full page screenshots of the built site, for design review.

    python3 tools/shots.py                 # every page, desktop
    python3 tools/shots.py --mobile        # narrow, see the warning below
    python3 tools/shots.py --dark          # dark theme
    python3 tools/shots.py / /about/       # just these routes

Serves the build on a spare port and drives headless Chrome. Shots land in
_shots/ and are overwritten each run.

--mobile CAVEAT. Headless Chrome sizes the window but does not turn on device
emulation, so `width=device-width` does not take effect and the page lays out
wider than the window and is then clipped at the edge. The shots look like a
horizontal overflow bug that is not there. Use the real browser for phone QA
and treat --mobile as a rough guide to stacking order only.
"""
import http.server
import os
import subprocess
import sys
import threading
import functools

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(os.path.dirname(ROOT), 'public')
SHOTS = os.path.join(ROOT, '_shots')
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
PORT = 8899

PAGES = ['/', '/services/', '/what-it-costs/', '/pictures/', '/home-pest-control/',
         '/bed-bugs/', '/commercial-pest-control/', '/rodents-and-wildlife/',
         '/bees-wasps-hornets/', '/pests/', '/about/', '/service-area/', '/contact/',
         '/privacy/']


def serve():
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=PUBLIC)
    handler.log_message = lambda *a, **k: None
    httpd = http.server.ThreadingHTTPServer(('127.0.0.1', PORT), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def shot(route, width, height, out, dark=False):
    url = f'http://127.0.0.1:{PORT}{route}'
    if dark:
        # the theme is stored in localStorage, so ask for it in the query and let
        # the page's own head script pick it up
        url += ('&' if '?' in url else '?') + 'theme=dark'
    cmd = [
        CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
        '--force-device-scale-factor=1',
        f'--window-size={width},{height}',
        '--screenshot=' + out,
        '--virtual-time-budget=9000',
        '--default-background-color=ffffff',
    ]
    if dark:
        cmd.append('--force-dark-mode')
    cmd.append(url)
    subprocess.run(cmd, capture_output=True, timeout=90)
    return os.path.exists(out)


def main():
    args = [a for a in sys.argv[1:]]
    mobile = '--mobile' in args
    dark = '--dark' in args
    routes = [a for a in args if a.startswith('/')] or PAGES

    w, h = (390, 6000) if mobile else (1440, 5200)
    tag = ('m' if mobile else 'd') + ('-dark' if dark else '')
    if mobile:
        print('NOTE: headless Chrome does not emulate a device, so these will look')
        print('      clipped on the right. That is the tool, not the site. See the')
        print('      module docstring; check phones in a real browser.\n')

    os.makedirs(SHOTS, exist_ok=True)
    httpd = serve()
    try:
        for r in routes:
            name = (r.strip('/').replace('/', '-') or 'home') + f'.{tag}.png'
            out = os.path.join(SHOTS, name)
            ok = shot(r, w, h, out, dark)
            size = os.path.getsize(out) // 1024 if ok else 0
            print(f'{"ok " if ok else "FAIL"} {r:28s} -> _shots/{name} ({size} KB)')
    finally:
        httpd.shutdown()


if __name__ == '__main__':
    sys.exit(main())
