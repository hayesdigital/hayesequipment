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
    "award": ["Guardian Exemplary Sales Achievement Award (2003)", "American Honda 50 Years in America dealer recognition (2009)", "Bad Boy Mowers Platinum Dealer (2008, 2010)", "Bad Boy Mowers Platinum Plus Dealer (2011, 2012)", "Bad Boy Mowers Gold Dealer (2014, 2015, 2016, 2020)"],
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
    <a href="/about/">Our Story</a>
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
      <li><a href="/about/">The Hayes Equipment Story</a></li>
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
      <p>Need something else, like a harness or toggle switch? Ask us. New controllers are no longer made, but if we've got the part on the shelf, we'll let you know.</p>
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

# ---------------- ABOUT / OUR STORY ----------------
H = "/img/history/"
def fig(src, w, h, alt, cap, cls=""):
    return (f'<figure class="fig {cls}"><img src="{H}{src}.webp" width="{w}" height="{h}" loading="lazy" alt="{alt}">'
            f'<figcaption>{cap}</figcaption></figure>')

TODD = {"@type": "Person", "@id": SITE + "/about/#todd", "name": "Todd Hayes", "url": "https://toddhayes.com",
        "jobTitle": "Owner, Hayes Digital Marketing", "alumniOf": {"@type": "CollegeOrUniversity", "name": "Oklahoma State University"},
        "worksFor": {"@type": "Organization", "name": "Hayes Digital Marketing", "url": "https://toddhayes.com"},
        "homeLocation": {"@type": "Place", "name": "Ponca City, Oklahoma"},
        "knowsAbout": ["Search engine optimization", "Website design", "Local SEO", "Google Ads", "Party rental marketing"],
        "sameAs": ["https://toddhayes.com"]}
about_schema = [
    {"@context": "https://schema.org", "@type": "AboutPage", "@id": SITE + "/about/#webpage", "url": SITE + "/about/",
     "name": "The Hayes Equipment Story", "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#org"},
     "author": TODD, "primaryImageOfPage": SITE + H + "john-b-hayes-auctioneer-ponca-city.webp"},
    {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "The Hayes Equipment Story", "item": SITE + "/about/"}]},
]

TIMELINE = [
    ("1994", "Purple Haze BBS goes live from a trailer house with five phone lines"),
    ("1997", "Hayes Computer hosts computer shows at the John B. Hayes Sale Facility"),
    ("1999", "Hayes Equipment opens as a weekday retail store with Snapper mowers"),
    ("2001", "hayesequipment.com goes online, hand-coded and uploaded over FTP"),
    ("2017", "My dad, John B. Hayes, passes away"),
    ("2023", "Hayes Equipment and Hayes Products, Inc. retire"),
    ("Today", "Hayes Digital Marketing helps small businesses get found nationwide"),
]
tl = "".join(f"<li><b>{y}</b><span>{t}</span></li>" for y, t in TIMELINE)

write("/about/", head(
    "The Hayes Equipment Story: A Ponca City Family Business, Purple Haze BBS, and How I Fell in Love with SEO",
    "How a Ponca City auction family, a dial-up BBS called Purple Haze, Hayes Computer, and the Honda generator pages on hayesequipment.com started Todd Hayes on a lifelong path in website design and SEO.",
    "/about/", about_schema) + f"""
<main class="story">
<section class="story-hero"><div class="container">
  <span class="eyebrow">Our story</span>
  <h1>The Hayes Equipment Story: How a Ponca City Family Business Taught Me to Get Found Online</h1>
  <p class="byline">By Todd Hayes &middot; Ponca City, Oklahoma</p>
</div></section>

<article class="container story-body">
  <p class="lead">Fair warning: this page is pure nostalgia. You don't need to read a word of it to find a WSK-1 manual or ask about a part. That's all on the <a href="/">support page</a>.</p>
  <p>But if you've got a few minutes and a cup of coffee, I'd be glad if you stuck around. Just for old time's sake.</p>
  <p>Maybe an old link brought you here, looking for a Honda EU2000i we sold twenty years ago, or a Snapper mower, or a Cookshack smoker. If so, welcome back. Those pages are gone now. Hayes Equipment closed its doors in the fall of 2023. But I didn't want this site to just go dark. It's where my whole career started... so here's the story.</p>

  <aside class="timeline" aria-label="Hayes Equipment timeline"><h2>At a glance</h2><ol>{tl}</ol></aside>

  <h2>It started with an auctioneer and a Big Chief tablet</h2>
  {fig("john-b-hayes-auctioneer-ponca-city", 700, 875, "John B. Hayes, Ponca City auctioneer, in a Hayes cap and shirt with a cartoon auctioneer asking Do I hear five and a nickel", "My dad, John B. Hayes (1952 to 2017), doing what he loved.", "right")}
  <p>My dad, John B. Hayes, was an auctioneer. Our family ran sales out of a big metal building on the north edge of Ponca City, the John B. Hayes Sale Facility on US 77. If you grew up around here, there's a decent chance you bought something there on a Saturday. My younger brother, Scott, grew up to be a great auctioneer himself.</p>
  {fig("john-b-hayes-real-estate-auction-card-since-1981", 900, 486, "John B. Hayes Real Estate and Auction Inc. card, Putting Buyers and Sellers Together Since 1981, with a cartoon auctioneer asking Do I hear five and a nickel", "The auction company card. Putting buyers and sellers together since 1981.")}
  <p>I got pulled into the marketing side early. By the time I was 14 or 15, I was writing our auction ads by hand on a legal pad. Dad always called it a Big Chief tablet. I'd drop the pages off with Doris, a nice lady who ran a typing service out of her home. When I picked them up, they came back neatly typed. Just plain text, with a line that said "photo here" wherever I'd scribbled it.</p>
  <p>Then I'd drive those ads over to the Ponca City News and hand them through their drive-up window. We ran ads every week, in the papers and in the local shoppers too, like the Shop and Swap and the Nickel papers. When fax machines came along, the little papers around us in Tonkawa, Newkirk and Shidler got one before the Ponca City News did. So I kept making that drive.</p>
  <p>Looking back, that was my first marketing job. I just didn't know it yet.</p>

  <h2>Purple Haze BBS: getting found online before most people had the internet</h2>
  {fig("purple-haze-bbs-worlds-best-sysop-trophy-todd-hayes", 800, 1067, "Worlds Best SysOp trophy engraved for Todd Hayes, given by Purple Haze BBS users", "The &ldquo;Worlds Best SysOp&rdquo; trophy my Purple Haze BBS users gave me at the meetup they organized at Lake Ponca.", "left")}
  <p>After I got out of Oklahoma State University, I bought a little trailer house and ran five phone lines into it. That's where I started Purple Haze BBS, a dial-up bulletin board system, in 1994. (Haze with a Z. My name's spelled H-A-Y-E-S. I thought it was funny.)</p>
  <p>This was back in the DOS and Windows 3.1 days. We started out on 14,400 baud modems, then upgraded to 28,800, and later to 33,600, which felt lightning fast at the time. The other local boards were text only. Purple Haze ran on Excalibur BBS software, which had only come out the year before, and it made the whole board fully graphical, point and click. The first time you dialed in, you downloaded the Excalibur software to get access, kind of like installing a web browser today. And once you got in, the first thing you heard was a WAV file of Jimi Hendrix's "Purple Haze," turned up loud.</p>
  <p>Nearly 1,000 people signed up. Most were from Ponca City and the towns around us, but some dialed in from across the country. They played games together, chatted, sent private messages and traded files. I hosted a huge library of shareware and even Linux distributions like Red Hat. It was a social network before anybody called it that. We even had Purple Haze T-shirts made, with a Nagel girl on the front. I'm pretty sure I still have one around here somewhere.</p>
  <p>One year the users organized a lunch at the shelter houses at Lake Ponca, just so everybody could meet in person. I didn't plan it. I was just invited. And at that lunch, they surprised me with a trophy engraved "Worlds Best SysOp." I still have it.</p>
  <p>Purple Haze was one of only two or three BBSs in the area, so I take the "world's best" part with a grin. But it taught me something I still use every day. When people can find you, and they like what they find, they tell their friends.</p>

  <h2>Hayes Computer: custom PCs, computer shows and Y2K phone calls</h2>
  <p>The BBS turned out to be great marketing for my other business, Hayes Computer. Our slogan was "We custom build to fit your needs." We sold new, used and refurbished systems, plus parts, upgrades and repairs, right out of the family facility at US 77 and John B. Hayes Road.</p>
  <div class="fig-row">
    {fig("hayes-computer-business-card-ponca-city", 1000, 579, "Hayes Computer business card, We custom build to fit your needs, Todd Hayes owner, Ponca City OK", "My Hayes Computer business card. The 580 area code dates it to after Oklahoma split from 405 in late 1997.")}
    {fig("hayes-computer-show-and-sale-ad-1997-ponca-city", 760, 1014, "Newspaper ad for a Computer Show and Sale on August 9, 1997 at the John B. Hayes Sale Facility in Ponca City", "Our August 9, 1997 Computer Show &amp; Sale ad. Complete systems from $149!")}
  </div>
  <p>I hosted computer shows there too. Vendors from Oklahoma City and Wichita, Kansas, along with another computer builder from Ponca City, set up booths right alongside me. It was kind of a kick watching big city dealers drive to Ponca City to sell parts and new PCs. I still have the ad for one of them: a one-day Computer Show &amp; Sale on Saturday, August 9, 1997, co-sponsored with Abernathy's Accessories.</p>
  {fig("hayes-computer-receipt-1998-k6-233-custom-pc", 760, 1018, "Hayes Computer sales receipt from January 8, 1998 for a custom AMD K6-233 MMX computer", "A Hayes Computer receipt from January 8, 1998. Customer name blurred.", "right")}
  <p>What did a custom build look like back then? I found an old receipt from January 1998: an AMD K6-233 MMX, 64 MB of RAM, a 4.3 GB hard drive, a 24x CD-ROM, a 56k modem, 3D sound with speakers and a 15" monitor. $1,447.33 out the door.</p>
  <h3>eBay, PowerSeller status and Todd's Magic Boot Disk</h3>
  {fig("ebay-powerseller-shirt-todd-hayes", 600, 695, "eBay PowerSeller T-shirt sent to Todd Hayes by eBay", "One of the eBay PowerSeller shirts they used to mail me. I still have it.", "right narrow")}
  <p>Somewhere in there I found eBay, back when it was brand new. I started selling there in 1996. My account still says "member since April 20, 1998," and it carries 8,131 positive reviews and a 100% feedback rating.</p>
  <p>Early eBay was mostly baseball cards, collectibles and a few antiques. But every so often you'd see a lot of computer parts, and that got my attention. Pretty soon I was selling parts there too. When eBay started its PowerSeller program, I was a PowerSeller right from the start. They used to mail me all kinds of stuff: T-shirts, mouse pads, business card holders and award certificates.</p>
  <p>My best seller from that era was a 3.5" floppy I called Todd's Magic Boot Disk. Back then, a brand new computer with no operating system usually couldn't boot from a CD. To install Windows from the CD-ROM, you first had to make a boot disk with the right CD-ROM driver for your exact drive, plus the right AUTOEXEC.BAT and system files. Get one piece wrong and you were stuck. My disk had a universal driver that recognized just about any CD-ROM drive, so builders and hobbyists could pop it in and start installing. People bought a lot of them.</p>
  <p>Then came Y2K. In late 1999, I took call after call from customers worried their computer might blow up when the clock hit midnight on New Year's Eve. So I'd walk them through it. Set your date to 2000, or 2005, or 2010, and click OK. You could hear the hesitation in their voice. Probably a little wince as they clicked the mouse. And then... nothing. Their computer just kept ticking along like always.</p>

  <h2>Hayes Equipment: lawn mowers on weekdays, auctions on Saturdays</h2>
  <p>Auctions kept us busiest on weekends, especially Saturdays. Getting ready for a sale was plenty of work during the week too, but with at least three of us there, we had time for something more. So in 1999, we picked up Snapper mowers as our first equipment line, and Hayes Equipment opened as our Monday through Friday retail store. Later on, we opened a second Hayes Equipment location in Stillwater, Oklahoma, too.</p>
  <p>It grew from there. Over the years we sold Scag, Walker, Toro, Snapper, Everride, Dixie Chopper, and finally Bad Boy mowers and Bad Boy implements. We carried LS tractors and Twister mini dune buggies. We even sold Cookshack smokers, which are built right here in Ponca City.</p>
  <div class="gallery">
    {fig("hayes-equipment-storefront-ponca-city-bad-boy-outlaw", 800, 600, "Hayes Equipment storefront with red HAYES sign, company truck and a Bad Boy Outlaw zero turn mower", "The Hayes Equipment storefront on US 77.")}
    {fig("hayes-equipment-showroom-bad-boy-mowers-honda-snapper", 800, 600, "Hayes Equipment showroom lined with Bad Boy zero turn mowers, a Honda generator banner and Snapper sign", "The showroom, back when it was full.")}
    {fig("hayes-equipment-showroom-honda-generators-bad-boy-outlaw", 800, 600, "Bad Boy Outlaw mower beside Honda EU3000is and Yamaha EF2000iS generators in the Hayes Equipment showroom", "A Bad Boy Outlaw next to the Honda and Yamaha generator display.")}
    {fig("hayes-equipment-unloading-bad-boy-mower-delivery", 800, 600, "Unloading a semi trailer of new Bad Boy mowers at Hayes Equipment in Ponca City", "Unloading another semi of new Bad Boys.")}
    {fig("hayes-equipment-bad-boy-zt-elite-mowers-lot", 800, 600, "Row of Bad Boy ZT Elite zero turn mowers outside Hayes Equipment with the Bad Boy trailer behind", "A row of ZT Elites lined up out front.")}
    {fig("hayes-equipment-showroom-bad-boy-mz-magnum-zero-turns", 800, 600, "Rows of Bad Boy MZ Magnum zero turn mowers inside the Hayes Equipment showroom", "MZ Magnums ready for spring.")}
  </div>
  {fig("hayes-equipment-shop-bulldog-asleep-on-mat", 675, 900, "Buddy the English bulldog asleep in the sun on the Hayes Equipment floor mat next to a Bad Boy mower", "Buddy, my English bulldog, came to work with me every day. His favorite job was keeping the welcome mat warm.", "right narrow")}
  <p>Generators became a big part of who we were. Honda was always our anchor. We also sold Yamaha, plenty of MorPower portables, and some Winco, which were good generators even if they never sold in big numbers for us. For a couple of years we sold a lot of Kipor super quiet generators, until we started seeing quality issues we never had with Honda, so we stopped carrying them. And we sold home standby generators, enough to earn a 2003 Exemplary Sales Achievement Award for Guardian automatic home standby systems.</p>

  <h3>The awards shelf</h3>
  {fig("hayes-equipment-dealer-awards-bad-boy-mowers-honda-guardian", 1200, 900, "Hayes Equipment dealer awards from Bad Boy Mowers, American Honda and Guardian home standby generators", "Two shelves of dealer awards from Bad Boy Mowers, American Honda and Guardian.")}
  <p>For a small dealership on the north edge of Ponca City, we collected a lot of hardware. Bad Boy Mowers named us a Platinum Dealer in 2008 and 2010, a Platinum Plus Dealer in 2011 and 2012, and a Gold Dealer in 2014, 2015 and 2016. In 2009, American Honda gave us a plaque for helping Honda and its customers "realize 50 years of American dreams."</p>
  {fig("hayes-equipment-bad-boy-mowers-gold-dealer-award-2020", 800, 1067, "Bad Boy Mowers Gold Dealer Award 2020 presented to Hayes Equipment, The Great American Comeback", "Bad Boy Mowers Gold Dealer, 2020.", "right")}
  <p>The one that means the most to me might be the last one. In 2020, right in the middle of COVID, Bad Boy named us a Gold Dealer again. The theme that year was "The Great American Comeback." Even with supply drying up, we were still selling mowers... we just couldn't get our hands on enough of them.</p>

  <h3>Hayes Products and the WSK-1 remote start kit</h3>
  <p>Selling all those generators gave us an idea. Under the Hayes Products, Inc. name, we designed the <a href="/">WSK-1 wireless remote start kit</a> for the Honda EU3000is and Yamaha EF3000ise generators. We built the remotes ourselves from component parts. Then we had an overseas company produce the controllers, the "brain box" that tells the generator to start, stop and work the choke. Customers bought them from all over the world.</p>

  <h3>Getting the word out</h3>
  <p>All those years writing auction ads never really left me. We put the Hayes name everywhere we could: a billboard that said "Mow With an Attitude," booths at home and garden shows with a giant inflatable Bad Boy bulldog, our trailer, Snapper rain gauges people stuck in their yards, and a Hayes Equipment decal on just about every mower and generator that left the lot.</p>
  <div class="gallery">
    {fig("hayes-equipment-billboard-bad-boy-honda-mow-with-an-attitude", 800, 600, "Hayes Equipment billboard for Bad Boy Mowers and Honda Power Equipment, Mow With an Attitude, 580-762-6334", "Our Bad Boy and Honda billboard.")}
    {fig("hayes-equipment-trade-show-booth-bad-boy-bulldog-inflatable", 800, 600, "Hayes Equipment trade show booth with a giant inflatable Bad Boy bulldog and banner", "Show booth, with the bulldog doing the heavy lifting.")}
    {fig("hayes-equipment-snapper-rain-gauge-giveaway", 800, 600, "Hayes Equipment Ponca City Snapper rain gauge giveaway with phone number 580-762-6334", "A Snapper rain gauge giveaway from the early days.")}
    {fig("hayes-equipment-dealer-decal-honda-eu3000is-generator", 800, 600, "Hayes Equipment dealer decal on a Honda EU3000is inverter generator", "Every unit left with our decal on it.")}
    {fig("hayes-equipment-trailer-bad-boy-mz-magnum-mowers", 800, 600, "Hayes Equipment trailer and Bad Boy MZ Magnum mowers in front of the John B. Hayes Real Estate and Auction building", "Our trailer, parked in front of the auction building.")}
    {fig("bad-boy-mowers-semi-delivery-hayes-equipment-trailer", 800, 600, "Bad Boy Mowers semi truck delivering mowers to Hayes Equipment in Ponca City", "Bad Boy's truck pulling in with another load.")}
  </div>

  <h2>hayesequipment.com and the Honda generator pages that ranked nationwide</h2>
  <p>I registered hayesequipment.com in January 2001 through Network Solutions and hosted it with a small Texas company called X7 Hosting. I built every page by hand in Microsoft FrontPage Express and uploaded each HTML file, one at a time, over FTP.</p>
  <p>It worked better than I ever expected. When people searched for a quiet Honda generator, like the EU1000i, EU2000i, EU3000is or later the EU6500is, or a Honda generator for construction or home backup, our little Ponca City dealership showed up at the top of Google. Not just locally. Nationwide.</p>
  <p>Every time we added a new product line, I built its page the same way, aiming for Google to pick us as a top place to buy. Mowers, tractors, smokers. It kept working. That's when I fell in love with SEO. Figuring out what people were searching for, then building the page that answered it best, never got old.</p>

  <h2>My first big website mistake, and the lesson I never forgot</h2>
  <p>A few years in, I moved the site from X7 Hosting to GoDaddy so we could have a better shopping cart. The new site looked prettier. It was also my first big mistake in the website business.</p>
  {fig("hayesequipment-com-old-website-shopping-cart", 450, 754, "Later version of hayesequipment.com with a shopping cart, Hayes Equipment logo and Hayes Products EU3000is wireless remote start kits", "A later version of hayesequipment.com, shopping cart and all.", "right narrow")}
  <p>The move changed every URL on the site. RV forums, lawn mower forums and all kinds of other websites had links pointing to our specific pages, and overnight those links went nowhere. I didn't know what a 301 redirect was back then, much less how to write an .htaccess file on an Apache server to send every old address to its new home.</p>
  <p>We lost a lot of the ranking power those links had built up. Worse, people started calling and emailing because the links they clicked were dead. Some of them genuinely thought we'd gone out of business.</p>
  <p>That one stuck with me. I've never caused that problem for a client, and I've fixed it for plenty of businesses since. With this rebuild, I finally went back and added the redirects I didn't know to add twenty years ago. If an old link brought you to this page, now you know why.</p>

  <h2>Saying goodbye to Hayes Equipment</h2>
  <p>My dad passed away in 2017. We kept the business going for several more years, and honestly, we probably would have kept going longer if not for COVID. The shutdowns choked off supply. We couldn't get enough new Bad Boy mowers and other equipment to cover what we could sell, or even enough sales to keep the doors open.</p>
  <p>COVID hit Hayes Products too. The overseas company that built our WSK-1 controllers went out of business. Building them in-house would have cost too much, and we couldn't find another manufacturer who could make them at a reasonable price. So we stopped producing the kits.</p>
  <p>So in the fall of 2023, we retired Hayes Equipment and Hayes Products, Inc. It was the right time to move on to brighter territory. We still support our WSK-1 customers, and this site is still here to do that.</p>

  <h2>Where I am now: Hayes Digital Marketing</h2>
  <p>After we closed, I went full time with my own agency, <a href="https://toddhayes.com">Hayes Digital Marketing</a>. Since then I've helped small businesses from coast to coast get found: barbershops, a truck flatbed manufacturer with a nationwide dealer network, boutique shops on small-town main streets, and HVAC and plumbing companies.</p>
  <p>Most of all, I've become known for party rental marketing. I help bounce house, tent, table and chair rental companies from California and Arizona to Kansas City, Idaho and Florida rank high on Google and in AI search, so they get more paid bookings and keep their calendars full.</p>
  <p>It's the same thing I was doing with a Big Chief tablet at 15, and with Honda generator pages in 2001. Find out what people are looking for, then make sure they find you first.</p>
  <div class="cta-card">
    <div><h3>Own a small business that needs to get found?</h3><p>Learn more about me and how I help businesses rank on Google and in AI search.</p></div>
    <a class="btn" href="https://toddhayes.com">Visit toddhayes.com</a>
  </div>
  <div class="cta-card alt">
    <div><h3>Still running a WSK-1 remote start kit?</h3><p>Grab the manuals, troubleshooting tips and replacement parts.</p></div>
    <a class="btn ghost" href="/">WSK-1 Support</a>
  </div>
</article>
</main>
""" + FOOT)

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
urls = ["/", "/about/", "/privacy/"] + [f"/docs/{f}" for f, _, _ in DOCS]

# 301s for old hayesequipment.com URLs that still have backlinks (from SE Ranking, Oct 2026).
# WSK-1 / Hayes Products pages go to the support home page; old dealership pages go to the story page.
TO_HOME = ["/hayes_products.htm", "/portable_generator_wireless_remote_start_kit.htm",
           "/portable_generator_wireless_remote_start_ki", "/portable_generator_wireless_remote_"]
TO_ABOUT = ["/eu1000i.htm", "/eu2000i.htm", "/eu3000is.htm", "/eu6500is.htm", "/eb12d.htm", "/ex4500.htm", "/es6500.htm",
            "/wholesale.htm", "/honda_generator_wattage_guide.htm", "/kipor_generators.htm", "/pl400aerator.htm",
            "/sahara_mini_250cc_dune_buggy.htm", "/sahara_250cc_dune_buggy_gallery/", "/sahara_250cc_dune_buggy_gallery/index.html",
            "/p/honda-generators", "/honda/*", "/yamaha_generators/*", "/wholesale/*", "/p/*"]
(ROOT / "_redirects").write_text("".join(f"{u} / 301\n" for u in TO_HOME) + "".join(f"{u} /about/ 301\n" for u in TO_ABOUT))
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{SITE}{u}</loc></url>\n" for u in urls) + "</urlset>\n")
(ROOT / "site.webmanifest").write_text(json.dumps({"name": "Hayes Equipment WSK-1 Support", "short_name": "Hayes Equipment",
    "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"}],
    "theme_color": "#232428", "background_color": "#f6f5f2", "display": "browser"}, indent=2))
(ROOT / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="11" fill="#c8102e"/>'
    '<text x="32" y="47" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="44" fill="#fff">H</text></svg>')
print("Built", sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob("*.html")))
