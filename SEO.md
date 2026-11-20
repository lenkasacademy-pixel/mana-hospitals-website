# Mana Hospitals — SEO & AEO plan (Gajularamaram)

Goal: rank #1–3 in Google's local results and AI answers for "<speciality> in/near Gajularamaram"
(and the surrounding areas) for every department that has a consultant.

## What's built into the site (done)

| Area | What | Where |
|---|---|---|
| Speciality pages | 16 pages — one per speciality with a consultant (8 new: piles/fistula, general & laparoscopic surgery, paediatrics, 24×7 emergency & ICU, ENT, radiology, infertility, diabetes & thyroid) | `build.py`, `specialities_extra.py` |
| Doctor pages | 18 profile pages with photo, qualifications, departments, booking | `build.py` → `dr-*.html` |
| Titles & descriptions | Keyword-first, "Gajularamaram" in every title, ≤66 / ≤160 chars, all unique | `build.py` (`fit_title`, `fit_desc`) |
| Structured data | One schema.org graph per page: `Hospital` (NAP, geo, 24×7 hours, emergency contact, 16 areas served, departments), `WebSite`, page type (`MedicalWebPage`, `ProfilePage`, `CollectionPage`…), `BreadcrumbList`, `FAQPage`, `MedicalClinic` per department, `Physician` per doctor | `seo.py` |
| AEO | "At a glance" answer box + local FAQs on every speciality page, quick-facts block + 10 FAQs on the homepage, `speakable`, `llms.txt`, AI crawlers explicitly allowed in `robots.txt` | `build.py`, `seo.py` |
| Local signals | Exact map pin, Telugu name (మన హాస్పిటల్స్) as alternate name, areas-served copy, `geo.*` meta, consistent NAP in footer of every page | `seo.py` |
| Images | Descriptive alt text on every image (doctor name + speciality + Gajularamaram) | all pages |
| Old-URL redirects | 36 WordPress URLs → new pages (`/<old-slug>/index.html`), so existing rankings carry over | `seo.py` `REDIRECTS` |
| Technical | `sitemap.xml` (lastmod + image entries), `robots.txt`, `404.html`, favicon/app icons, web manifest, canonical URLs, Open Graph/Twitter cards, `lang="en-IN"`, preloaded hero image, versioned assets | `build.py` |

## Before go-live (must do)

1. **Point wecaremana.com at this site.** Add a `CNAME` file containing `wecaremana.com` and set the
   DNS (GitHub Pages A records / CNAME). All canonicals and schema already use `https://wecaremana.com/`.
2. **Keep the preview out of Google** until then — the github.io copy duplicates the content. Don't share
   the preview link publicly; once the domain is live, the github.io URL redirects to it automatically.
3. **Resolve NAP mismatches** (critical for local ranking):
   - Postcode: **500072** everywhere (matches the Google listing) — use the same on Practo, Justdial, etc.
   - Phones: appointments **79958 95858**, emergency **99669 94859** (matches the listing) — use the same
     numbers on Practo, Justdial, etc.
4. **Services confirmed (18 Nov 2026):** ENT surgery ✔, CT & MRI ✔, IVF ✘ (not offered — the infertility page
   says so and refers out). Never publish a service the hospital doesn't offer.
5. **Former doctors:** Dr. Rahul Gunde and Dr. Sujeeth Kumar Reddy K have left — their old URLs redirect to
   the doctors page.

## Google Business Profile (biggest local lever)

- Primary category **Hospital**; add secondary categories that match the pages: *Orthopedic surgeon,
  Gynecologist, Pediatrician, Proctologist, General surgeon, Diabetologist, Pulmonologist, ENT,
  Emergency care service, Diagnostic center, Fertility clinic, Dialysis center*.
- Website link → `https://wecaremana.com/`; add a **Services** list mirroring the 16 speciality pages,
  each with the page URL.
- Hours: 24 hours (emergency). Add special hours for festivals.
- Upload 30+ real photos (building, reception, OPD, ICU, theatre, doctors) — geo-tagged, named
  `mana-hospitals-gajularamaram-<what>.jpg`. Add 2–3 photos a week.
- Weekly **Posts** (health tips, camps, new doctor) linking to the matching speciality page.
- Seed the **Q&A** with the FAQs from the site (answer from the owner account).
- **Reviews:** target 15–20 new Google reviews per month. Ask at discharge via WhatsApp with the
  direct review link. Reply to every review within 48 h, mentioning the speciality and "Gajularamaram"
  naturally. Never offer incentives; never write reviews yourself.

## Citations & directories (same NAP, character for character)

Practo, Justdial, Lybrate, Sulekha, Credihealth, Bing Places, Apple Business Connect, Facebook page,
Instagram bio, IndiaMART healthcare, hospital associations / NABH listings, TPA hospital-network lists.
Each doctor: claim/create Practo and Google profiles linking to their `dr-*.html` page.

## Content plan (3–4 posts / month)

Local, answer-first articles that link to the speciality pages, e.g.
"Piles treatment cost in Hyderabad — what affects it", "Knee replacement recovery week by week",
"When is a fever an emergency for children?", "Dengue warning signs — Gajularamaram monsoon guide",
"Diabetes diet in Telugu homes". Add Telugu versions of the top pages (`/te/…` with `hreflang`) —
many local searches and voice queries are in Telugu.

## Off-page / links

Local news (Hans India, Deccan Chronicle, Telangana Today) on camps or new services; free health camps
with RWAs and schools in Jeedimetla, Quthbullapur, Kukatpally (ask for a link/mention); sponsor local
events; doctor guest articles; insurer/TPA network pages.

## Measure

- Google Search Console (domain property) — submit `sitemap.xml`; watch queries per speciality page.
- Google Business Profile insights — calls, direction requests, website clicks.
- Track 30 keywords weekly: "<speciality> in Gajularamaram", "<speciality> near me" (geo-gridded),
  "hospital in Gajularamaram", "24 hours hospital Jeedimetla", "piles doctor Kukatpally"…
- Check answer engines monthly: ask ChatGPT / Perplexity / Google AI Mode
  "best <speciality> hospital in Gajularamaram" and note whether Mana is cited.

## Mana Chat (website assistant + leads) — added 20 Nov 2026

- Floating chat on every page (`assets/chat.js`, `assets/chat.css`). Knowledge base `assets/chat-kb.js` is generated by
  `build.py` (`write_chat_kb`) from DOCTORS, SPECIALITIES, FAQs, insurers and contact details — rebuild after any data change.
- Understands symptoms in plain words ("knee pain", "sugar", "child fever", "piles bleeding"), doctor names, timings,
  location, insurance/insurer names, costs (never quotes prices), and routes emergencies (chest pain, accident…) straight
  to the emergency number. Answers the site FAQs (e.g. "do you do IVF?").
- **Contact gate (client, 20 Nov):** after the bot's first answer it asks for name → mobile (a question typed meanwhile is
  answered right after), sends that as an enquiry lead, then shows a big "Call now" card + WhatsApp; every later reply
  keeps a "📞 Call now" chip first. Emergencies skip the gate.
- Lead flow: patient name → mobile (Indian 10-digit check) → concern/department → when → consent → submit.
  Leads go to **WhatsApp (79958 95858) pre-filled** and, once set, to a **Google Sheet + email** via
  `tools/lead-collector.gs` (paste into Apps Script, deploy as web app, put the /exec URL in `CHAT_LEAD_ENDPOINT`).
- Ad attribution (UTM, gclid, fbclid, landing page, referrer) is stored with each lead. Fires `mana_chat_open`,
  `mana_chat_book_start`, `mana_chat_lead`, `mana_chat_whatsapp`, `mana_chat_emergency` to dataLayer / gtag, and a Meta
  `Lead` event if a pixel is installed.
- No AI service and no running cost; general information only, never a diagnosis.
