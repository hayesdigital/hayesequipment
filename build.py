"""Builds the hayesequipment.com static site into ./public. Run: python3 build.py"""
import json, pathlib

ROOT = pathlib.Path(__file__).parent / "public"
SITE = "https://www.hayesequipment.com"
FORM_EMAIL = "todd@toddhayes.com"      # where contact form messages are delivered (via FormSubmit)
PHONE = "(580) 767-9056"
PHONE_TEL = "+15807679056"
ADDRESS = "1417 John B Hayes Rd, Ponca City, OK 74601"
FACEBOOK = "https://facebook.com/HayesEquipment"
YEAR = 2026

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">')

# ---- the downloadable manuals (file lives in public/docs/) ----
DOCS = [
    ("wsk-1-operating-instructions.pdf", "WSK-1 Operating Instructions", "How to start and stop your generator with the remote. 1 page"),
    ("wsk-1-troubleshooting-faq.pdf", "WSK-1 Troubleshooting FAQ", "Fixes for clicking, no start, and won't shut off. 1 page"),
    ("wsk-1-remote-key-fob-programming.pdf", "WSK-1 Remote Key Fob Programming", "Pair a new or replacement fob to your control box. 1 page"),
    ("wsk-1-honda-eu3000is-installation-instructions.pdf", "Honda EU3000is Installation Instructions", "Original WSK-1 install guide with photos. 17 pages"),
    ("wsk-1-yamaha-ef3000ise-installation-instructions.pdf", "Yamaha EF3000ise / EF3000iseB Installation Instructions", "Original WSK-1 install guide with photos. 12 pages"),
]

def size(f):
    b = (ROOT / "docs" / f).stat().st_size
    return f"{b/1024/1024:.1f} MB" if b > 1024 * 1024 else f"{round(b/1024)} KB"

def doc_list():
    items = "".join(
        f'<li><a class="doc" href="/docs/{f}" download><span class="ico">PDF</span><span><b>{t}</b><span>{d} &middot; {size(f)}</span></span></a></li>'
        for f, t, d in DOCS)
    return f'<ul class="doc-list">{items}</ul>'

TOPICS = ["General question", "Replacement remote key fob", "Replacement choke controller",
          "Other replacement part", "Installation or troubleshooting help"]
GENERATORS = ["Honda EU3000is", "Yamaha EF3000ise", "Yamaha EF3000iseB", "Other or not sure"]

# ---- troubleshooting (used on page and in FAQ schema) ----
FIXES = [
    ("The remote only clicks and won't turn the engine over",
     "The generator's battery is a little too weak to crank the engine remotely. Remote starting asks more of the battery than the key does, so a battery that seems \"fine\" can still come up short.",
     "Disconnect the battery and give it a full charge. If it still clicks after charging, the battery is likely worn out and should be replaced."),
    ("The generator starts but won't shut off with the remote or the key",
     "This almost always happens when the generator was started with the remote while the ignition key was turned on, or started with the key while the control panel toggle switch was on.",
     "Unplug the WSK-1 control box power connector and the wide harness plug. Count to 10, then plug them back in. That resets the ground circuits so the generator can shut down. To keep it from happening again, leave the key OFF (or out) when you start with the remote. Keep the toggle switch ON when using the remote, and OFF for storage or when starting with the key."),
]

FAQ = [(q, f"{cause} {fix}") for q, cause, fix in FIXES] + [
    ("Can I still get a replacement key fob or choke controller for my WSK-1 kit?",
     "Yes. Hayes Equipment still supports WSK-1 owners with replacement parts like remote key fobs and choke controllers. Use the contact form on hayesequipment.com and pick the part you need from the dropdown."),
    ("How do I program a new remote key fob to my WSK-1 control box?",
     "Hold program button 1 (closest to the antenna) until the LED flashes, press ON/OFF on the fob, then press button 1 again. Repeat with button 2 and the START button, then button 3 and the ARM button. The full steps are on this page and in the key fob programming PDF."),
    ("Which generators does the WSK-1 remote start kit fit?",
     "The WSK-1 wireless remote start kit was made for the Honda EU3000is and the Yamaha EF3000ise and EF3000iseB generators. Installation instructions for both are free to download on this page."),
]

ORG = {
    "@context": "https://schema.org", "@type": "Organization", "@id": SITE + "/#org",
    "name": "Hayes Equipment", "alternateName": ["Hayes Products", "Hayes Products, Inc."],
    "url": SITE + "/", "logo": SITE + "/icon-512.png", "telephone": PHONE_TEL,
    "description": "Product support and replacement parts for the Hayes Products WSK-1 wireless remote start kit for Honda EU3000is and Yamaha EF3000ise generators.",
    "address": {"@type": "PostalAddress", "streetAddress": "1417 John B Hayes Rd", "addressLocality": "Ponca City",
                "addressRegion": "OK", "postalCode": "74601", "addressCountry": "US"},
    "sameAs": [FACEBOOK],
}
WEBSITE = {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "name": "Hayes Equipment", "url": SITE + "/", "publisher": {"@id": SITE + "/#org"}}

OG = "/img/wsk-1-remote-start-kit-support-share.jpg"

def head(title, desc, path, schemas=(), noindex=False):
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, separators=(",", ":"))}</script>' for s in [ORG, *schemas])
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Hayes Equipment"><meta property="og:locale" content="en_US">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}{OG}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="WSK-1 wireless remote start kit support for Honda EU3000is and Yamaha EF3000ise generators">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{SITE}{OG}">
<meta name="theme-color" content="#232428">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">
{FONTS}
<link rel="stylesheet" href="/styles.css">
{ld}
</head>
<body>
<header class="site-header"><div class="container">
  <a class="logo" href="/"><span class="mark">H</span><span><b>HAYES EQUIPMENT</b><small>WSK-1 Remote Start Support</small></span></a>
  <nav class="nav" aria-label="Main">
    <a href="/#manuals">Manuals</a>
    <a href="/#troubleshooting">Troubleshooting</a>
    <a href="/#program-key-fob">Program a Fob</a>
    <a href="/#replacement-parts">Parts</a>
    <a class="btn" href="/#contact">Contact Us</a>
  </nav>
</div></header>
"""

FOOT = f"""<footer class="site-footer"><div class="container">
  <div class="cols">
    <div>
      <a class="logo" href="/"><span class="mark">H</span><span><b>HAYES EQUIPMENT</b><small>WSK-1 Remote Start Support</small></span></a>
      <p style="margin-top:14px;max-width:44ch">Hayes Products, Inc. of Ponca City, Oklahoma, made the WSK-1 wireless remote start kit for Honda and Yamaha generators. Our store is closed, but we still help owners keep their kits running.</p>
    </div>
    <div><ul>
      <li><a href="/#manuals">Download Manuals</a></li>
      <li><a href="/#how-to-start">How to Use the Remote</a></li>
      <li><a href="/#troubleshooting">Troubleshooting</a></li>
      <li><a href="/#program-key-fob">Program a Key Fob</a></li>
      <li><a href="/#replacement-parts">Replacement Parts</a></li>
      <li><a href="/#contact">Contact Us</a></li>
    </ul></div>
    <div><ul>
      <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
      <li>1417 John B Hayes Rd<br>Ponca City, OK 74601</li>
      <li><a href="{FACEBOOK}" rel="noopener">Facebook</a></li>
    </ul></div>
  </div>
  <div class="bottom">&copy; {YEAR} Hayes Equipment. Hayes Products and WSK-1 are trademarks of Hayes Products, Inc. Honda and Yamaha are trademarks of their respective owners. &middot; <a href="/privacy/">Privacy Policy</a></div>
</div></footer>
<script>
(function(){{
  var sel=document.getElementById("f-topic"), subj=document.getElementById("f-subject");
  function setSubj(){{ if(sel&&subj) subj.value="Hayes Equipment website: "+sel.value; }}
  if(sel){{ sel.addEventListener("change",setSubj); setSubj(); }}
  document.querySelectorAll("[data-topic]").forEach(function(a){{
    a.addEventListener("click",function(){{ if(sel){{ sel.value=a.getAttribute("data-topic"); setSubj(); }} }});
  }});
  document.querySelectorAll(".next-url").forEach(function(i){{ i.value=location.origin+"/thank-you/"; }});
}})();
</script>
</body>
</html>
"""

def contact_form():
    topics = "".join(f"<option>{t}</option>" for t in TOPICS)
    gens = "".join(f"<option>{g}</option>" for g in GENERATORS)
    return f"""<div class="form-card">
  <h3>Send us a message</h3>
  <form action="https://formsubmit.co/{FORM_EMAIL}" method="POST">
    <input type="hidden" name="_subject" id="f-subject" value="Hayes Equipment website message">
    <input type="hidden" name="_next" value="{SITE}/thank-you/" class="next-url">
    <input type="hidden" name="_template" value="table">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
    <label for="f-topic">What's your message about?</label>
    <select id="f-topic" name="topic" required>{topics}</select>
    <label for="f-gen">Which generator is your kit on?</label>
    <select id="f-gen" name="generator">{gens}</select>
    <div class="row">
      <div><label for="f-name">Your name</label><input id="f-name" name="name" required autocomplete="name"></div>
      <div><label for="f-email">Email</label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
    </div>
    <label for="f-phone">Phone (optional)</label><input id="f-phone" name="phone" type="tel" autocomplete="tel">
    <label for="f-msg">How can we help?</label>
    <textarea id="f-msg" name="message" required placeholder="Tell us what's going on, or which part you need and how many."></textarea>
    <button class="btn" type="submit">Send My Message</button>
    <p class="fine">We'll reply by email. Your info is only used to answer your message.</p>
  </form>
</div>"""

def write(path, html):
    out = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)

# ---------------- HOME ----------------
fix_html = "".join(f'<div class="fix"><h3>{q}</h3><p><b>Why it happens:</b> {c}</p><p><b>The fix:</b> {f}</p></div>' for q, c, f in FIXES)
faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
page_schema = {"@context": "https://schema.org", "@type": "WebPage", "@id": SITE + "/#webpage", "url": SITE + "/",
               "name": "Honda EU3000is and Yamaha EF3000ise Remote Start Kit Support", "isPartOf": {"@id": SITE + "/#website"},
               "about": {"@id": SITE + "/#org"}, "primaryImageOfPage": SITE + "/img/honda-eu3000is-generator-wsk-1-wireless-remote-start-kit.webp"}

home = head(
    "Honda EU3000is Remote Start Kit Support, Manuals and Parts | WSK-1 by Hayes Products",
    "WSK-1 wireless remote start kit support for Honda EU3000is and Yamaha EF3000ise generators. Download the manuals, fix common problems, program a key fob, and order replacement parts.",
    "/", [WEBSITE, page_schema, faq_schema]) + f"""
<main>
<section class="hero"><div class="container hero-grid">
  <div>
    <span class="eyebrow">Hayes Products WSK-1 Support</span>
    <h1>Honda EU3000is and Yamaha EF3000ise Remote Start Kit Support</h1>
    <p class="lead">Still running a WSK-1 remote start kit on your generator? We're glad it's still earning its keep. Our store has closed, but we still help WSK-1 owners with the original manuals, troubleshooting, and replacement parts like key fobs and choke controllers.</p>
    <div class="hero-actions">
      <a class="btn" href="#manuals">Download the Manuals</a>
      <a class="btn ghost" href="#contact" data-topic="Replacement remote key fob">Ask About a Part</a>
    </div>
    <ul class="trust">
      <li>Original Hayes Products manuals</li>
      <li>Replacement fobs and choke controllers</li>
      <li>Answered by a real person in Ponca City, OK</li>
    </ul>
  </div>
  <div class="quick" id="manuals">
    <img src="/img/honda-eu3000is-generator-wsk-1-wireless-remote-start-kit.webp" width="352" height="248" alt="Honda EU3000is generator with the Hayes Products WSK-1 wireless remote start key fob in hand">
    <h2>WSK-1 manuals and instructions (free PDF downloads)</h2>
    {doc_list()}
    <p class="note" style="margin-top:12px">Heads up: some older manuals list phone numbers we no longer use. Please reach us through the contact form or the number on this page.</p>
  </div>
</div></section>

<section id="how-to-start"><div class="container two">
  <div>
    <span class="eyebrow">Using your remote</span>
    <h2>How to start your generator with the WSK-1 remote</h2>
    <p>Before anything else, make sure the generator's battery is installed the way the manufacturer says and fully charged. Leave the ignition key in the OFF position. The key still works normally... you just don't need it (or the choke) when you start with the remote, because the WSK-1 handles the choke for you.</p>
    <ol class="steps" style="margin-top:18px">
      <li>Turn the toggle switch on the generator's control panel to <b>ON</b>.</li>
      <li>Press the red <b>ON/OFF</b> button on the fob.</li>
      <li>Press the <b>ARM/DISARM</b> button (gray on Honda kits, white on Yamaha kits).</li>
      <li>Press the blue <b>START</b> button. The engine turns over and the generator starts.</li>
      <li>Didn't catch the first time? Press ARM/DISARM again, then START.</li>
    </ol>
    <p class="note">The AUX 1 button isn't used on the WSK-1.</p>
  </div>
  <div class="card">
    <h3>Stopping the generator</h3>
    <ol class="steps">
      <li>Press the red <b>ON/OFF</b> button on the fob. The generator shuts down.</li>
      <li>Turn the control panel toggle switch to <b>OFF</b> if you're storing the generator or won't use the remote for a while. That keeps the kit from slowly draining your battery.</li>
    </ol>
    <img src="/img/wsk-1-replacement-remote-key-fob.webp" width="362" height="416" loading="lazy" alt="WSK-1 remote key fob with ON/OFF, START, ARM/DISARM and AUX 1 buttons" style="max-width:220px;margin:20px auto 0;border-radius:8px">
  </div>
</div></section>

<section class="alt" id="troubleshooting"><div class="container" style="max-width:860px">
  <span class="eyebrow">Troubleshooting</span>
  <h2>WSK-1 troubleshooting: the two problems we hear about most</h2>
  <p>Nine times out of ten, a WSK-1 that "quit working" is one of these two things. Both are quick fixes you can do in your driveway.</p>
  {fix_html}
  <p style="margin-top:26px">Tried these and still stuck? <a href="#contact" data-topic="Installation or troubleshooting help">Send us a message</a> and tell us what the generator is doing. The more detail, the better.</p>
</div></section>

<section id="program-key-fob"><div class="container two">
  <div>
    <span class="eyebrow">Key fob programming</span>
    <h2>How to program a new or replacement WSK-1 key fob</h2>
    <p>Got a new fob, or adding a second one? You'll pair it to the control box using the three small program buttons on the box. Button 1 is the one closest to the antenna. Each pairing takes a few seconds.</p>
    <ol class="steps" style="margin-top:18px">
      <li>Press and hold program button <b>1</b> until the LED lights up and flashes.</li>
      <li>While it's flashing, press <b>ON/OFF</b> on the fob. The LED stays lit for a moment, then flashes.</li>
      <li>Press button <b>1</b> once. The blue light goes out.</li>
      <li>Press and hold program button <b>2</b> until the LED lights up and flashes.</li>
      <li>While it's flashing, press <b>START</b> on the fob. The LED stays lit for a moment, then flashes.</li>
      <li>Press button <b>2</b> once. The blue light goes out.</li>
      <li>Press and hold program button <b>3</b> until the LED lights up and flashes.</li>
      <li>While it's flashing, press <b>ARM/DISARM</b> on the fob. The LED stays lit for a moment, then flashes.</li>
      <li>Press button <b>3</b> once. The blue light goes out. That's it, your new fob is paired.</li>
    </ol>
  </div>
  <div>
    <img src="/img/wsk-1-control-box-programming-buttons.webp" width="592" height="428" loading="lazy" alt="WSK-1 control box showing program buttons 1, 2 and 3 for pairing a key fob" style="border-radius:10px;border:1px solid var(--line)">
    <p style="font-size:.9rem;color:var(--muted);margin-top:8px">The three program buttons on the WSK-1 control box. Button 1 sits closest to the antenna.</p>
    <p style="margin-top:16px"><a href="/docs/wsk-1-remote-key-fob-programming.pdf" download>Download the printable key fob programming sheet (PDF)</a></p>
  </div>
</div></section>

<section class="alt" id="replacement-parts"><div class="container">
  <span class="eyebrow">Replacement parts</span>
  <h2>WSK-1 replacement parts</h2>
  <p style="max-width:62ch">Lost a fob in the yard? Choke controller finally gave up? We still have parts to keep your WSK-1 going. Just tell us what you need and which generator it's on, and we'll get back to you with pricing and shipping.</p>
  <div class="parts">
    <div class="part">
      <img src="/img/wsk-1-replacement-remote-key-fob.webp" width="362" height="416" loading="lazy" alt="Replacement WSK-1 wireless remote key fob for Honda and Yamaha generator remote start kits">
      <h3>Replacement remote key fob</h3>
      <p>A new or spare fob for your WSK-1. Pairs to your existing control box in a couple of minutes using the steps above.</p>
      <a class="btn" href="#contact" data-topic="Replacement remote key fob">Ask About a Key Fob</a>
    </div>
    <div class="part">
      <div class="ph">WSK-1 Choke Controller</div>
      <h3>Replacement choke controller</h3>
      <p>The actuator and cable that work the choke automatically when you start with the remote. Fits the Honda EU3000is and Yamaha EF3000ise kits.</p>
      <a class="btn" href="#contact" data-topic="Replacement choke controller">Ask About a Choke Controller</a>
    </div>
    <div class="part">
      <img src="/img/wsk-1-control-box-mounted-honda-eu3000is-door.webp" width="640" height="480" loading="lazy" alt="WSK-1 control box mounted inside the side door of a Honda EU3000is generator">
      <h3>Other WSK-1 parts</h3>
      <p>Need something else, like a harness, toggle switch, or control box? Ask us. If we've got it, we'll let you know.</p>
      <a class="btn" href="#contact" data-topic="Other replacement part">Ask About Another Part</a>
    </div>
  </div>
</div></section>

<section id="contact"><div class="container two">
  <div class="contact-side">
    <span class="eyebrow">Contact</span>
    <h2>Questions about your WSK-1? Send us a message.</h2>
    <p>Pick what your message is about, tell us which generator you've got, and we'll reply by email. Whether it's a part you need or a generator that's acting up, we're happy to help.</p>
    <ul>
      <li><b>Call</b><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
      <li><b>Mailing address</b>{ADDRESS}</li>
      <li><b>Facebook</b><a href="{FACEBOOK}" rel="noopener">facebook.com/HayesEquipment</a></li>
    </ul>
  </div>
  {contact_form()}
</div></section>
</main>
""" + FOOT
write("/", home)

# ---------------- THANK YOU ----------------
write("/thank-you/", head("Thanks for Your Message | Hayes Equipment", "Thanks for contacting Hayes Equipment about your WSK-1 remote start kit.", "/thank-you/", noindex=True) + f"""
<main class="page"><div class="container">
  <span class="eyebrow">Message sent</span>
  <h1>Thanks, we got your message.</h1>
  <p class="lead" style="margin-top:14px">We'll read it and reply by email as soon as we can. If you asked about a part, we'll include pricing and shipping in our reply.</p>
  <h2>While you wait</h2>
  <p>A lot of WSK-1 questions are answered in the original manuals. Feel free to grab any of them:</p>
  <div style="margin-top:16px">{doc_list()}</div>
  <p style="margin-top:24px">Or jump to the <a href="/#troubleshooting">troubleshooting tips</a> and <a href="/#program-key-fob">key fob programming steps</a>.</p>
  <p style="margin-top:24px"><a class="btn" href="/">Back to WSK-1 Support</a></p>
</div></main>
""" + FOOT)

# ---------------- PRIVACY ----------------
write("/privacy/", head("Privacy Policy | Hayes Equipment", "How Hayes Equipment handles the information you send through hayesequipment.com.", "/privacy/") + f"""
<main class="page"><div class="container">
  <h1>Privacy Policy</h1>
  <p style="margin-top:14px">Hayes Equipment, {ADDRESS}, runs hayesequipment.com to support owners of the Hayes Products WSK-1 wireless remote start kit. This page explains what information we collect and how we use it.</p>
  <h2>Information you give us</h2>
  <p>When you use our contact form, we collect what you enter: your name, email, phone number (if you give it), your generator model, the topic you pick, and your message. We use it only to answer your question or help with a parts request.</p>
  <h2>How form messages are delivered</h2>
  <p>Our contact form is processed by FormSubmit, a third-party form service that delivers your message to our email. Their handling of data is covered by their own privacy policy.</p>
  <h2>Information collected automatically</h2>
  <p>Like most websites, our hosting provider may log basic technical information such as IP address, browser type and pages visited, for security and performance.</p>
  <h2>Sharing</h2>
  <p>We don't sell, rent or trade your personal information. We only share it with service providers that help us run this website, or when required by law.</p>
  <h2>Your choices</h2>
  <p>You can ask us to update or delete the information you've sent at any time. Just send us a message through the <a href="/#contact">contact form</a> or call <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p>
</div></main>
""" + FOOT)

# ---------------- 404 ----------------
(ROOT / "404.html").write_text(head("Page Not Found | Hayes Equipment", "That page isn't here. Find WSK-1 manuals, troubleshooting and parts on the home page.", "/404.html", noindex=True) + f"""
<main class="page"><div class="container">
  <h1>That page isn't here.</h1>
  <p class="lead" style="margin-top:14px">We moved things around a bit. Everything for the WSK-1 remote start kit is on one page now, including all the manuals:</p>
  <div style="margin-top:18px">{doc_list()}</div>
  <p style="margin-top:24px"><a class="btn" href="/">Go to WSK-1 Support</a></p>
</div></main>
""" + FOOT)

# ---------------- misc files ----------------
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
urls = ["/", "/privacy/"] + [f"/docs/{f}" for f, _, _ in DOCS]
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
(ROOT / "site.webmanifest").write_text(json.dumps({"name": "Hayes Equipment WSK-1 Support", "short_name": "Hayes Equipment",
    "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}],
    "theme_color": "#232428", "background_color": "#f6f5f2", "display": "browser"}, indent=2))
(ROOT / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="11" fill="#c8102e"/>'
    '<text x="32" y="47" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="44" fill="#fff">H</text></svg>')
print("Built", sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob("*.html")))
