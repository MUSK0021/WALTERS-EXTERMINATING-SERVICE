# Deploying to Vercel

The site is static HTML plus one serverless function for the contact form.
Nothing is built on Vercel's side: `python3 src/build.py` produces `public/`,
`api/` and `vercel.json` locally, they are committed, and Vercel just serves
them.

```
src/           the generator. Edit here.
public/        GENERATED. 14 pages, assets, sitemap, robots.
api/           GENERATED. The contact form handler.
vercel.json    GENERATED. Routes, redirects, headers, cache rules.
```

Never edit `public/`, `api/` or `vercel.json` by hand. `build.py` overwrites all
three. `vercel.json` in particular carries a hash of the one inline script; edit
it by hand and the browser will block that script.

---

## 1. Build

```bash
python3 src/build.py && python3 src/check.py
```

`check.py` must print **NO PROBLEMS** before you deploy. It checks every page
for broken links, missing images, heading order, alt text, meta length, leftover
wording, and that the form handler only redirects to pages that exist.

## 2. Deploy from GitHub

Push the repository, then in Vercel: **Add New → Project → Import** it.

Leave every setting alone. Framework preset **Other**, build command **empty**,
install command **empty**, root directory **`./`**. `vercel.json` already
declares `outputDirectory: public`, which is the only thing Vercel needs to
know. Press **Deploy**.

From then on every push to `main` deploys itself, and a pull request gets its
own preview URL.

> If Vercel guesses a framework and fills in a build command, clear it. There is
> nothing to build: the site in `public/` is already built and committed.

## 3. Turn the contact form on

Until you do this, the form shows the "that did not send" page. The handler
needs a mailbox to send through. In **Vercel → your project → Settings →
Environment Variables**, add these for Production (and Preview if you want to
test there):

| Name | Value | Notes |
|---|---|---|
| `SMTP_HOST` | e.g. `smtp.hostinger.com` | whoever hosts `bugwalters.com` mail |
| `SMTP_PORT` | `465` | or `587` for STARTTLS |
| `SMTP_USER` | the full mailbox address | used to sign in |
| `SMTP_PASS` | an **app password** for that mailbox | not the normal password |
| `MAIL_TO` | `info@bugwalters.com` | comma separate for several |
| `MAIL_FROM_NAME` | `Walters Exterminating Website` | optional |

Then **redeploy** (Vercel → Deployments → the latest one → Redeploy), because
environment variables are only read at deploy time. Send yourself a test through `/contact/` and check it arrives.

If you use Gmail or Microsoft 365, you must create an app password; those
providers reject a normal password from a server.

## 4. Point the domain at it

In **Vercel → Settings → Domains**, add `bugwalters.com` and `www.bugwalters.com`.
Vercel will show you the DNS records to set at whoever runs the domain now.
Vercel issues the HTTPS certificate automatically.

**Do this last**, and check the deploy on the Vercel URL first, because the
current site is live and the cutover is immediate.

Two things worth knowing about the old site:

- Its contact and referral forms post over plain **HTTP**, so names, emails and
  phone numbers travel in clear text. That is the strongest reason to cut over.
- Its page URLs were auto-generated ids (`id1.html`, `id70.html` and so on).
  `vercel.json` 301s every one of them to the matching new page, so existing
  links and search rankings survive.

## 5. After it is live

- Claim the **Google Business Profile**. It is currently unclaimed, which is why
  it shows no hours and no service area. It is free and it is the single biggest
  local visibility win available.
- Take the old site down once mail is confirmed working on the new one.
- Work through `OPEN_QUESTIONS` in `content.py` with Nolan. Nothing there is
  wrong on the site today; each item is something the site currently stays quiet
  about because it has not been confirmed.

## Rolling back

Vercel keeps every deploy. **Deployments → the one you want → Promote to
Production**. It is instant and needs no rebuild.
