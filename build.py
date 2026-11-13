# One-off generator for the Dr. Pressure static pages (shared header/footer).
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
PHONE = "+17868622611"; PHONE_TXT = "(786) 862-2611"
EMAIL = "doctorpressurecleaning@gmail.com"
IG = "https://www.instagram.com/dr.pressurecleaning/"
FB = "https://www.facebook.com/profile.php?id=61586886702951"
GMAPS = "https://www.google.com/maps/place/Dr.+Pressure+Cleaning+Services,+LLC/@26.540264,-80.9608332,9z/data=!4m8!3m7!1s0x623ec37fb17737cd:0x69ecc6bd66718e75!8m2!3d26.541781!4d-80.3013955!9m1!1b1!16s%2Fg%2F11wqyf3mq2"

I = {
 "phone": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>',
 "mail": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4-8 5-8-5V6l8 5 8-5z"/></svg>',
 "pin": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>',
 "check": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm-2 15-5-5 1.4-1.4 3.6 3.6 7.6-7.6L19 8z"/></svg>',
 "arrow": '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4l-1.4 1.4 5.6 5.6H4v2h12.2l-5.6 5.6L12 20l8-8z"/></svg>',
 "ig": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4zM17.3 5.5a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4zM21.9 7.8c-.1-1.6-.4-3-1.6-4.1S17.8 2.2 16.2 2.1C14.5 2 9.5 2 7.8 2.1 6.2 2.2 4.8 2.5 3.7 3.7S2.2 6.2 2.1 7.8C2 9.5 2 14.5 2.1 16.2c.1 1.6.4 3 1.6 4.1s2.5 1.5 4.1 1.6c1.7.1 6.7.1 8.4 0 1.6-.1 3-.4 4.1-1.6s1.5-2.5 1.6-4.1c.1-1.7.1-6.7 0-8.4zm-2.2 10.3a3.3 3.3 0 0 1-1.9 1.9c-1.3.5-4.4.4-5.8.4s-4.5.1-5.8-.4a3.3 3.3 0 0 1-1.9-1.9c-.5-1.3-.4-4.4-.4-5.8s-.1-4.5.4-5.8a3.3 3.3 0 0 1 1.9-1.9c1.3-.5 4.4-.4 5.8-.4s4.5-.1 5.8.4a3.3 3.3 0 0 1 1.9 1.9c.5 1.3.4 4.4.4 5.8s.1 4.5-.4 5.8z"/></svg>',
 "fb": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"/></svg>',
 "g": '<svg viewBox="0 0 48 48" width="20" height="20" aria-hidden="true"><path fill="#EA4335" d="M24 9.5c3.5 0 6.6 1.2 9.1 3.6l6.8-6.8C35.8 2.4 30.3 0 24 0 14.6 0 6.6 5.4 2.6 13.3l7.9 6.1C12.4 13.7 17.7 9.5 24 9.5z"/><path fill="#4285F4" d="M46.1 24.5c0-1.6-.1-3.1-.4-4.5H24v9h12.4c-.5 2.9-2.2 5.3-4.6 6.9l7.4 5.7c4.3-4 6.9-9.9 6.9-17.1z"/><path fill="#FBBC05" d="M10.5 28.6A14.5 14.5 0 0 1 9.5 24c0-1.6.3-3.2.8-4.6l-7.9-6.1A24 24 0 0 0 0 24c0 3.9.9 7.5 2.6 10.7z"/><path fill="#34A853" d="M24 48c6.5 0 11.9-2.1 15.9-5.8l-7.4-5.7c-2.1 1.4-4.8 2.3-8.5 2.3-6.3 0-11.6-4.2-13.5-9.9l-7.9 6.1C6.6 42.6 14.6 48 24 48z"/></svg>',
 "drag": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8.5 6 2.5 12l6 6 1.4-1.4L5.3 12l4.6-4.6zm7 0-1.4 1.4 4.6 4.6-4.6 4.6 1.4 1.4 6-6z"/></svg>',
}
SVC_ICON = {
 "roof": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 1 12h3v8h6v-6h4v6h6v-8h3z"/></svg>',
 "seal": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2 4 5v6c0 5 3.4 9.7 8 11 4.6-1.3 8-6 8-11V5z"/></svg>',
 "drive": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18.9 6a1.5 1.5 0 0 0-1.4-1h-11a1.5 1.5 0 0 0-1.4 1L3 12v8a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-1h12v1a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-8zM6.5 16a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm11 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zM5 11l1.5-4.5h11L19 11z"/></svg>',
 "pool": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2 18c2 0 2-1 4-1s2 1 4 1 2-1 4-1 2 1 4 1 2-1 4-1v2c-2 0-2 1-4 1s-2-1-4-1-2 1-4 1-2-1-4-1-2 1-4 1zm0-4c2 0 2-1 4-1s2 1 4 1 2-1 4-1 2 1 4 1 2-1 4-1v2c-2 0-2 1-4 1s-2-1-4-1-2 1-4 1-2-1-4-1-2 1-4 1zM8 4h2v8H8zm6 0h2v8h-2z"/></svg>',
 "house": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 2 11h3v10h14V11h3zm0 5.5c1.3 1.8 2.5 3.3 2.5 4.5a2.5 2.5 0 0 1-5 0c0-1.2 1.2-2.7 2.5-4.5z"/></svg>',
 "window": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 3h18v18H3zm2 2v6h6V5zm8 0v6h6V5zm-8 8v6h6v-6zm8 0v6h6v-6z"/></svg>',
 "building": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21V3h12v6h6v12h-8v-4h-2v4zm3-15v2h2V6zm4 0v2h2V6zm-4 4v2h2v-2zm4 0v2h2v-2zm-4 4v2h2v-2zm4 0v2h2v-2zm6-2v2h2v-2zm0 4v2h2v-2z"/></svg>',
 "sparkle": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.2 6.3L20 10l-5.8 1.7L12 18l-2.2-6.3L4 10l5.8-1.7zm7 12 1 2.6 2.5.9-2.5.9-1 2.6-1-2.6-2.5-.9 2.5-.9z"/></svg>',
}
SERVICES = [
 ("roof", "Roof Soft Wash", "Safe, low-pressure roof cleaning that removes stains without damage.", ["Removes algae and mold", "Safe for all roof types", "Low-pressure application"]),
 ("seal", "Seal Coating", "Protective coating that extends surface life and appearance.", ["Protects from wear", "Enhances durability", "Clean, dark finish"]),
 ("drive", "Driveway & Sidewalk Cleaning", "Deep cleaning that restores concrete surfaces and curb appeal.", ["Removes dirt and stains", "Brightens concrete", "Safe and effective"]),
 ("pool", "Pool Deck & Fence Cleaning", "Cleaning that keeps outdoor areas safe and clean.", ["Removes slippery buildup", "Safe for surfaces", "Improves appearance"]),
 ("house", "House Wash", "Exterior house washing that refreshes your home safely.", ["Removes mold and grime", "Safe for siding and stucco", "Even, clean finish"]),
 ("window", "Exterior Window Cleaning", "Streak-free exterior window cleaning for clear views.", ["Frames and sills included", "High-reach equipment", "Spotless results"]),
 ("building", "Commercial Building Cleaning", "Professional exterior cleaning for commercial properties.", ["HOAs and businesses", "High-traffic areas", "Reliable service"]),
 ("sparkle", "Interior Window Cleaning", "Careful interior window cleaning with no mess.", ["Smudge-free glass", "Frames and tracks cleaned", "Home-safe service"]),
]
WORK = [  # slug, title, service
 ("roof-tile", "Barrel Tile Roof", "Roof Soft Wash"),
 ("pool-deck", "Pool Deck Pavers", "Pool Deck Cleaning"),
 ("fence", "Vinyl Privacy Fence", "Fence Cleaning"),
 ("roof-ridge", "Flat Tile Roof", "Roof Soft Wash"),
 ("backyard", "Backyard Patio", "Concrete Cleaning"),
 ("patio-tile", "Terracotta Patio", "Patio Cleaning"),
 ("pool-walkway", "Pool Walkway", "Concrete Cleaning"),
 ("tennis-court", "Tennis Court", "Court Cleaning"),
]
REVIEWS = [
 ("James R.", "Our driveway and sidewalks look brand new again. Incredible difference after just one visit."),
 ("Andrew S.", "Very professional service. The crew was on time, careful, and left our windows spotless inside and out."),
 ("Rachel", "Amazing service from start to finish. Our windows have never looked this clean. Professional, fast, and very respectful of our home."),
 ("Daniel K.", "The house exterior looks spotless. Great attention to detail and very efficient work."),
 ("Brian M.", "Fast, reliable, and excellent results. You can clearly see the difference."),
 ("John P.", "Excellent service and spotless results. Our windows have never looked better."),
 ("Michael T.", "They cleaned our driveway, walls, and fence. Everything looks fresh and clean again."),
 ("Mark L.", "Our interior and exterior windows look amazing. The difference is night and day."),
 ("Megan C.", "Clean windows, no streaks, no mess. Exactly what we expected and more."),
]
AREAS = ["Boca Raton", "Coral Springs", "Davie", "Fort Lauderdale", "Hollywood", "Miami", "Miramar", "Parkland", "Pembroke Pines", "Plantation", "Pompano Beach", "Sunrise", "Weston"]
NAV = [("index.html", "Home"), ("services.html", "Services"), ("our-work.html", "Before & After"), ("index.html#reviews", "Reviews"), ("quote.html", "Contact")]

# Preview mode: shows a "design preview" banner on every page and asks search engines not to index it.
# Set PREVIEW = False (then run `python build.py`) when the site launches on the owner's domain.
PREVIEW = True
PREVIEW_META = '\n<meta name="robots" content="noindex, nofollow">' if PREVIEW else ""
PREVIEW_BANNER = ('\n<div class="preview-banner" role="note"><strong>Design preview</strong>'
                  '<span>Concept redesign of drpressureservices.com. Not the official Dr. Pressure website.</span></div>') if PREVIEW else ""
PREVIEW_FOOTER = ' <span class="preview-note">Design preview: not the official website.</span>' if PREVIEW else ""

def quote_btn(cls="", label="Get a Quote"):
    return f'<a class="btn btn--quote {cls}" href="quote.html">{label}</a>'

def head(title, desc, page):
    cur = ' aria-current="page"'
    nav = "".join(f'<a href="{h}"{cur if h == page else ""}>{t}</a>' for h, t in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">{PREVIEW_META}
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css?v=15">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>{PREVIEW_BANNER}
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="index.html"><img src="assets/img/logo.png" width="640" height="253" alt="Dr. Pressure Cleaning Services LLC: Bringing your property back to life"></a>
    <nav class="nav" aria-label="Main">{nav}</nav>
    <div class="header-actions">
      <a class="header-phone" href="tel:{PHONE}">{I["phone"]}{PHONE_TXT}</a>
      {quote_btn()}
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu">{I["menu"]}</button>
    </div>
  </div>
  <nav class="mobile-nav" id="mobile-nav" aria-label="Mobile">{nav}<a href="tel:{PHONE}">Call {PHONE_TXT}</a></nav>
</header>
<main id="main">
'''

def quote_band(h="Ready for a cleaner property?", p="Get your free quote in 60 seconds. Lasting results, or we come back for free."):
    return f'''<section class="quote-band" aria-label="Get a quote">
  <div class="container quote-band-inner">
    <div><h2>{h}</h2><p>{p}</p></div>
    <div class="quote-band-actions">{quote_btn("btn--lg", "Get My Free Quote")}<a class="btn btn--ghost btn--lg" href="tel:{PHONE}">{I["phone"]}Call Now</a></div>
  </div>
</section>
'''

def foot():
    links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f'''</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="footer-logo" href="index.html"><img src="assets/img/logo.png" width="640" height="253" alt="Dr. Pressure Cleaning Services LLC" loading="lazy"></a>
        <p>Professional exterior cleaning services across South Florida. We guarantee lasting results, or we come back for free.</p>
        <div class="social">
          <a href="{IG}" aria-label="Instagram" target="_blank" rel="noopener">{I["ig"]}</a>
          <a href="{FB}" aria-label="Facebook" target="_blank" rel="noopener">{I["fb"]}</a>
        </div>
      </div>
      <div><h3>Explore</h3><ul>{links}<li><a href="quote.html">Get a Quote</a></li></ul></div>
      <div class="footer-contact"><h3>Contact</h3><ul>
        <li><a href="tel:{PHONE}">{I["phone"]}{PHONE_TXT}</a></li>
        <li><a href="mailto:{EMAIL}">{I["mail"]}{EMAIL}</a></li>
        <li><a href="{GMAPS}" target="_blank" rel="noopener">{I["pin"]}{AREA_LABEL}</a></li>
      </ul>
      <p style="margin-top:18px">{quote_btn()}</p></div>
    </div>
    <div class="footer-bottom">&copy; <span data-year>2026</span> Dr. Pressure Cleaning Services LLC. All rights reserved.{PREVIEW_FOOTER}</div>
  </div>
</footer>
<div class="quote-bar" aria-label="Quick contact">
  <a class="btn btn--ghost" href="tel:{PHONE}">{I["phone"]}Call</a>
  {quote_btn()}
</div>
<script src="js/main.js?v=2" defer></script>
</body>
</html>
'''

def ba(slug, title, svc, lazy=True):
    ld = ' loading="lazy"' if lazy else ""
    return f'''<figure class="ba-card">
  <div class="ba" data-ba>
    <img class="ba-after" src="assets/img/work/{slug}-after.jpg" alt="{title} after cleaning by Dr. Pressure"{ld}>
    <img class="ba-before" src="assets/img/work/{slug}-before.jpg" alt="{title} before cleaning"{ld}>
    <span class="ba-tag ba-tag--before">Before</span><span class="ba-tag ba-tag--after">After</span>
    <span class="ba-line"></span>
    <input type="range" min="0" max="100" value="50" aria-label="Drag to compare before and after: {title}">
    <span class="ba-handle">{I["drag"]}</span>
  </div>
  <figcaption>{title}<span>{svc}</span></figcaption>
</figure>'''

def service_tiles(with_desc=False):
    """Simple service tiles: icon + name (+ one-line description on the Services page)."""
    out = []
    for ic, name, desc, pts in SERVICES:
        d = f"<p>{desc}</p>" if with_desc else ""
        inc = "".join(f"<li>{p}</li>" for p in pts)
        out.append(f'<li class="svc-tile"><span class="service-icon">{SVC_ICON[ic]}</span><div><h3>{name}</h3>{d}<ul class="svc-inc" aria-label="Included">{inc}</ul></div></li>')
    cls = "svc-tiles svc-tiles--desc" if with_desc else "svc-tiles"
    return f'<ul class="{cls}">{"".join(out)}</ul>'

FEATURED_REVIEWS = [REVIEWS[0], REVIEWS[1], REVIEWS[3]]

def reviews_html():
    items = "".join(f'<figure class="review"><span class="stars" aria-label="5 out of 5 stars">★★★★★</span><blockquote>&ldquo;{t}&rdquo;</blockquote><figcaption>{n}</figcaption></figure>' for n, t in FEATURED_REVIEWS)
    return f'''<section class="section section--alt section--tight" id="reviews">
  <div class="container">
    <h2 class="reviews-title">What customers say</h2>
    <div class="reviews-summary"><strong>5.0</strong><span class="stars" aria-hidden="true">★★★★★</span><span>from our customers on <a href="{GMAPS}" target="_blank" rel="noopener">Google</a></span></div>
    <div class="reviews">{items}</div>
  </div>
</section>
'''

MAIN_CITY = "Fort Lauderdale"
STATE = "FL"
AREA_LABEL = f"{MAIN_CITY}, {STATE} &amp; surrounding areas"

def areas_html():
    cities = [a for a in AREAS if a != MAIN_CITY]
    # keep each separator on the same line as the city before it, so no line starts with a dot
    nearby = " ".join(f'<span class="nowrap">{a}{"&nbsp;&middot;" if i < len(cities) - 1 else ""}</span>' for i, a in enumerate(cities))
    return f'''<section class="section section--tight" id="areas">
  <div class="container areas-block">
    <span class="eyebrow">Service area</span>
    <h2 class="areas-main">{I["pin"]}{MAIN_CITY}, {STATE}</h2>
    <p class="areas-sub">&amp; surrounding areas</p>
    <p class="areas-list">{nearby}</p>
    <p class="areas-note">Don&rsquo;t see your city? Call us. We likely cover it.</p>
  </div>
</section>
'''

STEPS = [
 ("Submit the form", "Fill out our quick service form with a few details about your property. This helps us prepare before we reach out."),
 ("Confirmation & estimate", "We review your request, confirm the details, and provide an estimate. If needed, we&rsquo;ll reach out to clarify or schedule."),
 ("We do the job", "Our team shows up on time, completes the job professionally, and treats your property with care from start to finish."),
 ("Results & follow-up", "After the job, you receive before &amp; after photos and a final update, so you know exactly what was done."),
]

# ---------- index ----------
idx = head("Dr. Pressure | Pressure Washing & Exterior Cleaning in South Florida",
           "Roof soft washing, driveways, pool decks, house washing and window cleaning across South Florida. 5.0 Google rating. Get your free quote in 60 seconds.", "index.html")
idx += f'''<section class="hero">
  <div class="container hero-grid">
  <div class="hero-inner">
    <a class="rating-badge" href="{GMAPS}" target="_blank" rel="noopener"><span class="g">{I["g"]}</span><span>5.0 <span class="stars" aria-hidden="true">★★★★★</span> Google rating</span></a>
    <h1>Bringing your property <span>back to life</span></h1>
    <p class="hero-lead">Professional exterior cleaning in South Florida. We guarantee lasting results, or we come back for free.</p>
    <div class="hero-actions">{quote_btn("btn--lg", "Get a Free Quote")}<a class="btn btn--ghost btn--lg" href="tel:{PHONE}">{I["phone"]}{PHONE_TXT}</a></div>
    <ul class="hero-points"><li>{I["check"]}Quote in 60 seconds</li><li>{I["check"]}Before &amp; after photos of every job</li><li>{I["check"]}Satisfaction guarantee</li></ul>
  </div>
  <figure class="hero-photo"><img src="assets/img/hero-pressure-washing.jpg" width="1400" height="1488" alt="Young man in a yellow rain jacket pressure washing house siding" fetchpriority="high"></figure>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Real results</span><h2>See the difference</h2><p>Drag the slider on any photo to compare before and after.</p></div>
    <div class="ba-grid ba-grid--3">
{ba(*WORK[0], lazy=False)}
{ba(*WORK[1], lazy=False)}
{ba(*WORK[2])}
    </div>
    <div class="center-cta"><a class="btn btn--quote" href="our-work.html">See all our work {I["arrow"]}</a></div>
  </div>
</section>

<section class="section section--alt" id="services">
  <div class="container">
    <div class="section-head"><span class="eyebrow">Services</span><h2>What we clean</h2><p>Homes, HOAs and businesses. One call handles it all.</p></div>
    {service_tiles()}
    <div class="center-cta"><a class="btn btn--quote" href="services.html">View services {I["arrow"]}</a></div>
  </div>
</section>

<section class="section" id="process">
  <div class="container">
    <div class="section-head"><span class="eyebrow">How it works</span><h2>Four simple steps</h2></div>
    <ol class="steps">{"".join(f"<li class='step'><h3>{t}</h3><p>{d}</p></li>" for t, d in STEPS)}</ol>
    <div class="center-cta">{quote_btn("btn--lg", "Start Step 1: Get a Quote")}</div>
  </div>
</section>
''' + reviews_html() + areas_html() + quote_band() + foot()

# ---------- services ----------
svc = head("Services | Dr. Pressure Cleaning Services", "Roof soft wash, seal coating, driveway, pool deck, fence, house wash, window and commercial cleaning in South Florida.", "services.html")
svc += f'''<section class="page-hero"><div class="container"><span class="eyebrow">Services</span><h1>What we clean</h1><p>Safe, professional exterior cleaning for homes, HOAs and businesses across South Florida.</p>{quote_btn("btn--lg", "Get a Free Quote")}</div></section>
<section class="section section--alt"><div class="container">
{service_tiles(with_desc=True)}
</div></section>
<section class="section"><div class="container">
  <div class="section-head"><span class="eyebrow">Real results</span><h2>Before &amp; after</h2></div>
  <div class="ba-grid ba-grid--3">{ba(*WORK[3])}{ba(*WORK[4])}{ba(*WORK[5])}</div>
  <div class="center-cta"><a class="btn btn--quote" href="our-work.html">See all our work {I["arrow"]}</a></div>
</div></section>
''' + quote_band("Not sure which service you need?", "Send us a few details and photos. We&rsquo;ll recommend the right clean and give you a quote.") + foot()

# ---------- our work ----------
wk = head("Before & After | Dr. Pressure Cleaning Services", "Before and after photos of roof, pool deck, fence, patio and concrete cleaning by Dr. Pressure in South Florida.", "our-work.html")
wk += f'''<section class="page-hero"><div class="container"><span class="eyebrow">Our work</span><h1>Before &amp; after</h1><p>Real jobs from our team. Drag the slider on each photo to see the difference.</p>{quote_btn("btn--lg", "Get a Free Quote")}</div></section>
<section class="section"><div class="container"><div class="ba-grid ba-grid--3">
{"".join(ba(*w, lazy=i > 2) for i, w in enumerate(WORK))}
</div></div></section>
''' + quote_band("Want results like these?", "Get your free quote in 60 seconds.") + foot()

# ---------- quote ----------
qt = head("Get a Free Quote | Dr. Pressure Cleaning Services", "Request a free pressure washing or exterior cleaning quote from Dr. Pressure. Takes about 60 seconds.", "quote.html")
qt += f'''<section class="page-hero"><div class="container"><span class="eyebrow">Free quote</span><h1>Get your quote</h1><p>Takes about 60 seconds. We&rsquo;ll review your request and get back to you with an estimate.</p></div></section>
<section class="section section--alt"><div class="container quote-layout">
  <div class="quote-form-card">
    <iframe data-tally-src="https://tally.so/embed/RGGEVv?alignLeft=1&amp;hideTitle=1&amp;transparentBackground=1&amp;dynamicHeight=1" src="https://tally.so/embed/RGGEVv?alignLeft=1&amp;hideTitle=1&amp;transparentBackground=1" loading="lazy" title="Dr. Pressure quote request form"></iframe>
    <p style="margin:12px 0 0;font-size:.92rem;color:var(--muted)">Form not loading? <a href="https://tally.so/r/RGGEVv" target="_blank" rel="noopener">Open the quote form in a new tab</a>.</p>
  </div>
  <aside class="quote-side">
    <div class="contact-card"><h2>Prefer to talk?</h2>
      <a href="tel:{PHONE}">{I["phone"]}{PHONE_TXT}</a>
      <a href="mailto:{EMAIL}">{I["mail"]}{EMAIL}</a>
      <a href="{IG}" target="_blank" rel="noopener"><svg class="icon" viewBox="0 0 24 24" aria-hidden="true">{I["ig"][I["ig"].index("<path"):I["ig"].index("</svg>")]}</svg>Instagram</a>
      <a href="{FB}" target="_blank" rel="noopener"><svg class="icon" viewBox="0 0 24 24" aria-hidden="true">{I["fb"][I["fb"].index("<path"):I["fb"].index("</svg>")]}</svg>Facebook</a>
    </div>
    <div class="guarantee"><h3>Our guarantee</h3><p>We guarantee lasting results, or we come back for free.</p></div>
    <div class="guarantee"><h3>What happens next</h3><p>We confirm the details, send your estimate, and schedule a time that works for you. After the job you get before &amp; after photos.</p></div>
  </aside>
</div></section>
''' + areas_html() + quote_band("Questions before you book?", "Call or text us and we&rsquo;ll help you out.") + foot()
qt = qt.replace('<script src="js/main.js?v=2" defer></script>', '<script src="js/main.js" defer></script>\n<script async src="https://tally.so/widgets/embed.js"></script>')

for name, html in [("index.html", idx), ("services.html", svc), ("our-work.html", wk), ("quote.html", qt)]:
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(html)
print("ok")
