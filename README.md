# Walters Exterminating Service

The website for Walters Exterminating Service, Northeast Philadelphia.
Family owned since April 1963. Live at **bugwalters.com**.

Fourteen static pages and one serverless function for the contact form. No
framework, no build step on the server, no JavaScript needed to read any of it.

---

## Deploying

The repository is already in the shape Vercel expects, so importing it needs no
settings in the dashboard:

```
public/        the built site        <- vercel.json points here
api/           the contact form handler
vercel.json    routes, redirects, security headers, cache rules
src/           the generator that produces all three
```

**Import the repo in Vercel and press deploy.** Framework preset "Other", no
build command, no install command. `vercel.json` already declares
`outputDirectory: public`, so leave every field alone. Every push to `main`
redeploys.

Then set the mail variables, or the form will land on its "that did not send"
page. See [DEPLOY.md](DEPLOY.md) for those and for the domain cutover.

## Changing the site

Everything readable lives in `src/content.py`: the words, the services, the
pests, the service area, the FAQ. Edit there, then:

```bash
python3 src/build.py && python3 src/check.py
```

`check.py` must print **NO PROBLEMS** before you push. It reads every built page
and fails on broken links, missing images, dead anchors, heading order, empty
alt text, meta descriptions outside 50 to 170 characters, two adjacent headings
saying the same thing, wording that must never ship, and any redirect in the
form handler that points at a page which does not exist.

Commit the regenerated `public/` along with your source change. The built site
is committed on purpose: it is what Vercel serves, and it means a deploy never
depends on Python being available.

### The other scripts

| | |
|---|---|
| `src/tools/photos.py` | Rebuilds every image. Pexels originals are fetched by id and cached in `src/_photos/` (gitignored); the company's own photographs are in `src/_source-photos/` and are committed. |
| `src/tools/mklogo.py` | Regenerates `src/logo_paths.py`, the oval badge as vector outlines. |
| `src/tools/mkicons.py` | Favicon and app icon, from those same outlines. |
| `src/tools/mkog.py` | The social share card. |
| `src/tools/shots.py` | Full page screenshots into `src/_shots/`, for design review. |

## House rules

`src/content.py` opens with them and they are not decoration. The short version:

- **Never hard-code the company's age.** `FOUNDED = 1963` is the only source of
  truth and `build.py` computes any number from it. The old site said "Our 63rd
  Year" and sat frozen at "2017 is our 54th Year" for about eight years.
- **Family owned since 1963, never "LLC since 1963".** The LLC is PA entity
  3981492, filed 23 September 2010.
- **No ratings, no review counts, no BBB badge.** There is no BBB profile, and
  marking up your own aggregate rating breaches Google's structured data policy.
- **No street address.** Their own site publishes none, deliberately.
- **Nothing unverified goes live.** `OPEN_QUESTIONS` at the bottom of
  `content.py` lists fifteen things the site currently stays quiet about because
  nobody has confirmed them yet.

The false claim that "in 1967 the E.P.A required all Pest control companies to
be Licensed by the State" is gone and must not come back in any form. The EPA
was created in December 1970, has never licensed pest control operators in
Pennsylvania, and PA licensing comes from the Pennsylvania Pesticide Control Act
of 1973.

## Licensing of the images

`src/_source-photos/` is the Walters family's own work.

Everything else is Pexels, under the Pexels licence: free to use commercially,
no attribution required. The photo id is recorded against each one in
`src/tools/photos.py`, so any of them can be traced back to its source.

Fraunces and Inter are both SIL Open Font Licence; the licence text ships with
them in `src/static/assets/fonts/OFL.txt`.
