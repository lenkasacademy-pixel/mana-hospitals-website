"""
Mana Hospitals — SEO / AEO helpers used by build.py.

One source of truth for NAP (name, address, phone), geo, areas served and the
schema.org graph, so every page tells Google and answer engines the same story.
"""
import json, html as _html

SITE = "https://wecaremana.com"
HOSPITAL_ID = SITE + "/#hospital"
WEBSITE_ID = SITE + "/#website"

NAME = "Mana Hospitals"
LEGAL = "Wecare Lifeline Healthcare Pvt. Ltd."
TELUGU = "మన హాస్పిటల్స్"
STREET = "Plot No. 219, beside SBI Bank, Mahadevapuram Colony, Gajularamaram"
LOCALITY = "Hyderabad"
POSTCODE = "500055"           # client's address; Google listing shows 500072 — needs reconciling
REGION = "Telangana"
LAT, LNG = 17.5166458, 78.4144235
PHONE_E164 = "+917995895858"
PHONE_SCHEMA = "+91-79958-95858"
EMERG_SCHEMA = "+91-99669-94859"
EMAIL = "info@wecaremana.com"
MAPS_CID = "https://maps.google.com/?cid=3478330352746109876"
MAPS_SHARE = "https://share.google/QCrYoUiRkgj39kQA7"

# Neighbourhoods within the hospital's natural catchment (north-west Hyderabad / Medchal-Malkajgiri)
AREAS = ["Gajularamaram", "Mahadevapuram Colony", "Jeedimetla", "Quthbullapur", "Shapur Nagar",
         "Chintal", "Suraram", "Jagathgiri Gutta", "Kukatpally", "Nizampet", "Bachupally",
         "Pragathi Nagar", "Kompally", "Dundigal", "Bowrampet", "Gandimaisamma"]


def esc(s):
    return _html.escape(_html.unescape(s), quote=True)


def plain(s):
    return _html.unescape(s).replace("<i>", "").replace("</i>", "")


def postal():
    return {"@type": "PostalAddress", "streetAddress": STREET, "addressLocality": LOCALITY,
            "addressRegion": REGION, "postalCode": POSTCODE, "addressCountry": "IN"}


def geo():
    return {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LNG}


def hospital_node(specialities, doctors_count):
    """The full Hospital entity. Emitted on every page with the same @id."""
    return {
        "@type": ["Hospital", "MedicalOrganization"],
        "@id": HOSPITAL_ID,
        "name": NAME,
        "alternateName": [NAME + " Gajularamaram", TELUGU, "Mana Hospital", LEGAL],
        "legalName": LEGAL,
        "url": SITE + "/",
        "logo": {"@type": "ImageObject", "url": SITE + "/assets/logo.png", "width": 895, "height": 181},
        "image": [SITE + "/assets/img/building.jpg", SITE + "/assets/cine/poster.webp"],
        "description": (f"{NAME} is a multispeciality hospital in Gajularamaram, Hyderabad with "
                        f"{doctors_count} specialist consultants, 24×7 emergency, ICU and NICU, in-house "
                        "diagnostics, dialysis and pharmacy, and cashless insurance support."),
        "telephone": PHONE_SCHEMA,
        "email": EMAIL,
        "address": postal(),
        "geo": geo(),
        "hasMap": MAPS_CID,
        "sameAs": [MAPS_CID],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00", "closes": "23:59"}],
        "contactPoint": [
            {"@type": "ContactPoint", "telephone": PHONE_SCHEMA, "contactType": "customer service",
             "areaServed": "IN", "availableLanguage": ["English", "Telugu", "Hindi"]},
            {"@type": "ContactPoint", "telephone": EMERG_SCHEMA, "contactType": "emergency",
             "areaServed": "IN", "availableLanguage": ["English", "Telugu", "Hindi"]}],
        "areaServed": [{"@type": "Place", "name": a + ", Hyderabad"} for a in AREAS],
        "medicalSpecialty": sorted({s["specialty"] for s in specialities}),
        "department": [dept_node(s) for s in specialities],
        "priceRange": "₹₹",
        "currenciesAccepted": "INR",
    }


def dept_node(s):
    """A department as a complete local business (Google wants NAP + image + priceRange on each)."""
    return {"@type": "MedicalClinic", "@id": f'{SITE}/{s["slug"]}.html#department',
            "name": f'{plain(s["title"])} — {NAME} Gajularamaram', "url": f'{SITE}/{s["slug"]}.html',
            "medicalSpecialty": s["specialty"], "parentOrganization": {"@id": HOSPITAL_ID},
            "address": postal(), "geo": geo(), "telephone": PHONE_SCHEMA,
            "image": SITE + "/assets/img/building.jpg", "priceRange": "₹₹",
            "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                "opens": "00:00", "closes": "23:59"}]}


def website_node():
    return {"@type": "WebSite", "@id": WEBSITE_ID, "url": SITE + "/", "name": NAME,
            "inLanguage": "en-IN", "publisher": {"@id": HOSPITAL_ID}}


def webpage_node(slug, title, desc, kind="WebPage", about=None, image=None, speakable=False):
    url = f"{SITE}/{slug}"
    n = {"@type": kind, "@id": url + "#webpage", "url": url, "name": plain(title),
         "description": plain(desc), "inLanguage": "en-IN",
         "isPartOf": {"@id": WEBSITE_ID}, "publisher": {"@id": HOSPITAL_ID},
         "breadcrumb": {"@id": url + "#breadcrumb"}, "lastReviewed": "2026-11-18"}
    if about:
        n["about"] = about
    if image:
        n["primaryImageOfPage"] = {"@type": "ImageObject", "url": image}
    if speakable:
        n["speakable"] = {"@type": "SpeakableSpecification", "cssSelector": [".aeo-answer", "h1"]}
    return n


def breadcrumb_node(slug, crumbs):
    """crumbs: [(name, path)] after Home; last item may have path=None (= this page)."""
    url = f"{SITE}/{slug}"
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    for i, (name, path) in enumerate(crumbs, start=2):
        items.append({"@type": "ListItem", "position": i, "name": plain(name),
                      "item": f"{SITE}/{path}" if path else url})
    return {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": items}


def faq_node(slug, items):
    url = f"{SITE}/{slug}"
    return {"@type": "FAQPage", "@id": url + "#faq", "isPartOf": {"@id": url + "#webpage"},
            "mainEntity": [{"@type": "Question", "name": plain(q),
                            "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in items]}


def graph(*nodes):
    data = {"@context": "https://schema.org", "@graph": [n for n in nodes if n]}
    return ('<script type="application/ld+json">\n'
            + json.dumps(data, ensure_ascii=False, separators=(",", ":"))
            + "\n</script>")


def head_meta(*, slug, title, desc, image=None, kind="website"):
    """Extra <head> tags: robots, social cards, locale, geo."""
    img = image or (SITE + "/assets/img/building.jpg")
    url = f"{SITE}/{slug}"
    return f"""<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta property="og:site_name" content="{NAME}">
<meta property="og:locale" content="en_IN">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="{kind}">
<meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{img}">
<meta name="geo.region" content="IN-TG">
<meta name="geo.placename" content="Gajularamaram, Hyderabad">
<meta name="geo.position" content="{LAT};{LNG}">
<meta name="ICBM" content="{LAT}, {LNG}">
<link rel="icon" href="assets/icons/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="assets/icons/icon-192.png" sizes="192x192" type="image/png">
<link rel="apple-touch-icon" href="assets/icons/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">"""


# Old WordPress URLs (from wecaremana.com/page-sitemap.xml, 18 Nov 2026) → new pages.
# Each becomes /<old>/index.html with a canonical + instant redirect, so existing rankings carry over
# once the domain points at this site.
REDIRECTS = {
    "about": "about.html",
    "home": "",
    "book-appointment": "book-appointment.html",
    "contact": "contact.html",
    "contact-mana-hospitals-gajularamaram": "contact.html",
    "doctors": "doctors.html",
    "our-doctors": "doctors.html",
    "our-specialist-doctors": "doctors.html",
    "best-gastro-and-surgical-gastro-near-me": "gastroenterology.html",
    "gastroenterology-surgical-gastro-gajularamaram": "gastroenterology.html",
    "best-general-medicine-in-gajularamaram": "general-medicine.html",
    "best-general-physician-in-gajularamaram": "general-medicine.html",
    "best-gynecologist-womens-health-expertnear-you": "gynaecology.html",
    "obstetrics-gynecology-gajularamaram": "gynaecology.html",
    "best-orthopedic-surgeons-near-you": "orthopaedics.html",
    "orthopedics-joint-replacement-gajularamaram": "orthopaedics.html",
    "knee-replacement": "orthopaedics.html",
    "best-piles-surgery-in-hyderabad": "piles-fissure-fistula.html",
    "best-pulmonologist-in-gajularamaram": "pulmonology.html",
    "pulmonology-gajularamaram": "pulmonology.html",
    "nephrology-dialysis-gajularamaram": "nephrology.html",
    "neurology-gajularamaram": "neurology.html",
    "urology-gajularamaram": "urology.html",
    "radiofrequency-ablation-rfa": "specialities.html",
    "dr-bagam-mahesh": "dr-bagam-mahesh.html",
    "dr-g-srujana": "dr-guntaka-srujana.html",
    "dr-juluri-vamshi-krishna": "dr-juluri-vamshi-krishna.html",
    "dr-shivaiahgari-vinaykumar": "dr-shivaiahgari-vinaykumar.html",
    "shivaiahgari-vinay-kumar": "dr-shivaiahgari-vinaykumar.html",
    "dr-swaroop-chandra": "dr-swaroop-chandra.html",
    "kosuri-akhila": "dr-kosuri-akhila.html",
    "p-alekya": "dr-alekhya-patluri.html",
    "rama-krishna-reddy": "dr-ramakrishna-reddy-m.html",
    "sasikanth-reddy-p": "dr-sasikanth-reddy-p.html",
    "v-harika": "dr-vidyala-harika.html",
    "rahul-gunde": "doctors.html",              # not on the current consultant list — confirm with client
    "sujeeth-kumar-reddy-k": "doctors.html",    # not on the current consultant list — confirm with client
}


def redirect_page(target):
    url = f"{SITE}/{target}"
    return f"""<!DOCTYPE html>
<html lang="en-IN"><head><meta charset="utf-8">
<title>Moved — {NAME}</title>
<link rel="canonical" href="{url}">
<meta name="robots" content="noindex,follow">
<meta http-equiv="refresh" content="0; url=../{target}">
<script>location.replace('../{target}'+location.hash)</script>
</head><body><p>This page has moved to <a href="../{target}">{url}</a>.</p></body></html>
"""
