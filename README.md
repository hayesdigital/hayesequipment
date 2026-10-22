# hayesequipment.com

Support site for the Hayes Products WSK-1 wireless remote start kit (Honda EU3000is, Yamaha EF3000ise/iseB).

- `build.py` generates every page into `public/`. Edit it, run `python3 build.py`, commit and push. Cloudflare deploys on push.
- `public/docs/` holds the original WSK-1 PDFs.
- Contact form posts to FormSubmit and delivers to todd@toddhayes.com (set `FORM_EMAIL` in build.py). The first submission from the live site sends FormSubmit an activation email that must be confirmed once.
- `wrangler.jsonc` is the Cloudflare static-assets config.
- `.github/workflows/indexnow.yml` pings IndexNow after each push.
