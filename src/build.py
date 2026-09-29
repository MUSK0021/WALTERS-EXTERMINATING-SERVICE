"""Build the Walters Exterminating Service website (static HTML) for Vercel.

    python3 src/build.py             -> ./public/, ./api/, ./vercel.json
    OUT=/some/dir python3 build.py

Every page shares one header, one footer and one stylesheet, so they always match.
No framework, no build step on Vercel, no JavaScript libraries.
"""
import base64
import datetime
import hashlib
import html
import json
import os
import shutil

from content import (AREAS, COUPON, PRICING, FOUNDED, FOUNDED_MONTH, HOME_FAQ, HOME_PESTS, HERO_SLIDES, HOW_IT_WORKS,
                     NAV, OPEN_QUESTIONS, PEST_BY_SLUG, PESTS, PHOTO_CAPTIONS, PROMISES, SERVICE_BY_SLUG,
                     SERVICES, SITE, STORY, TIMELINE)
from icons import icon
from pest_art import pest_art, service_art
from logo_paths import LETTERS as LOGO_LETTERS, MONO as LOGO_MONO, MONO_W, MONO_X0, OVAL_H as LOGO_H, OVAL_W as LOGO_W

ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(ROOT, 'static')
# src/ holds the generator; everything it produces lands in the repository root,
# which is what Vercel serves.
OUT = os.environ.get('OUT') or os.path.dirname(ROOT)
PUBLIC = os.path.join(OUT, 'public')
PHOTOS = json.load(open(os.path.join(ROOT, 'photos.json')))
TODAY = datetime.date.today()
YEAR = TODAY.year

e = html.escape

# Years the family has run the business, computed so it can never go stale.
# The April anniversary is what flips it over.
YEARS = YEAR - FOUNDED - (0 if TODAY.month >= 4 else 1)

# Runs before first paint: marks JS as on and applies a saved day/night choice with no flash.
HEAD_SCRIPT = ("(function(d){var h=d.documentElement;h.className='js';"
               "try{var t=localStorage.getItem('walters-theme');if(t==='light'||t==='dark')h.setAttribute('data-theme',t)}catch(x){}"
               "})(document);")
HEAD_SCRIPT_HASH = 'sha256-' + base64.b64encode(hashlib.sha256(HEAD_SCRIPT.encode()).digest()).decode()

ROUTES = []


# ================================================================= helpers

def ver(rel):
    with open(os.path.join(STATIC, rel.lstrip('/')), 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()[:10]


def asset(rel):
    return f'{rel}?v={ver(rel)}'


def img(name, alt, cls='', eager=False, sizes='100vw'):
    p = PHOTOS[name]
    load = 'eager" fetchpriority="high' if eager else 'lazy'
    c = f' class="{cls}"' if cls else ''
    srcset = (f'srcset="/assets/img/photos/{name}-sm.webp {p["sw"]}w, /assets/img/photos/{name}.webp {p["w"]}w" sizes="{sizes}" '
              if p.get('sw') else '')
    return (f'<img src="/assets/img/photos/{name}.webp" {srcset}'
            f'width="{p["w"]}" height="{p["h"]}" alt="{e(alt)}" loading="{load}" decoding="async"{c}>')


def figure(name, alt, caption='', cls=''):
    cap = f'<figcaption>{e(caption)}</figcaption>' if caption else ''
    return f'<figure class="shot {cls}">{img(name, alt)}{cap}</figure>'


def logo(cls=''):
    """Their real oval badge, as vector outlines.

    Traced from the mark on the van and the shirt (tools/mklogo.py). The oval
    is the brand green: sampling the badge in two separate photographs gives
    #3e514e and #3c4a48, both within a couple of points of #41504f. The two
    fills are CSS-driven so the badge can reverse on dark sections.
    """
    return (f'<span class="mark {cls}">'
            f'<svg class="mark__svg" viewBox="0 0 {LOGO_W} {LOGO_H}" role="img" '
            f'aria-label="{e(SITE["name"])}">'
            f'<ellipse class="mark__oval" cx="{LOGO_W / 2}" cy="{LOGO_H / 2}" '
            f'rx="{LOGO_W / 2}" ry="{LOGO_H / 2}"/>'
            f'<g class="mark__letters">{LOGO_LETTERS}</g>'
            f'</svg></span>')


def btn(label, href, kind='primary', size='', ico='arrow', attrs=''):
    cls = f'btn btn--{kind}' + (f' btn--{size}' if size else '')
    lead = trail = ''
    if ico == 'phone':
        lead = f'<span class="btn__lead">{icon("phone")}</span>'
    elif ico:
        trail = f'<span class="btn__icon">{icon(ico)}</span>'
    return f'<a class="{cls}" href="{href}"{attrs}>{lead}<span>{label}</span>{trail}</a>'


def call_btn(kind='primary', size='lg', label=None):
    return btn(label or f'Call {SITE["phone"]}', SITE['phone_href'], kind, size, ico='phone')


def quote_btn(kind='outline', size='lg', label='Get a free quote'):
    return btn(label, '/contact/#form', kind, size)


def eyebrow(text):
    return f'<p class="eyebrow">{e(text)}</p>'


def head_block(eb, title, lead='', cls=''):
    lead_html = f'<p class="lead" data-reveal style="--d:2">{lead}</p>' if lead else ''
    return (f'<div class="head {cls}">{eyebrow(eb) if eb else ""}'
            f'<h2 class="h2" data-reveal style="--d:1">{title}</h2>{lead_html}</div>')


def checks(items, cls='checks'):
    return f'<ul class="{cls}">' + ''.join(f'<li>{icon("check")}<span>{e(x)}</span></li>' for x in items) + '</ul>'


def faq_section(items, title='Questions people ask.', eb='Straight answers'):
    rows = ''.join(
        f'<details class="faq__item" data-reveal style="--d:{min(i, 4)}"><summary><span>{e(q)}</span>'
        f'<span class="faq__sign" aria-hidden="true">{icon("plus")}</span></summary>'
        f'<div class="faq__a"><p>{e(a)}</p></div></details>'
        for i, (q, a) in enumerate(items))
    return f'''<section class="section faq" id="faq">
  <div class="wrap faq__grid">
    <div class="faq__side">
      {eyebrow(eb)}
      <h2 class="h2" data-reveal style="--d:1">{title}</h2>
      <div class="faq__help" data-reveal style="--d:2">
        <span class="faq__help-icon">{icon("phone")}</span>
        <div><strong>Still not sure?</strong><p>Call and describe it in your own words.</p>
        {call_btn('primary', '')}</div>
      </div>
    </div>
    <div class="faq__list">{rows}</div>
  </div>
</section>'''


def crumbs(items):
    parts = []
    for i, (label, href) in enumerate(items):
        if i == len(items) - 1:
            parts.append(f'<li><span aria-current="page">{e(label)}</span></li>')
        else:
            parts.append(f'<li><a href="{href}">{e(label)}</a>{icon("chevron-right")}</li>')
    data = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': l, 'item': SITE['origin'] + h}
        for i, (l, h) in enumerate(items)]}
    return (f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(parts)}</ol></nav>'
            f'<script type="application/ld+json">{json.dumps(data)}</script>')


# ================================================================= layout

def head(title, desc, path, noindex=False, preload_img=None):
    full = f'{title} | {SITE["name"]}' if title else f'{SITE["name"]} | Pest Control in Northeast Philadelphia'
    canonical = SITE['origin'] + path
    robots = '<meta name="robots" content="noindex">\n' if noindex else ''
    # LocalBusiness only. Deliberately NO aggregateRating: marking up your own
    # ratings breaches Google's structured data policy. Deliberately NO street
    # address: the business does not publish one anywhere.
    business = {
        '@context': 'https://schema.org', '@type': 'PestControlService',
        '@id': SITE['origin'] + '/#business',
        'name': SITE['name'], 'legalName': SITE['legal'], 'url': SITE['origin'] + '/',
        'telephone': '+1-215-947-8818', 'email': SITE['email'],
        'foundingDate': str(FOUNDED), 'founder': {'@type': 'Person', 'name': SITE['founder']},
        'slogan': SITE['tagline'], 'priceRange': '$$',
        'address': {'@type': 'PostalAddress', 'addressRegion': 'PA', 'addressCountry': 'US'},
        'areaServed': [{'@type': 'AdministrativeArea', 'name': n} for n, _ in AREAS],
    }
    preload = ''
    if preload_img:
        p = PHOTOS[preload_img]
        responsive = (f'imagesrcset="/assets/img/photos/{preload_img}-sm.webp {p["sw"]}w, '
                      f'/assets/img/photos/{preload_img}.webp {p["w"]}w" imagesizes="100vw" ' if p.get('sw') else '')
        preload = f'<link rel="preload" as="image" href="/assets/img/photos/{preload_img}.webp" {responsive}fetchpriority="high">\n'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}">
{robots}<link rel="canonical" href="{canonical}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0f1413" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(SITE["name"])}">
<meta property="og:title" content="{e(full)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE["origin"]}/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
{preload}<link rel="stylesheet" href="{asset("/assets/css/site.css")}">
<script>{HEAD_SCRIPT}</script>
<script type="application/ld+json">{json.dumps(business)}</script>
</head>'''


def theme_toggle(cls=''):
    return (f'<button class="theme-toggle {cls}" type="button" data-theme-toggle '
            f'aria-label="Switch between day and night" title="Day / night">'
            f'<span class="theme-toggle__sun">{icon("sun")}</span>'
            f'<span class="theme-toggle__moon">{icon("moon")}</span></button>')


def header(active, over_hero):
    def li(label, href, cls_attr):
        return f'<li><a href="{href}"{cls_attr}>{e(label)}</a></li>'

    # Services opens a panel listing all five, because "Services" on its own
    # tells somebody with a wasp nest nothing. Hover opens it on a mouse, the
    # caret opens it on a keyboard or a touch screen.
    drop_items = ''.join(
        f'<li><a class="drop__link" href="/{s["slug"]}/"'
        f'{" aria-current=" + chr(34) + "page" + chr(34) if active == "/" + s["slug"] + "/" else ""}>'
        f'<span class="drop__art">{service_art(s["slug"])}</span>'
        f'<span class="drop__text"><strong>{e(s["name"])}</strong><small>{e(s["short"])}</small></span></a></li>'
        for s in SERVICES)
    drop = (f'<div class="drop" id="drop-services"><ul class="drop__grid">{drop_items}</ul>'
            f'<div class="drop__foot"><span>Not sure which one? '
            f'<a href="{SITE["phone_href"]}">Call {SITE["phone"]}</a> and describe it.</span>'
            f'<a class="drop__all" href="/services/">All services {icon("arrow")}</a></div></div>')

    parts = []
    for label, href in NAV:
        on = active == href or (href == '/services/' and active == '/services/')
        cur = ' class="is-active" aria-current="page"' if on else ''
        if href == '/services/':
            parts.append(
                f'<li class="has-drop" data-drop><a href="{href}"{cur}>{e(label)}</a>'
                f'<button class="nav__caret" type="button" aria-expanded="false" '
                f'aria-controls="drop-services" data-drop-toggle>'
                f'<span class="sr-only">Show all services</span>{icon("chevron")}</button>{drop}</li>')
        else:
            parts.append(li(label, href, cur))
    links = ''.join(parts)

    m_services = ''.join(
        f'<li><a class="menu__sub" href="/{s["slug"]}/">{service_art(s["slug"])}<span>{e(s["name"])}</span></a></li>'
        for s in SERVICES)
    mobile = ''
    for label, href in NAV:
        mobile += li(label, href, ' aria-current="page"' if active == href else '')
        if href == '/services/':
            mobile += f'<li><ul class="menu__subs">{m_services}</ul></li>'
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="hdr{' hdr--over' if over_hero else ''}" data-hdr>
  <div class="wrap hdr__in">
    <a class="hdr__brand" href="/" aria-label="{e(SITE["name"])}, home">{logo()}</a>
    <nav class="hdr__nav" aria-label="Main"><ul>{links}</ul></nav>
    <div class="hdr__end">
      {theme_toggle()}
      <a class="hdr__tel" href="{SITE["phone_href"]}">{icon("phone")}<span>{SITE["phone"]}</span></a>
      <button class="burger" type="button" data-menu-open aria-expanded="false" aria-controls="menu">
        <span class="burger__bars" aria-hidden="true"><i></i><i></i></span><span>Menu</span></button>
    </div>
  </div>
</header>
<div class="menu" id="menu" data-menu hidden>
  <div class="menu__panel" role="dialog" aria-modal="true" aria-label="Menu">
    <div class="menu__top">{logo()}
      <button class="menu__close" type="button" data-menu-close aria-label="Close menu">{icon("x")}</button></div>
    <nav aria-label="Mobile"><ul class="menu__list">{mobile}</ul></nav>
    <div class="menu__foot">
      {call_btn('primary', 'lg')}
      {quote_btn('outline', 'lg')}
      <p class="menu__note">{e(SITE["tagline"])}</p>
    </div>
  </div>
</div>'''


def footer():
    svc = ''.join(f'<li><a href="/{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)
    company = ''.join(f'<li><a href="{h}">{e(l)}</a></li>' for l, h in
                      [('Our Story', '/about/'), ('Pictures', '/pictures/'),
                       ('What It Costs', '/what-it-costs/'), ('Areas We Cover', '/service-area/'),
                       ('Common Pests', '/pests/'), ('Contact', '/contact/'), ('Privacy', '/privacy/')])
    areas = ' &middot; '.join(e(n) for n, _ in AREAS)
    return f'''<footer class="ftr">
  <div class="wrap">
    <div class="ftr__top">
      <div class="ftr__brand">
        {logo('mark--lg')}
        <p class="ftr__tag">{e(SITE["tagline"])}</p>
        <p class="ftr__blurb">Family owned and operated since {FOUNDED}. Two generations looking after
          homes and businesses across {e(SITE["areas"])}.</p>
        <p class="ftr__lic">Licensed by the Pennsylvania Department of Agriculture as a pesticide
          application business. Licence <strong>{SITE["licence"]}</strong>.</p>
      </div>
      <div class="ftr__cols">
        <div><h2 class="ftr__h">Services</h2><ul>{svc}</ul></div>
        <div><h2 class="ftr__h">Company</h2><ul>{company}</ul></div>
        <div class="ftr__contact">
          <h2 class="ftr__h">Get in touch</h2>
          <a class="ftr__tel" href="{SITE["phone_href"]}">{SITE["phone"]}</a>
          <a class="ftr__mail" href="mailto:{SITE["email"]}">{SITE["email"]}</a>
          <p class="ftr__hours">Weekdays and Saturdays, with a one hour arrival window.</p>
        </div>
      </div>
    </div>
    <div class="ftr__areas"><span>Areas we cover</span><p>{areas}</p></div>
    <div class="ftr__base">
      <p>&copy; {YEAR} {e(SITE["legal"])}. All rights reserved.</p>
      <p class="ftr__made">Don&rsquo;t be bugged. Bug us.</p>
    </div>
  </div>
</footer>'''


def scripts(hero=False):
    s = f'<script src="{asset("/assets/js/app.js")}" defer></script>'
    if hero:
        s += f'<script src="{asset("/assets/js/hero.js")}" defer></script>'
    return s


def page(path, title, desc, body, active='', page_cls='', hero=False, over_hero=False,
         noindex=False, priority=0.7, preload_img=None):
    if not noindex:
        ROUTES.append((path, priority))
    doc = (head(title, desc, path, noindex, preload_img) +
           f'<body class="{page_cls}">' + header(active, over_hero) +
           f'<main id="main">{body}</main>' + footer() + scripts(hero) + '</body></html>')
    out = os.path.join(PUBLIC, path.strip('/'), 'index.html') if path != '/' else os.path.join(PUBLIC, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        f.write(doc)


# ================================================================= blocks

def page_hero(eb, title, lead, crumb_items, actions='', banner=None, banner_alt=''):
    """The band at the top of an inner page.

    With a banner it is a photograph behind white type, the way the home hero
    works, so the inner pages do not read as a plain document after it. Without
    one it falls back to the tinted panel with the badge watermarked into it.
    """
    if banner:
        media = (f'<div class="phero__media">{img(banner, banner_alt, eager=True, sizes="100vw")}'
                 f'<span class="phero__scrim"></span></div>')
        return f'''<section class="phero phero--photo">
  {media}
  <div class="wrap">''' + f'''
    {crumbs(crumb_items)}
    {eyebrow(eb)}
    <h1 class="h1" data-reveal style="--d:1">{title}</h1>
    <p class="phero__lead" data-reveal style="--d:2">{lead}</p>
    {f'<div class="actions" data-reveal style="--d:3">{actions}</div>' if actions else ''}
  </div>
</section>'''
    mark = (f'<svg class="phero__mark" viewBox="0 0 {LOGO_W} {LOGO_H}" aria-hidden="true" focusable="false">'
            f'<ellipse cx="{LOGO_W / 2}" cy="{LOGO_H / 2}" rx="{LOGO_W / 2}" ry="{LOGO_H / 2}"/></svg>')
    return f'''<section class="phero">
  {mark}
  <div class="wrap">
    {crumbs(crumb_items)}
    {eyebrow(eb)}
    <h1 class="h1" data-reveal style="--d:1">{title}</h1>
    <p class="phero__lead" data-reveal style="--d:2">{lead}</p>
    {f'<div class="actions" data-reveal style="--d:3">{actions}</div>' if actions else ''}
  </div>
</section>'''


def promises_strip():
    items = ''.join(
        f'<li data-reveal style="--d:{i}"><span class="promise__ico">{icon(ic)}</span>'
        f'<div><strong>{e(t)}</strong><p>{e(d)}</p></div></li>'
        for i, (ic, t, d) in enumerate(PROMISES))
    return f'<section class="section promises"><div class="wrap"><ul class="promises__grid">{items}</ul></div></section>'


def how_it_works(eb='How it goes', title='Three steps, no mystery.'):
    steps = ''.join(
        f'<li data-reveal style="--d:{i}"><span class="step__n">{i + 1}</span>'
        f'<span class="step__ico">{icon(ic)}</span><h3>{e(t)}</h3><p>{e(d)}</p></li>'
        for i, (ic, t, d) in enumerate(HOW_IT_WORKS))
    return f'''<section class="section steps">
  <div class="wrap">{head_block(eb, title)}<ol class="steps__grid">{steps}</ol></div>
</section>'''


def coupon_band():
    return f'''<section class="section band">
  <div class="wrap band__in">
    <div class="band__text">
      <p class="eyebrow eyebrow--inv">New customers</p>
      <h2 class="h2">{e(COUPON["headline"])}</h2>
      <p>{e(COUPON["terms"])}</p>
    </div>
    <div class="band__act">{call_btn('white', 'lg')}{quote_btn('ghost', 'lg')}</div>
  </div>
</section>'''


def cta_band(title=None, text=None):
    title = title or 'Got something crawling where it should not be?'
    text = text or ('Call and tell us what you are seeing. You will get a person who has done this for a long time, '
                    'not a call centre and not a sales script.')
    return f'''<section class="section cta">
  <div class="wrap cta__in">
    <div>
      <p class="eyebrow eyebrow--inv">{e(SITE["tagline"])}</p>
      <h2 class="h2" data-reveal style="--d:1">{e(title)}</h2>
      <p class="cta__lead" data-reveal style="--d:2">{e(text)}</p>
    </div>
    <div class="cta__act" data-reveal style="--d:3">{call_btn('white', 'lg')}{quote_btn('ghost', 'lg')}</div>
  </div>
</section>'''


def service_card(s, i, level=3):
    return f'''<a class="scard" href="/{s["slug"]}/" data-reveal style="--d:{i}">
  <span class="scard__art">{service_art(s["slug"])}</span>
  <h{level}>{e(s["name"])}</h{level}>
  <p>{e(s["short"])}</p>
  <span class="scard__go">{icon("arrow")}</span>
</a>'''


def not_sure_card(i):
    """Sixth card in the services grid. Fills the orphan cell and answers the
    question most callers actually have, which is what the thing even is."""
    return f"""<a class="scard scard--alt" href="/pests/" data-reveal style="--d:{i}">
  <span class="scard__art">{service_art("__none__")}</span>
  <h3>Not sure what it is?</h3>
  <p>Look through the ones we get called about most, and what usually gives them away.</p>
  <span class="scard__go">{icon("arrow")}</span>
</a>"""


def pest_tile(slug, i):
    p = PEST_BY_SLUG[slug]
    return f'''<a class="ptile" href="/pests/#{p["slug"]}" data-reveal style="--d:{min(i, 5)}">
  <span class="ptile__art">{pest_art(p["slug"])}</span>
  <span class="ptile__name">{e(p["name"])}</span>
  <span class="ptile__when">{e(p["when"])}</span>
</a>'''


# ================================================================= pages

def home():
    slides = ''.join(
        img(n, a, cls='hero__img' + (' is-active' if i == 0 else ''), eager=(i == 0),
            sizes='100vw')
        for i, (n, a) in enumerate(HERO_SLIDES))
    dots = ''.join(f'<button class="hero__tab{" is-active" if i == 0 else ""}" type="button" '
                   f'data-go="{i}" aria-label="Show photo {i + 1}"'
                   f'{" aria-current=" + chr(34) + "true" + chr(34) if i == 0 else ""}>'
                   f'<span class="hero__tab-bar"><i></i></span></button>'
                   for i in range(len(HERO_SLIDES)))
    cards = ''.join(service_card(s, i) for i, s in enumerate(SERVICES)) + not_sure_card(len(SERVICES))
    tiles = ''.join(pest_tile(s, i) for i, s in enumerate(HOME_PESTS))
    page('/', '', (
        f'Family owned pest control in Northeast Philadelphia since {FOUNDED}. Bed bugs, roaches, mice, '
        f'wasps and wildlife. No contracts, no sales people. Call {SITE["phone"]}.'
    ), f'''
<section class="hero" data-hero>
  <div class="hero__media">{slides}<canvas class="hero__gl" aria-hidden="true"></canvas><div class="hero__scrim"></div></div>
  <div class="wrap hero__in">
    <p class="hero__badge" style="--i:0">Family owned since {FOUNDED} &middot; Licence {SITE["licence"]}</p>
    <h1 class="hero__title"><span><i style="--i:0">Two generations of</i></span><span><i style="--i:1"><em>getting rid of them.</em></i></span></h1>
    <p class="hero__lead" style="--i:1">Pest control for homes and businesses across {e(SITE["areas"])}.
      Bed bugs, roaches, mice, wasps, and whatever is in the attic.</p>
    <div class="hero__act" style="--i:2">{call_btn('white', 'lg')}{quote_btn('ghost', 'lg')}</div>
    <ul class="hero__trust" style="--i:3">
      <li>{icon("check")}<span>No contracts</span></li>
      <li>{icon("check")}<span>No sales people</span></li>
      <li>{icon("check")}<span>Weekdays and Saturdays</span></li>
    </ul>
  </div>
  <div class="hero__dots">{dots}</div>
  <button class="hero__pause" type="button" data-hero-pause aria-label="Pause the slideshow">{icon("pause")}</button>
</section>

{promises_strip()}

<section class="section services-home">
  <div class="wrap">
    {head_block('What we do', 'Whatever it is, we have seen it before.',
                'Sixty years in the same corner of Pennsylvania means very little surprises us.')}
    <div class="scards">{cards}</div>
  </div>
</section>

<section class="section story-home">
  <div class="wrap story-home__grid">
    <div class="story-home__media">
      {figure('archive-1977', 'A young Nolan Walters wearing a Walters Exterminating company shirt in the 1970s', 'In a company shirt, 1970s', 'shot--tilt')}
      {figure('archive-harvey', 'Two men standing beside a white Walters Exterminating van', 'Harvey and Nolan Walters, 2010')}
    </div>
    <div class="story-home__text">
      {eyebrow('Since ' + str(FOUNDED))}
      <h2 class="h2" data-reveal style="--d:1">Started by Harvey.<br>Run by his son.</h2>
      <p class="lead" data-reveal style="--d:2">{e(STORY["lead"])}</p>
      <blockquote class="pull" data-reveal style="--d:3">
        <p>{e(STORY["quote"])}</p>
        <cite>{e(STORY["quote_by"])}<span>{e(STORY["quote_note"])}</span></cite>
      </blockquote>
      <div data-reveal style="--d:4">{btn('Read the whole story', '/about/', 'outline', '')}</div>
    </div>
  </div>
</section>

{how_it_works()}

<section class="section pests-home">
  <div class="wrap">
    {head_block('Common round here', 'Know what you are looking at.',
                'The ones we get called about most, and what usually gives them away.')}
    <div class="ptiles">{tiles}</div>
    <p class="center" data-reveal>{btn('See all common pests', '/pests/', 'outline', '')}</p>
  </div>
</section>

{coupon_band()}

{faq_section(HOME_FAQ)}

{cta_band()}
''', active='/', page_cls='p-home', hero=True, over_hero=True, priority=1.0, preload_img=HERO_SLIDES[0][0])


def services_index():
    cards = ''.join(service_card(s, i, level=2) for i, s in enumerate(SERVICES)) + not_sure_card(len(SERVICES))
    page('/services/', 'Services',
         'Home and commercial pest control, bed bug treatment, rodents and wildlife, wasps and hornets. '
         'Northeast Philadelphia and nearby Montgomery and Bucks.',
         f'''{page_hero('Services', 'What we take care of.',
                        'Five things we do, done by people who have been doing them a long time. '
                        'If you are not sure which one you need, call and describe it.',
                        [('Home', '/'), ('Services', '/services/')],
                        call_btn('white', 'lg') + quote_btn('ghost', 'lg'),
                        banner='banner-services',
                        banner_alt='A pest control crew working outside a building')}
<section class="section"><div class="wrap"><div class="scards">{cards}</div></div></section>
{how_it_works()}
{coupon_band()}
{cta_band()}''', active='/services/', priority=0.9)


def service_page(s):
    related = [x for x in SERVICES if x['slug'] != s['slug']][:3]
    rel = ''.join(service_card(x, i) for i, x in enumerate(related))
    pests = ''.join(pest_tile(p, i) for i, p in enumerate(s.get('pests', [])))

    blocks = [f'''<section class="section svc-intro">
  <div class="wrap svc-intro__grid">
    <div class="svc-intro__text">
      {eyebrow(s["included_title"])}
      <h2 class="h2" data-reveal style="--d:1">{e(s["intro_title"])}</h2>
      <p class="lead" data-reveal style="--d:2">{e(s["lead"])}</p>
      {checks(s["included"])}
    </div>
    <div class="svc-intro__media">{figure(s["image"], s["image_alt"])}</div>
  </div>
</section>''']

    if s.get('facts'):
        cells = ''.join(
            f'<li data-reveal style="--d:{i}"><span class="fact__ico">{icon(ic)}</span>'
            f'<h3>{e(t)}</h3><p>{e(d)}</p></li>' for i, (ic, t, d) in enumerate(s['facts']))
        blocks.append(f'''<section class="section facts">
  <div class="wrap">{head_block('Worth knowing', e(s["facts_title"]))}
  <ul class="facts__grid">{cells}</ul></div></section>''')

    if s.get('signs'):
        blocks.append(f'''<section class="section signs">
  <div class="wrap signs__grid">
    <div>{eyebrow('Early signs')}<h2 class="h2" data-reveal style="--d:1">{e(s["signs_title"])}</h2>
      <p class="lead" data-reveal style="--d:2">Spotting it early makes the job smaller and cheaper.
        If any of this sounds familiar, call us.</p>
      <div data-reveal style="--d:3">{call_btn('primary', '')}</div></div>
    <div>{checks(s["signs"], 'checks checks--lg')}</div>
  </div></section>''')

    if s.get('properties'):
        chips = ''.join(f'<li>{e(x)}</li>' for x in s['properties'])
        blocks.append(f'''<section class="section props"><div class="wrap">
  {head_block('Where we work', e(s["properties_title"]))}
  <ul class="chips">{chips}</ul></div></section>''')

    if s.get('approach'):
        blocks.append(f'''<section class="section approach"><div class="wrap approach__in">
  {eyebrow('How we work')}
  <h2 class="h2" data-reveal style="--d:1">{e(s["approach_title"])}</h2>
  <p class="lead" data-reveal style="--d:2">{e(s["approach"])}</p></div></section>''')

    if pests:
        blocks.append(f'''<section class="section"><div class="wrap">
  {head_block('Covered here', 'Pests this service deals with')}
  <div class="ptiles">{pests}</div></div></section>''')

    blocks.append(faq_section(s['faqs'], f'{e(s["name"])}, explained.'))
    blocks.append(f'''<section class="section"><div class="wrap">
  {head_block('Also from us', 'Where to go next')}<div class="scards">{rel}</div></div></section>''')
    blocks.append(cta_band())

    page(f'/{s["slug"]}/', s['name'], s['meta'],
         page_hero(s['name'], e(s['title']), e(s['short']),
                   [('Home', '/'), ('Services', '/services/'), (s['name'], f'/{s["slug"]}/')],
                   call_btn('white', 'lg') + quote_btn('ghost', 'lg'),
                   banner=s['banner'], banner_alt=s['banner_alt']) + ''.join(blocks),
         active='/services/', over_hero=True, priority=0.9)


def pests_page():
    rows = ''.join(f'''<article class="prow" id="{p["slug"]}" data-reveal style="--d:{min(i % 4, 3)}">
  <div class="prow__head"><span class="prow__art">{pest_art(p["slug"])}</span>
    <div><h2>{e(p["name"])}</h2><p class="prow__when">{e(p["when"])}</p></div></div>
  <p class="prow__sum">{e(p["summary"])}</p>
  <ul class="prow__signs">{''.join(f'<li>{icon("check")}<span>{e(x)}</span></li>' for x in p["signs"])}</ul>
  <a class="prow__link" href="/{p["service"]}/">{e(SERVICE_BY_SLUG[p["service"]]["name"])}{icon("arrow")}</a>
</article>''' for i, p in enumerate(PESTS))
    page('/pests/', 'Common Pests',
         'What we get called about most: bed bugs, roaches, mice, rats, wasps, hornets, ants and wildlife, '
         'with the signs that give each one away.',
         f'''{page_hero('Common pests', 'Know what you are looking at.',
                        'The pests we get called about most around here, what season they turn up, and the signs '
                        'people usually notice first.',
                        [('Home', '/'), ('Common Pests', '/pests/')],
                        call_btn('white', 'lg'),
                        banner='banner-pests', banner_alt='A cockroach photographed close up')}
<section class="section"><div class="wrap"><div class="prows">{rows}</div></div></section>
{cta_band('Not sure what you have got?', 'Describe it over the phone. Nine times out of ten we know what it is '
          'before we get there, and if we do not, we come and look.')}''',
         active='/pests/', over_hero=True, priority=0.8)


def about():
    paras = ''.join(f'<p data-reveal style="--d:{min(i + 1, 4)}">{e(x)}</p>'
                    for i, x in enumerate(STORY['paragraphs']))
    line = ''.join(f'''<li data-reveal style="--d:{min(i, 4)}">
  <span class="tl__year">{e(y)}</span><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>'''
                   for i, (y, t, d) in enumerate(TIMELINE))
    gallery = ''.join(figure(n, c, c) for n, c, _ in PHOTO_CAPTIONS[:3])
    page('/about/', 'Our Story',
         f'Harvey Walters started the company in {FOUNDED}. His son Nolan, the Bug-Man, runs it now. '
         f'Family owned pest control in Northeast Philadelphia.',
         f'''{page_hero('Our story', f'Same family since {FOUNDED}.',
                        e(STORY['lead']), [('Home', '/'), ('Our Story', '/about/')],
                        banner='banner-about', banner_alt='A terrace of red brick houses with white doors')}
<section class="section about-body">
  <div class="wrap about-body__grid">
    <div class="about-body__text">{paras}
      <blockquote class="pull pull--lg" data-reveal style="--d:5">
        <p>{e(STORY["quote"])}</p>
        <cite>{e(STORY["quote_by"])}<span>{e(STORY["quote_note"])}</span></cite>
      </blockquote>
    </div>
    <aside class="about-body__side">
      {figure('nolan-van', 'Nolan Walters standing beside the Walters Exterminating van', 'Nolan Walters')}
      <div class="lic-card">
        <span class="lic-card__ico">{icon("badge")}</span>
        <h2>Pennsylvania licence {SITE["licence"]}</h2>
        <p>We are licensed by the Pennsylvania Department of Agriculture as a pesticide application business.
          State law says that number goes on both sides of the van, so you can check it on the truck outside
          your house.</p>
      </div>
    </aside>
  </div>
</section>

<section class="section tl"><div class="wrap">
  {head_block('The short version', 'How we got here')}<ol class="tl__list">{line}</ol></div></section>

<section class="section gallery"><div class="wrap">
  {head_block('From the album', 'Sixty years of turning up')}
  <div class="gallery__grid">{gallery}</div>
  <p class="gallery__note">Photographs from the Walters family.
    <a href="/pictures/">See all of them {icon("arrow")}</a></p>
</div></section>

<section class="section motto"><div class="wrap motto__in">
  <p class="motto__q">&ldquo;{e(STORY["motto"])}&rdquo;</p>
  <p class="motto__by">{e(STORY["motto_by"])}</p>
</div></section>

{cta_band()}''', active='/about/', over_hero=True, priority=0.8)


def service_area():
    cols = ''.join(f'''<div class="area" data-reveal style="--d:{i}">
  <h2>{e(name)}</h2>
  <ul>{''.join(f'<li>{icon("pin")}<span>{e(p)}</span></li>' for p in places)}</ul>
</div>''' for i, (name, places) in enumerate(AREAS))
    page('/service-area/', 'Areas We Cover',
         'Towns we cover across Northeast Philadelphia, eastern Montgomery County and lower Bucks County, '
         'from Somerton and Bustleton to Abington and Bensalem.',
         f'''{page_hero('Where we go', 'Our corner of Pennsylvania.',
                        'We have worked these same streets for sixty years. If your town is not on the list and '
                        'you are nearby, call and ask.',
                        [('Home', '/'), ('Areas We Cover', '/service-area/')],
                        call_btn('white', 'lg'),
                        banner='banner-area',
                        banner_alt='A residential street of houses with front lawns')}
<section class="section"><div class="wrap"><div class="areas">{cols}</div></div></section>
{cta_band('Not sure if we come to you?', 'Give us a call. If we do not cover your street we will usually know '
          'someone who does.')}''', active='', over_hero=True, priority=0.8)


def pricing_page():
    """What it costs, without a price list.

    Samson's equivalent page is a set of priced tiers. Walters publishes no
    prices and quotes on the doorstep, so inventing tiers would be inventing a
    service he does not sell. This answers the same question, which is "how do
    I know what I am in for", using only his own process and his own coupon.
    """
    steps = ''.join(
        f'<li data-reveal style="--d:{i}"><span class="how__n">{i + 1}</span>'
        f'<span class="how__ico">{icon(ic)}</span>'
        f'<h2>{e(t)}</h2><p>{e(d)}</p></li>'
        for i, (ic, t, d) in enumerate(PRICING['steps']))
    factors = checks(PRICING['factors'])
    page('/what-it-costs/', 'What It Costs',
         'No price list, because no two jobs match. Here is exactly how we arrive at the '
         'number, and you hear it before any work starts.',
         f"""{page_hero('What it costs', 'No surprises on the invoice.',
                        e(PRICING['lead']),
                        [('Home', '/'), ('What It Costs', '/what-it-costs/')],
                        call_btn('white', 'lg') + quote_btn('ghost', 'lg'),
                        banner='banner-costs',
                        banner_alt='A brick house with a columned front porch')}
<section class="section"><div class="wrap">
  {head_block('How the price is set', 'Four steps, and you can stop at any of them.')}
  <ol class="how">{steps}</ol>
</div></section>
<section class="section section--tint"><div class="wrap price-grid">
  <div>
    {head_block('', e(PRICING['factors_title']))}
    {factors}
  </div>
  <aside class="lic-card price-card" data-reveal style="--d:2">
    <span class="lic-card__ico">{icon('badge')}</span>
    <h2>{e(COUPON['headline'])}</h2>
    <p>{e(COUPON['terms'])}</p>
    <div class="actions">{call_btn('white', 'md')}</div>
  </aside>
</div></section>
{faq_section(PRICING['faq'], 'Questions about the money.', 'Straight answers')}
{cta_band()}""", active='/what-it-costs/', over_hero=True, priority=0.8)


def gallery_page():
    """The Pictures page from their old site, rebuilt.

    Everything else on this site is either their own working photographs or
    licensed stock. This page is the family's own and nothing else, which is
    why the captions say what is in each one rather than selling anything.
    """
    shots = ''.join(
        f'<figure class="gal__item" data-reveal style="--d:{min(i % 3, 2)}">'
        f'{img(n, cap, sizes="(min-width: 900px) 33vw, 100vw")}'
        f'<figcaption><strong>{e(cap)}</strong><span>{e(note)}</span></figcaption></figure>'
        for i, (n, cap, note) in enumerate(PHOTO_CAPTIONS))
    page('/pictures/', 'Pictures',
         'Photographs from sixty years of the family business: the vans, the crew, '
         'and Harvey and Nolan in the years between.',
         f"""{page_hero('Pictures', 'Sixty years, a few photographs.',
                        'Their own pictures, not stock. Some of them are scans of prints that have '
                        'been in a drawer for forty years, so forgive the grain.',
                        [('Home', '/'), ('Our Story', '/about/'), ('Pictures', '/pictures/')],
                        call_btn('white', 'lg'),
                        banner='banner-pictures',
                        banner_alt='A row of houses with slate roofs on a quiet street')}
<section class="section"><div class="wrap">
  <div class="gal">{shots}</div>
</div></section>
{cta_band()}""", active='/about/', over_hero=True, priority=0.6)


def gallery_page_end():
    pass


def contact_form():
    opts = ''.join(f'<option value="{e(s["name"])}">{e(s["name"])}</option>' for s in SERVICES)
    return f'''<form class="form" id="form" method="post" action="/api/contact" novalidate data-form>
  <input type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" class="hp">
  <div class="form__row">
    <label for="name">Your name <span aria-hidden="true">*</span></label>
    <input id="name" name="name" type="text" required autocomplete="name">
  </div>
  <div class="form__two">
    <div class="form__row">
      <label for="phone">Phone <span aria-hidden="true">*</span></label>
      <input id="phone" name="phone" type="tel" required autocomplete="tel">
    </div>
    <div class="form__row">
      <label for="email">Email</label>
      <input id="email" name="email" type="email" autocomplete="email">
    </div>
  </div>
  <div class="form__two">
    <div class="form__row">
      <label for="town">Your town</label>
      <input id="town" name="town" type="text" autocomplete="address-level2">
    </div>
    <div class="form__row">
      <label for="service">What is it about?</label>
      <select id="service" name="service"><option value="">Not sure yet</option>{opts}</select>
    </div>
  </div>
  <div class="form__row">
    <label for="message">What are you seeing? <span aria-hidden="true">*</span></label>
    <textarea id="message" name="message" rows="5" required
      placeholder="Where you are seeing them, how long it has been going on, anything else worth knowing."></textarea>
  </div>
  <button class="btn btn--primary btn--lg form__send" type="submit">
    <span>Send it over</span><span class="btn__icon">{icon("arrow")}</span></button>
  <p class="form__note">We will get back to you. No sales people, no mailing list.</p>
</form>'''


def contact():
    page('/contact/', 'Contact',
         f'Call {SITE["phone"]} or send a message. Family owned pest control for Northeast Philadelphia, '
         f'eastern Montgomery County and lower Bucks County.',
         f'''{page_hero('Contact', 'Tell us what you are seeing.',
                        'Call and you will get a person. Or send this over and we will come back to you.',
                        [('Home', '/'), ('Contact', '/contact/')],
                        banner='banner-contact',
                        banner_alt='The front entrance and porch steps of a house')}
<section class="section contact"><div class="wrap contact__grid">
  <div class="contact__side">
    <a class="contact__big" href="{SITE["phone_href"]}">
      <span class="contact__big-ico">{icon("phone")}</span>
      <span><small>Call us</small><strong>{SITE["phone"]}</strong></span></a>
    <a class="contact__big contact__big--alt" href="mailto:{SITE["email"]}">
      <span class="contact__big-ico">{icon("mail")}</span>
      <span><small>Email us</small><strong>{SITE["email"]}</strong></span></a>
    <div class="contact__card">
      <h2>When we work</h2>
      <p>Weekdays and Saturdays, with a one hour arrival window so you are not stuck waiting in all day.</p>
    </div>
    <div class="contact__card">
      <h2>Where we go</h2>
      <p>{e(SITE["areas"][0].upper() + SITE["areas"][1:])}.</p>
      <p><a href="/service-area/">See the full list of towns{icon("arrow")}</a></p>
    </div>
    <div class="contact__card contact__card--lic">
      <h2>Licensed in Pennsylvania</h2>
      <p>PA Department of Agriculture pesticide application business licence <strong>{SITE["licence"]}</strong>.</p>
    </div>
  </div>
  <div class="contact__main">
    <h2 class="h2">Send us a message</h2>
    {contact_form()}
  </div>
</div></section>
{coupon_band()}''', active='/contact/', over_hero=True, priority=0.9)


def thank_you():
    page('/thank-you/', 'Thank you',
         'Your message reached Walters Exterminating Service.',
         f'''<section class="section status"><div class="wrap status__in">
  <span class="status__ico">{icon("check")}</span>
  <h1 class="h1">Got it, thank you.</h1>
  <p class="lead">Your message is with us and we will come back to you shortly.
    If it is urgent, ring <span class="nowrap">{SITE["phone"]}</span> and you will get a person.</p>
  <div class="actions">{call_btn('primary', 'lg')}{btn('Back to the home page', '/', 'outline', 'lg')}</div>
</div></section>''', noindex=True)


def form_problem_pages():
    """The two ways a form post can fail.

    There is no JavaScript on the form, so the POST to /api/contact is a plain
    browser submit and the redirect is the only way back. Both outcomes need a
    real page, and both need the phone number on them, because someone who has
    just failed to send a message should not have to go hunting for it.
    """
    page('/contact/error/', 'Check the form',
         'Something in the form needs another look before we can send it.',
         f"""<section class="section status"><div class="wrap status__in">
  <span class="status__ico status__ico--warn">{icon("alert")}</span>
  <h1 class="h1">Something was missing.</h1>
  <p class="lead">We need a name, a phone number and a line about what you are seeing.
    Go back and fill in whatever is blank, or skip it and ring <span class="nowrap">{SITE["phone"]}</span>.</p>
  <div class="actions">{btn('Back to the form', '/contact/#form', 'primary', 'lg')}{call_btn('outline', 'lg')}</div>
</div></section>""", noindex=True)

    page('/contact/unavailable/', 'Message not sent',
         'The message did not send. Call us and we will pick it up from there.',
         f"""<section class="section status"><div class="wrap status__in">
  <span class="status__ico status__ico--warn">{icon("alert")}</span>
  <h1 class="h1">That did not send.</h1>
  <p class="lead">Our end had a problem, not you. Nothing was lost on your side, so try again in a
    minute, or ring <span class="nowrap">{SITE["phone"]}</span> and you will get a person.</p>
  <div class="actions">{call_btn('primary', 'lg')}{btn('Try the form again', '/contact/#form', 'outline', 'lg')}</div>
</div></section>""", noindex=True)


def privacy():
    page('/privacy/', 'Privacy',
         'How Walters Exterminating Service handles the information you send through this website.',
         f'''{page_hero('Privacy', 'What we do with your details.',
                        'Short version: we use them to get back to you about pest control, and nothing else.',
                        [('Home', '/'), ('Privacy', '/privacy/')])}
<section class="section prose"><div class="wrap prose__in">
  <h2>What we collect</h2>
  <p>If you fill in the form on this site we receive your name, phone number, and whatever else you choose to
    put in it, such as your email address, your town and a description of the problem. If you call or email us
    we have whatever you tell us then.</p>
  <h2>What we do with it</h2>
  <p>We use it to answer you and to carry out the work if you decide to go ahead. That is all. We do not sell it,
    rent it, or pass it to anyone else for marketing, and no sales company gets your number from us.</p>
  <h2>How long we keep it</h2>
  <p>We keep customer records for as long as we need them to look after the property and to meet our obligations
    as a licensed pesticide application business in Pennsylvania.</p>
  <h2>Cookies and tracking</h2>
  <p>This site sets no advertising or tracking cookies. If you use the day and night switch, your choice is saved
    in your own browser so the site remembers it next time. That stays on your device and never reaches us.</p>
  <h2>Our web host</h2>
  <p>Like any website, our host keeps standard server logs, which include things like IP addresses and the pages
    requested. These are used to keep the site running and secure.</p>
  <h2>Asking us about your details</h2>
  <p>If you want to know what we hold about you, or want it removed, call {SITE["phone"]} or email
    <a href="mailto:{SITE["email"]}">{SITE["email"]}</a> and we will sort it out.</p>
</div></section>''', priority=0.3)


def not_found():
    body = f'''<section class="section status"><div class="wrap status__in">
  <span class="status__ico status__ico--warn">{icon("alert")}</span>
  <h1 class="h1">That page is not here.</h1>
  <p class="lead">It may have moved, or the link may be old. Try one of these, or just give us a ring.</p>
  <div class="actions">{btn('Home page', '/', 'primary', 'lg')}{btn('Services', '/services/', 'outline', 'lg')}
    {call_btn('ghost', 'lg')}</div>
</div></section>'''
    doc = (head('Page not found', 'That page could not be found on the Walters Exterminating website.',
                '/404.html', noindex=True) + '<body>' + header('', False) +
           f'<main id="main">{body}</main>' + footer() + scripts() + '</body></html>')
    with open(os.path.join(PUBLIC, '404.html'), 'w') as f:
        f.write(doc)


# ================================================================= extras

def write_meta_files():
    urls = ''.join(
        f'<url><loc>{SITE["origin"]}{p}</loc><lastmod>{TODAY.isoformat()}</lastmod>'
        f'<priority>{pr}</priority></url>' for p, pr in ROUTES)
    with open(os.path.join(PUBLIC, 'sitemap.xml'), 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    with open(os.path.join(PUBLIC, 'robots.txt'), 'w') as f:
        f.write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE["origin"]}/sitemap.xml\n')
    with open(os.path.join(PUBLIC, 'site.webmanifest'), 'w') as f:
        json.dump({'name': SITE['name'], 'short_name': 'Walters', 'start_url': '/',
                   'display': 'standalone', 'background_color': '#ffffff', 'theme_color': '#41504f',
                   'icons': [{'src': '/apple-touch-icon.png', 'sizes': '180x180', 'type': 'image/png'}]}, f)


def vercel_json():
    csp = ("default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; "
           f"script-src 'self' '{HEAD_SCRIPT_HASH}'; font-src 'self'; form-action 'self'; "
           "base-uri 'self'; frame-ancestors 'none'; object-src 'none'")
    cfg = {
        # Everything Vercel needs is here, so importing the repo needs no
        # settings in the dashboard: no framework, no build, serve ./public,
        # and pick up the function in ./api.
        'outputDirectory': 'public',
        'cleanUrls': True,
        'trailingSlash': True,
        'headers': [
            {'source': '/(.*)', 'headers': [
                {'key': 'X-Content-Type-Options', 'value': 'nosniff'},
                {'key': 'Referrer-Policy', 'value': 'strict-origin-when-cross-origin'},
                {'key': 'X-Frame-Options', 'value': 'DENY'},
                {'key': 'Strict-Transport-Security', 'value': 'max-age=63072000; includeSubDomains; preload'},
                {'key': 'Content-Security-Policy', 'value': csp},
            ]},
            {'source': '/assets/(.*)', 'headers': [
                {'key': 'Cache-Control', 'value': 'public, max-age=31536000, immutable'}]},
        ],
        # The old web.com site used meaningless auto-generated ids. Keep any
        # existing links and rankings alive.
        'redirects': [
            {'source': '/index.html', 'destination': '/', 'permanent': True},
            {'source': '/id1.html', 'destination': '/about/', 'permanent': True},
            {'source': '/id2.html', 'destination': '/services/', 'permanent': True},
            {'source': '/id72.html', 'destination': '/bed-bugs/', 'permanent': True},
            # id21 was Specials/Coupons: the coupon now lives on the costs page
            {'source': '/id21.html', 'destination': '/what-it-costs/', 'permanent': True},
            {'source': '/id17.html', 'destination': '/contact/', 'permanent': True},
            {'source': '/id4.html', 'destination': '/contact/', 'permanent': True},
            # id70 was Pictures, which now has a page of its own again
            {'source': '/id70.html', 'destination': '/pictures/', 'permanent': True},
        ],
    }
    with open(os.path.join(OUT, 'vercel.json'), 'w') as f:
        json.dump(cfg, f, indent=2)


def copy_static():
    for name in os.listdir(STATIC):
        src, dst = os.path.join(STATIC, name), os.path.join(PUBLIC, name)
        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)
    api_src = os.path.join(ROOT, 'api')
    if os.path.isdir(api_src):
        shutil.copytree(api_src, os.path.join(OUT, 'api'), dirs_exist_ok=True)


def build():
    # Only the generated directories are cleared. OUT is the repository root,
    # which also holds .git, the README and the generator itself.
    for d in (PUBLIC, os.path.join(OUT, 'api')):
        if os.path.isdir(d):
            shutil.rmtree(d)
    os.makedirs(PUBLIC, exist_ok=True)
    copy_static()
    home()
    services_index()
    for s in SERVICES:
        service_page(s)
    pests_page()
    about()
    service_area()
    contact()
    pricing_page()
    gallery_page()
    thank_you()
    form_problem_pages()
    privacy()
    not_found()
    write_meta_files()
    vercel_json()
    n = sum(len(files) for d in (PUBLIC, os.path.join(OUT, 'api'))
            for _, _, files in os.walk(d))
    print(f'built {len(ROUTES)} pages, {n} files -> {OUT}')
    print(f'the family has run the business {YEARS} years (computed from {FOUNDED_MONTH} {FOUNDED})')
    if OPEN_QUESTIONS:
        print(f'\n{len(OPEN_QUESTIONS)} things still to confirm with Nolan (see content.py OPEN_QUESTIONS)')


if __name__ == '__main__':
    build()
