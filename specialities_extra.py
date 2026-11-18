"""
Speciality pages added for local search (Nov 2026): one page per speciality that has a consultant.
Same shape as SPECIALITIES in build.py, plus the SEO keys used everywhere:
  specialty — schema.org MedicalSpecialty value
  term      — what a patient searches for ("piles doctor", "paediatrician")
  seo_kw    — keyword-first page title stem
Claims are kept to what the hospital and its consultants already state. Confirmed by the client
18 Nov 2026: ENT surgery yes, CT & MRI yes, IVF not offered in-house.
"""

EXTRA_SPECIALITIES = [
    dict(
        slug="piles-fissure-fistula", nav="Piles, Fissure &amp; Fistula",
        title="Piles, Fissure &amp; Fistula (Proctology)",
        lines=["Piles, Fissure", "<i>&amp; Fistula care</i>"],
        specialty="Surgical", term="piles specialist", seo_kw="Piles &amp; Fistula Laser Treatment",
        lede="Bleeding, pain or a lump while passing stools? Our anorectal surgeons treat piles, fissures, "
             "fistulas and pilonidal sinus — with laser and minimally invasive options and quick recovery.",
        meta="Piles, fissure and fistula treatment in Gajularamaram, Hyderabad — laser and minimally invasive "
             "anorectal surgery by Dr. Naresh Kumar at Mana Hospitals. Call +91 79958 95858.",
        overview="Piles (haemorrhoids), anal fissures and fistulas are common and very treatable — yet many "
                 "people wait years out of embarrassment. Our proctology service, led by a laparoscopic and laser "
                 "anorectal surgeon, offers a private consultation, a clear diagnosis and the least invasive "
                 "treatment that will work, from diet and medicines to day-care laser procedures.",
        conditions=["Piles (haemorrhoids) — internal and external, all grades", "Anal fissure — acute and chronic",
                    "Fistula-in-ano", "Perianal abscess", "Pilonidal sinus",
                    "Rectal prolapse", "Bleeding or itching around the anus", "Constipation-related anal problems"],
        procedures=["Laser haemorrhoidoplasty for piles",  # surgeon's own title: "Laparoscopic Laser Anorectal Surgeon"
                    "Laser and minimally invasive fissure treatment",
                    "Fistula surgery, including sphincter-saving techniques",
                    "Abscess drainage", "Pilonidal sinus excision",
                    "Diet, stool-softener and sitz-bath programmes for early-stage disease"],
        when=["Bright red blood on the toilet paper or in the pan",
              "Pain, burning or a cut-like feeling while passing stools",
              "A lump or swelling near the anus, or discharge of pus",
              "Symptoms that keep returning despite creams and home remedies"],
        expect="The examination is short and done in private. Many early piles and fissures settle with "
               "medicines and diet changes. When a procedure is needed, laser and minimally invasive options "
               "usually mean less pain, minimal bleeding and a return to work within days.",
        doctors=["Dr. Naresh Kumar", "Dr. Mohammed Adil Faraz"],
        faqs=[("Is laser treatment for piles painful?",
               "Laser procedures are done under anaesthesia, so you feel nothing during treatment. Most people "
               "have much less pain afterwards than with traditional surgery and go home the same or next day."),
              ("Can piles be cured without surgery?",
               "Yes — early-grade piles often improve with a high-fibre diet, enough water, stool softeners and "
               "medicines. Surgery or laser is advised when bleeding, prolapse or pain persists."),
              ("Is a fissure the same as piles?",
               "No. A fissure is a small tear in the lining of the anus that causes sharp pain while passing "
               "stools; piles are swollen blood vessels that usually cause painless bleeding or a lump. "
               "The treatments are different, so a proper examination matters.")]),

    dict(
        slug="general-surgery", nav="General &amp; Laparoscopic Surgery",
        title="General &amp; Laparoscopic Surgery",
        lines=["General &amp;", "<i>Laparoscopic Surgery</i>"],
        specialty="Surgical", term="general surgeon", seo_kw="General &amp; Laparoscopic Surgeon",
        lede="Hernia, gallbladder stones, appendicitis, lumps and cysts — treated with keyhole (laparoscopic) "
             "surgery wherever possible, for smaller scars and a faster return home.",
        meta="General and laparoscopic surgeon in Gajularamaram, Hyderabad — hernia, gallbladder stones, "
             "appendix, lipoma and cyst surgery at Mana Hospitals. Call +91 79958 95858.",
        overview="Our general surgeons handle both planned operations and surgical emergencies. Laparoscopic "
                 "(keyhole) techniques are used whenever they are safe, which usually means less pain, smaller "
                 "scars and a shorter hospital stay — with the ICU and emergency department in the same building.",
        conditions=["Inguinal, umbilical and incisional hernia", "Gallbladder stones (cholelithiasis)",
                    "Appendicitis", "Lipoma, sebaceous cyst and other lumps", "Abscesses and wound infections",
                    "Breast lumps (evaluation)", "Diabetic foot and non-healing wounds", "Abdominal pain needing surgical review"],
        procedures=["Laparoscopic cholecystectomy (gallbladder removal)", "Laparoscopic appendectomy",
                    "Hernia repair — laparoscopic (TEP / TAPP) or open mesh repair",
                    "Excision of lumps, lipomas and cysts", "Incision and drainage of abscesses",
                    "Wound care and debridement"],
        when=["A bulge in the groin or around the navel that grows when you cough or strain",
              "Pain under the right ribs after meals, or a scan showing gallstones",
              "Sudden pain in the lower right abdomen with fever or vomiting — come to emergency",
              "Any new lump, or a wound that is not healing"],
        expect="Most planned laparoscopic operations need a short hospital stay. You will have a fitness "
               "check and anaesthesia review beforehand, and clear written instructions on diet, wound care "
               "and return to work afterwards.",
        doctors=["Dr. Mohammed Adil Faraz", "Dr. Naresh Kumar"],
        faqs=[("Is laparoscopic surgery better than open surgery?",
               "For many conditions — gallstones, appendix and many hernias — keyhole surgery means smaller "
               "cuts, less pain and quicker recovery. Your surgeon will advise which approach is safest for you."),
              ("How long is the hospital stay after gallbladder removal?",
               "After laparoscopic cholecystectomy most patients go home within a day or two and return to "
               "normal activity in about a week."),
              ("Does every hernia need surgery?",
               "Hernias do not heal on their own and can get stuck, so repair is usually recommended. "
               "The timing depends on symptoms and your overall health.")]),

    dict(
        slug="paediatrics", nav="Paediatrics &amp; Child Care",
        title="Paediatrics &amp; Child Care",
        lines=["Paediatrics", "<i>&amp; child care</i>"],
        specialty="Pediatric", term="paediatrician", seo_kw="Child Specialist &amp; Paediatrician",
        lede="Fevers, coughs, vaccinations, growth and nutrition — care for newborns, children and teenagers, "
             "with NICU support and 24×7 emergency in the same building.",
        meta="Child specialist and paediatrician in Gajularamaram, Hyderabad — vaccination, fever, growth, "
             "nutrition and newborn care with NICU support at Mana Hospitals. Call +91 79958 95858.",
        overview="Children are not small adults — they need doctors who understand how they grow, how illness "
                 "shows up differently in them, and how to put an anxious parent at ease. Our paediatricians "
                 "cover everyday illness, preventive care and nutrition, with the NICU and emergency team on site "
                 "for babies and children who need more.",
        conditions=["Fever, cold, cough and ear infections", "Diarrhoea, vomiting and dehydration",
                    "Asthma and wheezing in children", "Poor weight gain, growth and nutrition concerns",
                    "Newborn jaundice and feeding problems", "Allergies and skin rashes",
                    "Seizures with fever (febrile convulsions)", "Developmental milestones review"],
        procedures=["Vaccinations as per the national and IAP schedules", "Well-baby and growth check-ups",
                    "Nutrition and diet counselling",  # Dr. Vinaykumar: PGPN (Boston)
                    "Nebulisation and asthma care plans", "Newborn care with NICU support",
                    "In-house blood tests and imaging for children"],
        when=["A fever above 101°F lasting more than two days, or any fever in a baby under 3 months",
              "Fast or difficult breathing, or a child who is unusually drowsy — come to emergency",
              "Fewer wet nappies, refusal to feed, or repeated vomiting",
              "Concerns about weight, height, speech or development"],
        expect="Bring your child's vaccination card and any previous prescriptions. Most illnesses are "
               "assessed and treated at the same visit, with lab tests on site when needed.",
        doctors=["Dr. Shivaiahgari Vinaykumar", "Dr. G. Vaishnavi", "Dr. Ch. Divya"],
        faqs=[("When should I take my child to emergency?",
               "Come straight in for difficulty breathing, a seizure, severe dehydration, a very drowsy or "
               "floppy child, or any fever in a baby under three months. Our emergency department is open 24×7."),
              ("Do you give vaccinations?",
               "Yes. Our paediatricians follow the national and IAP immunisation schedules. Bring your child's "
               "vaccination card to every visit."),
              ("Is there a NICU at Mana Hospitals?",
               "Yes. Newborns who need extra care are supported by our NICU, alongside our obstetrics team.")]),

    dict(
        slug="emergency-critical-care", nav="24×7 Emergency &amp; ICU",
        title="24×7 Emergency &amp; Critical Care",
        lines=["24×7 Emergency", "<i>&amp; Critical Care</i>"],
        specialty="Emergency", term="emergency hospital", seo_kw="24×7 Emergency Hospital &amp; ICU",
        lede="Accidents, chest pain, breathlessness, stroke, poisoning or high fever — our emergency department, "
             "ICU and NICU are staffed around the clock, every day of the year.",
        meta="24×7 emergency hospital and ICU in Gajularamaram, Hyderabad — trauma, chest pain, stroke, "
             "breathlessness and critical care at Mana Hospitals. Emergency: +91 99669 94859.",
        overview="In an emergency, minutes matter and so does distance. Our emergency department in "
                 "Gajularamaram is open 24 hours with an intensivist-led ICU behind it, on-call consultants "
                 "across specialities, and lab, imaging and pharmacy in the same building — so treatment starts "
                 "on arrival, not after a transfer.",
        conditions=["Road traffic accidents, falls and fractures", "Chest pain and suspected heart attack",
                    "Stroke — sudden weakness, facial droop or slurred speech", "Severe breathlessness and asthma attacks",
                    "Poisoning, snake and dog bites", "High fever, dengue and severe infections",
                    "Seizures and loss of consciousness", "Severe abdominal pain, vomiting and dehydration"],
        procedures=["24×7 triage and resuscitation", "Intensive care (ICU) with continuous monitoring",
                    "Ventilator and non-invasive breathing support", "NICU for newborns",
                    "Emergency lab and imaging", "Emergency dialysis support"],
        when=["Chest pain, breathlessness, fainting or sudden weakness — call immediately",
              "Any serious injury, heavy bleeding or a suspected fracture",
              "Poisoning, a bite, or a seizure",
              "A child or elderly person who is suddenly very unwell"],
        expect="Call ahead on the emergency number so the team is ready when you arrive. Bring any regular "
               "medicines and previous reports if you can — but do not delay coming in to find them.",
        doctors=["Dr. Juluri Vamshi Krishna"],
        faqs=[("Is Mana Hospitals emergency open at night?",
               "Yes. The emergency department, ICU and NICU are open 24 hours a day, 7 days a week, "
               "including Sundays and holidays."),
              ("What is the emergency number?",
               "Call +91 99669 94859 for emergencies, or the hospital on +91 79958 95858. Calling ahead lets "
               "the team prepare before you arrive."),
              ("Is cashless insurance accepted in an emergency?",
               "Yes. Treatment starts first; our insurance desk then raises pre-authorisation with your insurer "
               "or TPA for cashless treatment.")]),

    dict(
        slug="ent", nav="ENT (Ear, Nose &amp; Throat)",
        title="ENT — Ear, Nose &amp; Throat",
        lines=["ENT —", "<i>ear, nose &amp; throat</i>"],
        specialty="Otolaryngologic", term="ENT doctor", seo_kw="ENT Doctor (Ear, Nose &amp; Throat)",
        lede="Ear pain, hearing problems, sinusitis, tonsils, snoring and voice problems — diagnosed and treated, "
             "including ENT surgery, by an ENT surgeon for adults and children.",
        meta="ENT doctor in Gajularamaram, Hyderabad — ear, nose and throat problems, sinus, tonsil and ear "
             "surgery by Dr. Manisha M at Mana Hospitals. Call +91 79958 95858.",
        overview="Ear, nose and throat problems affect sleep, hearing, speech and breathing — and in children "
                 "they can affect learning too. Our ENT surgeon examines, diagnoses and treats these conditions "
                 "with medicines or procedures as needed, for children and adults alike.",
        conditions=["Ear infections, ear discharge and ear pain", "Hearing loss and ear wax",
                    "Sinusitis and blocked nose", "Tonsillitis and adenoids", "Allergic rhinitis",
                    "Nose bleeds", "Vertigo and giddiness", "Hoarseness and voice problems"],
        procedures=["ENT examination and endoscopy", "Ear wax removal and ear toilet",
                    "Treatment plans for sinusitis and allergy",
                    "Tonsil and adenoid surgery (tonsillectomy, adenoidectomy)",
                    "Nose and sinus surgery — septoplasty, endoscopic sinus surgery, nasal polyps",
                    "Ear surgery — ear drum repair and other ear procedures",
                    "Hearing assessment referral and follow-up"],
        when=["Ear pain or discharge, especially in a child",
              "Reduced hearing, ringing in the ears or giddiness",
              "A blocked nose or sinus pain for more than two weeks",
              "Repeated sore throats, loud snoring, or a voice change that lasts more than three weeks"],
        expect="Most ENT problems are diagnosed at the first visit with a careful examination. Bring any "
               "previous reports or scans; treatment usually starts the same day.",
        doctors=["Dr. Manisha M"],
        faqs=[("When should tonsils be removed?",
               "Tonsil removal is considered for frequent, severe tonsillitis, breathing or sleep problems, or "
               "complications such as an abscess. Many children are managed with medicines alone."),
              ("Can sinusitis be treated without surgery?",
               "Most sinusitis settles with medicines, nasal sprays and steam. Surgery is considered only for "
               "chronic or complicated cases."),
              ("Is it safe to clean ear wax with buds?",
               "Cotton buds can push wax deeper and injure the ear. If wax is blocking hearing, an ENT doctor "
               "can remove it safely.")]),

    dict(
        slug="radiology-diagnostics", nav="Radiology &amp; Diagnostics",
        title="Radiology &amp; Diagnostics",
        lines=["Radiology", "<i>&amp; diagnostics</i>"],
        specialty="Radiography", term="diagnostic centre", seo_kw="CT, MRI &amp; Ultrasound Scans",
        lede="CT, MRI, ultrasound, X-ray, Doppler and laboratory tests in the same building as your doctor — "
             "reported by a radiologist, with most results the same day.",
        meta="CT, MRI, ultrasound and X-ray scan centre with lab in Gajularamaram, Hyderabad — reported by a "
             "radiologist at Mana Hospitals. Call +91 79958 95858.",
        overview="Accurate diagnosis drives good treatment. Our radiology and laboratory services sit under the "
                 "same roof as the consultants, so scans and tests are done and reported quickly — and you are "
                 "not sent across the city mid-treatment.",
        conditions=["Brain, spine and body CT and MRI", "Abdominal and pelvic scans", "Pregnancy scans",
                    "Joint, bone and chest X-rays",
                    "Blood vessel (Doppler) studies", "Thyroid and neck scans", "Routine and specialised blood tests"],
        procedures=["CT scan", "MRI scan", "Ultrasound (USG)", "Digital X-ray", "Colour Doppler",
                    "Antenatal ultrasound — dating, anomaly and growth scans", "Pathology and biochemistry lab",
                    "Health check-up packages"],
        when=["Your doctor has advised a scan or blood test",
              "Monitoring a pregnancy",
              "An injury where a fracture needs ruling out",
              "A routine annual health check-up"],
        expect="Some scans need preparation — for example a full bladder for pelvic ultrasound or fasting for "
               "some abdominal scans and blood tests. The front desk will tell you when you book.",
        doctors=["Dr. Guntaka Srujana"],
        faqs=[("Can I get a scan without a doctor's prescription?",
               "Most tests are done on a doctor's advice. If you have symptoms, see one of our consultants first "
               "and the scan can usually be done the same day."),
              ("Is CT and MRI available at Mana Hospitals?",
               "Yes. CT and MRI scans are done in-house in Gajularamaram and reported by our radiologist, so you "
               "don't need to travel to another scan centre."),
              ("How soon will I get my report?",
               "Most ultrasound, X-ray and blood test reports are ready the same day; CT and MRI reports usually "
               "follow within the day."),
              ("Do I need to fast before an ultrasound?",
               "Fasting is needed for some abdominal scans, and a full bladder for pelvic scans. "
               "We will tell you how to prepare when you book.")]),

    dict(
        slug="infertility", nav="Infertility &amp; Fertility Care",
        title="Infertility &amp; Fertility Care",
        lines=["Infertility", "<i>&amp; fertility care</i>"],
        specialty="Gynecologic", term="infertility specialist", seo_kw="Infertility Specialist",
        lede="Trying to conceive without success? Step-by-step evaluation and treatment for couples, "
             "led by a gynaecologist with a fellowship in reproductive medicine.",
        meta="Infertility specialist in Gajularamaram, Hyderabad — fertility evaluation, PCOS and ovulation "
             "treatment by Dr. Madhavaram Mounika (FRM) at Mana Hospitals. Call +91 79958 95858.",
        overview="Difficulty conceiving is common and often treatable. Our fertility service, led by a "
                 "consultant OBGYN with a fellowship in reproductive medicine (FRM) and minimal-access surgery "
                 "(FMAS), evaluates both partners, explains the cause in plain language and starts with the "
                 "simplest effective treatment.",
        conditions=["Difficulty conceiving after a year of trying (six months if over 35)",
                    "PCOS and irregular ovulation", "Blocked fallopian tubes", "Endometriosis",
                    "Fibroids and uterine polyps affecting fertility", "Recurrent pregnancy loss",
                    "Thyroid and hormone problems", "Male factor evaluation"],
        procedures=["Fertility evaluation for both partners", "Hormone tests and pelvic ultrasound",
                    "Ovulation induction and follicular monitoring",
                    "Laparoscopic and hysteroscopic fertility-enhancing surgery",  # FMAS
                    "PCOS and lifestyle programmes",
                    "Counselling and referral when IVF is needed"],  # IVF is NOT done in-house (client, 18 Nov 2026)
        when=["You have been trying for a year (or six months if you are over 35) without success",
              "Your periods are irregular or absent",
              "You have had two or more miscarriages",
              "You have known PCOS, endometriosis or fibroids and are planning a pregnancy"],
        expect="The first visit is a detailed history and examination for both partners, followed by a "
               "short list of tests. You will get a clear, written plan — most couples start with simple, "
               "affordable steps.",
        doctors=["Dr. Madhavaram Mounika", "Dr. Alekhya Patluri"],
        faqs=[("When should we see an infertility specialist?",
               "After one year of regular unprotected intercourse without pregnancy, or after six months if "
               "the woman is over 35 — sooner if periods are irregular or there is a known condition."),
              ("Can PCOS affect fertility?",
               "Yes, PCOS can stop regular ovulation. It is one of the most treatable causes — with lifestyle "
               "changes and ovulation-inducing medicines many women conceive."),
              ("Do you do IVF at Mana Hospitals?",
               "IVF is not done at Mana Hospitals. We evaluate and treat most causes of infertility here; if IVF is "
               "the right next step, our specialist explains why, refers you to a trusted IVF centre, and can continue "
               "your pregnancy care with us afterwards."),
              ("Should both partners be tested?",
               "Yes. Male factors contribute to a large share of infertility, so evaluating both partners from "
               "the start saves time.")]),

    dict(
        slug="diabetes-care", nav="Diabetes &amp; Thyroid Care",
        title="Diabetes &amp; Thyroid Care (Diabetology)",
        lines=["Diabetes", "<i>&amp; thyroid care</i>"],
        specialty="Endocrine", term="diabetologist", seo_kw="Diabetologist &amp; Thyroid Care",
        lede="Sugar control, insulin, thyroid and cholesterol — personalised plans from diabetologists, "
             "with same-day lab tests and regular follow-up.",
        meta="Diabetologist in Gajularamaram, Hyderabad — diabetes, insulin, thyroid and cholesterol care with "
             "same-day tests at Mana Hospitals. Call +91 79958 95858.",
        overview="Diabetes is a long-term condition, and good control today prevents heart, kidney, eye and "
                 "foot problems tomorrow. Our diabetologists build a practical plan around your diet, routine "
                 "and medicines — and check the complications early, with the lab and specialists under one roof.",
        conditions=["Type 2 and type 1 diabetes", "Pre-diabetes", "Diabetes in pregnancy (GDM)",
                    "Thyroid disorders — hypo and hyperthyroidism", "High cholesterol",
                    "Obesity and metabolic syndrome", "Diabetic foot, nerve and kidney problems"],
        procedures=["HbA1c, sugar, thyroid and lipid tests — same day", "Insulin starting and dose adjustment",
                    "Diet and lifestyle counselling", "Diabetic foot and nerve screening",
                    "Kidney and heart risk screening", "Regular follow-up programmes"],
        when=["Excessive thirst, frequent urination or unexplained weight loss",
              "A sugar or HbA1c report above normal",
              "Diabetes that stays uncontrolled despite medicines",
              "Tiredness, weight change or swelling in the neck (thyroid)"],
        expect="Come fasting if possible so sugar and lipid tests can be done at the same visit. Bring your "
               "medicine list and any glucometer readings.",
        doctors=["Dr. Kosuri Akhila", "Dr. Sasikanth Reddy P"],
        faqs=[("What is a normal HbA1c?",
               "An HbA1c below 5.7% is normal, 5.7–6.4% suggests pre-diabetes, and 6.5% or above indicates "
               "diabetes. Your target depends on your age and health — your doctor will set it with you."),
              ("Can diabetes be reversed?",
               "Early type 2 diabetes can often be brought into remission with weight loss, diet and exercise. "
               "Long-standing diabetes usually needs ongoing medicines, but good control prevents complications."),
              ("Do I need to fast for a sugar test?",
               "A fasting sugar needs 8–10 hours without food; HbA1c does not need fasting. Coming fasting lets "
               "us do both in one visit.")]),
]

# SEO keys for the original eight pages
BASE_SEO = {
    "general-medicine": dict(specialty="PrimaryCare", term="general physician", seo_kw="General Physician"),
    "orthopaedics": dict(specialty="Musculoskeletal", term="orthopaedic doctor", seo_kw="Orthopaedic &amp; Knee Replacement"),
    "nephrology": dict(specialty="Renal", term="nephrologist", seo_kw="Kidney Care &amp; Dialysis Centre"),
    "gastroenterology": dict(specialty="Gastroenterologic", term="gastroenterologist", seo_kw="Gastroenterologist &amp; Endoscopy"),
    "neurology": dict(specialty="Neurologic", term="neurologist", seo_kw="Neurologist &amp; Stroke Care"),
    "pulmonology": dict(specialty="Pulmonary", term="pulmonologist", seo_kw="Pulmonologist &amp; Chest Specialist"),
    "gynaecology": dict(specialty="Gynecologic", term="gynaecologist", seo_kw="Gynaecologist &amp; Maternity"),
    "urology": dict(specialty="Urologic", term="urologist", seo_kw="Urologist &amp; Kidney Stones"),
}

# schema.org MedicalSpecialty for each consultant
DOC_SPECIALTY = {
    "Dr. Kosuri Akhila": ["PrimaryCare", "Endocrine"], "Dr. Madhavaram Mounika": ["Gynecologic", "Obstetric"],
    "Dr. Gopala Ithihaas": ["Pulmonary"], "Dr. Shivaiahgari Vinaykumar": ["Pediatric", "DietNutrition"],
    "Dr. Guntaka Srujana": ["Radiography"], "Dr. Sasikanth Reddy P": ["PrimaryCare", "Endocrine"],
    "Dr. Ramakrishna Reddy M": ["Pulmonary"], "Dr. Swaroop Chandra": ["Musculoskeletal"],
    "Dr. Naresh Kumar": ["Surgical"], "Dr. Alekhya Patluri": ["Gynecologic", "Obstetric"],
    "Dr. Vidyala Harika": ["PrimaryCare"], "Dr. M. Kiran Kumar": ["PrimaryCare"],
    "Dr. Juluri Vamshi Krishna": ["Emergency"], "Dr. Mohammed Adil Faraz": ["Surgical"],
    "Dr. Bagam Mahesh": ["Musculoskeletal"], "Dr. Ch. Divya": ["Pediatric"],
    "Dr. G. Vaishnavi": ["Pediatric"], "Dr. Manisha M": ["Otolaryngologic"],
}
