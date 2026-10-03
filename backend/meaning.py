def getMeaning(disease):
    D = {
        "Pancreatitis": {
            "description": "Inflammation of the pancreas, which can be acute (sudden) or chronic (long-term). The pancreas produces digestive enzymes that can start digesting the organ itself when inflamed.",
            "causes": "Gallstones, excessive alcohol use, high triglycerides, certain medications, or abdominal trauma.",
            "tests": [
                "Serum Amylase and Lipase blood test (key diagnostic markers)",
                "Complete Blood Count (CBC)",
                "Liver function tests",
                "Abdominal Ultrasound",
                "CT Scan of abdomen (to assess severity)",
                "MRI / MRCP (for ductal abnormalities)"
            ],
            "care": [
                "Hospitalization with IV fluids and fasting (NPO) in acute cases",
                "Pain management with analgesics",
                "Avoid alcohol and fatty foods completely",
                "Low-fat diet after recovery",
                "Treat underlying cause (e.g., remove gallstones)",
                "Pancreatic enzyme supplements in chronic cases"
            ]
        },
        "Multiple Sclerosis": {
            "description": "A chronic autoimmune disease where the immune system attacks the myelin sheath (protective covering) of nerve fibers in the brain and spinal cord, disrupting nerve signal transmission.",
            "causes": "Exact cause unknown; involves genetic predisposition and environmental triggers like viral infections.",
            "tests": [
                "MRI of brain and spinal cord (gold standard — shows lesions/plaques)",
                "Lumbar Puncture / Spinal Tap (checks for oligoclonal bands)",
                "Evoked Potential Tests (measures nerve signal speed)",
                "Blood tests to rule out other conditions",
                "Visual Evoked Potential (VEP) test"
            ],
            "care": [
                "Disease-modifying therapies (DMTs) like Interferon beta, Glatiramer acetate",
                "Corticosteroids during relapses",
                "Physical therapy to maintain mobility",
                "Occupational therapy",
                "Fatigue management and adequate rest",
                "Regular neurologist follow-up"
            ]
        },
        "Stroke": {
            "description": "A medical emergency where blood supply to part of the brain is cut off (ischemic) or a blood vessel in the brain bursts (hemorrhagic), causing brain cells to die rapidly.",
            "causes": "Blood clots, arterial blockage, high blood pressure, atrial fibrillation, or ruptured aneurysm.",
            "tests": [
                "CT Scan of brain (immediate — to distinguish ischemic vs hemorrhagic)",
                "MRI Brain (more detailed lesion detection)",
                "Carotid Ultrasound",
                "Echocardiogram (to check for heart clots)",
                "Blood coagulation tests (PT, INR, aPTT)",
                "Blood glucose and lipid profile"
            ],
            "care": [
                "EMERGENCY — call ambulance immediately (golden hour critical)",
                "tPA (clot-busting drug) within 4.5 hours for ischemic stroke",
                "Blood pressure control",
                "Antiplatelet therapy (Aspirin, Clopidogrel)",
                "Anticoagulants if atrial fibrillation is cause",
                "Rehabilitation: physiotherapy, speech therapy, occupational therapy",
                "Lifestyle changes: diet, exercise, quit smoking"
            ]
        },
        "Irritable Bowel Syndrome": {
            "description": "A common chronic gastrointestinal disorder affecting the large intestine, causing recurring abdominal pain and altered bowel habits without any structural damage.",
            "causes": "Exact cause unknown; involves gut-brain axis dysfunction, gut sensitivity, intestinal inflammation, and stress.",
            "tests": [
                "Clinical diagnosis based on Rome IV criteria",
                "Blood tests to rule out celiac disease, anemia, infection",
                "Stool tests (to rule out infection, blood)",
                "Colonoscopy (if red flag symptoms present)",
                "Food intolerance testing (lactose, gluten)"
            ],
            "care": [
                "High-fiber diet or low FODMAP diet",
                "Avoid trigger foods (dairy, gluten, spicy food, caffeine)",
                "Stress management (yoga, meditation, CBT)",
                "Antispasmodic medications (Mebeverine, Hyoscine)",
                "Laxatives for constipation-dominant IBS",
                "Antidiarrheals (Loperamide) for diarrhea-dominant IBS",
                "Probiotics to restore gut flora"
            ]
        },
        "Typhoid Fever": {
            "description": "A systemic bacterial infection caused by Salmonella typhi, spread through contaminated food and water. Common in areas with poor sanitation.",
            "causes": "Ingestion of food or water contaminated with Salmonella typhi bacteria.",
            "tests": [
                "Widal Test (antibody detection — common but less specific)",
                "Blood Culture (gold standard in first week)",
                "Stool and Urine Culture (after 2nd week)",
                "Typhidot / Tubex test (rapid antigen detection)",
                "Complete Blood Count (low WBC is typical)"
            ],
            "care": [
                "Antibiotics: Azithromycin, Ciprofloxacin, or Ceftriaxone",
                "Adequate hydration with ORS or IV fluids",
                "Soft, easily digestible diet",
                "Bed rest",
                "Antipyretics for fever (Paracetamol — avoid Aspirin)",
                "Typhoid vaccine for prevention in endemic areas",
                "Isolate patient to prevent spread"
            ]
        },
        "Influenza": {
            "description": "A highly contagious viral respiratory illness caused by Influenza A or B viruses, typically occurring in seasonal outbreaks. More severe than the common cold.",
            "causes": "Influenza virus spread through respiratory droplets from coughing, sneezing, or talking.",
            "tests": [
                "Rapid Influenza Diagnostic Test (RIDT) — nasal swab",
                "RT-PCR (most accurate — gold standard)",
                "Viral culture",
                "Clinical diagnosis based on symptoms during outbreak season"
            ],
            "care": [
                "Rest and adequate fluid intake",
                "Antiviral drugs: Oseltamivir (Tamiflu) within 48 hours of onset",
                "Paracetamol for fever and body ache",
                "Annual influenza vaccination (best prevention)",
                "Isolate patient to prevent spread",
                "Seek hospital care if breathing difficulty, persistent high fever, or confusion"
            ]
        },
        "Whooping Cough": {
            "description": "A highly contagious bacterial respiratory infection (Pertussis) characterized by severe coughing spells that end with a 'whoop' sound while gasping for air. Dangerous for infants.",
            "causes": "Bordetella pertussis bacteria, spread via respiratory droplets.",
            "tests": [
                "Nasopharyngeal swab culture (gold standard)",
                "PCR test of nasal/throat swab",
                "Blood test (elevated lymphocytes)",
                "Clinical diagnosis based on cough pattern"
            ],
            "care": [
                "Antibiotics: Azithromycin or Erythromycin (especially effective early)",
                "Isolate patient for at least 5 days after starting antibiotics",
                "Adequate rest and hydration",
                "Avoid irritants like smoke",
                "DTaP / Tdap vaccination (prevention — given in childhood schedule)",
                "Hospitalization for infants and severe cases"
            ]
        },
        "Epilepsy": {
            "description": "A chronic neurological disorder characterized by recurrent, unprovoked seizures caused by abnormal electrical activity in the brain.",
            "causes": "Brain injury, genetic factors, brain tumors, stroke, infections, or unknown (idiopathic).",
            "tests": [
                "EEG (Electroencephalogram) — detects abnormal brain wave patterns",
                "MRI Brain (to detect structural causes)",
                "CT Scan Brain",
                "Blood tests (glucose, electrolytes, renal/liver function)",
                "Lumbar Puncture (if infection suspected)"
            ],
            "care": [
                "Antiepileptic drugs (AEDs): Valproate, Phenytoin, Levetiracetam, Carbamazepine",
                "Never leave patient alone during seizure — protect from injury",
                "Do not restrain during seizure; place on side to prevent aspiration",
                "Avoid seizure triggers: sleep deprivation, alcohol, flickering lights",
                "Ketogenic diet (for drug-resistant cases)",
                "Surgery (if single seizure focus identified)",
                "Avoid driving until seizure-free for prescribed duration"
            ]
        },
        "Encephalitis": {
            "description": "Inflammation of the brain, usually caused by a viral infection. It is a serious, potentially life-threatening condition requiring urgent medical care.",
            "causes": "Viral infections (Herpes simplex, Japanese Encephalitis, Rabies), autoimmune conditions, or bacterial spread.",
            "tests": [
                "MRI Brain (shows areas of inflammation)",
                "Lumbar Puncture / CSF analysis (key diagnostic test)",
                "EEG",
                "Blood cultures and viral serology",
                "PCR for Herpes simplex virus (HSV) in CSF"
            ],
            "care": [
                "Immediate hospitalization — medical emergency",
                "Antiviral therapy: IV Acyclovir (for HSV encephalitis)",
                "Corticosteroids (for autoimmune encephalitis)",
                "Seizure management with antiepileptic drugs",
                "IV fluids and nutritional support",
                "Monitor and manage brain swelling (ICP monitoring)"
            ]
        },
        "Heart Failure": {
            "description": "A chronic condition where the heart muscle is unable to pump enough blood to meet the body's needs, leading to fluid buildup in the lungs and body.",
            "causes": "Coronary artery disease, high blood pressure, previous heart attack, diabetes, or valvular heart disease.",
            "tests": [
                "Echocardiogram (most important — assesses ejection fraction)",
                "BNP / NT-proBNP blood test (biomarker of heart strain)",
                "Chest X-ray (shows enlarged heart, pulmonary edema)",
                "ECG (Electrocardiogram)",
                "Complete Blood Count and kidney/liver function tests",
                "Cardiac MRI"
            ],
            "care": [
                "ACE inhibitors or ARBs (reduce heart workload)",
                "Beta-blockers (slow heart rate, improve function)",
                "Diuretics (Furosemide — remove excess fluid)",
                "Salt and fluid restriction in diet",
                "Daily weight monitoring (fluid accumulation alert)",
                "Cardiac rehabilitation program",
                "Avoid NSAIDs — worsen heart failure",
                "ICD (defibrillator) or pacemaker if indicated"
            ]
        },
        "Pneumonia": {
            "description": "An infection that inflames the air sacs (alveoli) in one or both lungs, causing them to fill with fluid or pus, making breathing difficult.",
            "causes": "Bacteria (Streptococcus pneumoniae most common), viruses (influenza, COVID-19), or fungi.",
            "tests": [
                "Chest X-ray (shows consolidation — key diagnostic tool)",
                "Complete Blood Count (elevated WBC indicates bacterial)",
                "Sputum culture and sensitivity",
                "Blood culture (if severe)",
                "Pulse oximetry (oxygen saturation)",
                "CT Chest (if X-ray inconclusive)"
            ],
            "care": [
                "Antibiotics (Amoxicillin, Azithromycin, or Levofloxacin based on severity)",
                "Antiviral if viral pneumonia (Oseltamivir)",
                "Adequate rest and fluid intake",
                "Oxygen therapy if SpO2 < 94%",
                "Hospitalization for severe cases (CURB-65 score)",
                "Pneumococcal vaccine for prevention",
                "Deep breathing exercises during recovery"
            ]
        },
        "Appendicitis": {
            "description": "Inflammation of the appendix (a small pouch attached to the large intestine), which can rupture if untreated, causing life-threatening infection.",
            "causes": "Blockage of the appendix by stool, mucus, or foreign matter leading to bacterial overgrowth.",
            "tests": [
                "Clinical examination (Rebound tenderness, McBurney's point)",
                "Ultrasound abdomen (first-line imaging)",
                "CT Scan abdomen (gold standard — highest accuracy)",
                "Complete Blood Count (elevated WBC)",
                "Urine test (to rule out UTI)",
                "Alvarado Score assessment"
            ],
            "care": [
                "SURGICAL EMERGENCY — Appendectomy (laparoscopic or open)",
                "IV antibiotics before and after surgery",
                "IV fluids and pain management pre-operatively",
                "Do NOT take laxatives or apply heat to abdomen",
                "NPO (nothing by mouth) once diagnosed",
                "Post-operative wound care and early ambulation"
            ]
        },
        "Cholera": {
            "description": "An acute diarrheal infection caused by Vibrio cholerae bacteria, capable of causing severe dehydration and death within hours if untreated. Linked to contaminated water.",
            "causes": "Drinking water or eating food contaminated with Vibrio cholerae bacteria.",
            "tests": [
                "Stool culture (gold standard — identifies Vibrio cholerae)",
                "Rapid Cholera Dipstick Test",
                "Dark-field microscopy of stool",
                "Blood electrolytes (assess dehydration severity)"
            ],
            "care": [
                "PRIORITY: Immediate rehydration with ORS (Oral Rehydration Solution)",
                "IV fluids (Ringer's Lactate) for severe dehydration",
                "Antibiotics: Doxycycline or Azithromycin (shortens illness duration)",
                "Zinc supplementation (especially in children)",
                "Clean water, sanitation, and hygiene (WASH) practices",
                "Cholera vaccine (Dukoral) for endemic areas and travelers"
            ]
        },
        "Rabies": {
            "description": "A fatal viral disease transmitted through the saliva of infected animals, primarily dogs. Once clinical symptoms appear, it is almost always fatal.",
            "causes": "Rabies virus transmitted via bite or scratch from infected animals (dogs, bats, foxes).",
            "tests": [
                "Clinical diagnosis (post-exposure — do not wait for test results)",
                "Direct Fluorescent Antibody (DFA) test on brain tissue (post-mortem)",
                "Skin biopsy (nape of neck)",
                "Saliva PCR",
                "CSF analysis"
            ],
            "care": [
                "PREVENTION IS CRITICAL — post-exposure prophylaxis (PEP) must start immediately",
                "Wound washing with soap and water for 15 minutes immediately after bite",
                "Rabies Immunoglobulin (RIG) at wound site",
                "Rabies vaccine series (Days 0, 3, 7, 14)",
                "Pre-exposure vaccination for high-risk individuals (vets, travelers)",
                "Once symptoms appear — only palliative (comfort) care is possible"
            ]
        },
        "Filariasis": {
            "description": "A parasitic disease caused by filarial worms transmitted through mosquito bites, leading to lymphatic damage and severe swelling of limbs (elephantiasis).",
            "causes": "Wuchereria bancrofti parasitic worm transmitted by Culex mosquitoes.",
            "tests": [
                "Peripheral blood smear (nocturnal — for microfilariae detection)",
                "Antigen detection test (ICT card test)",
                "Ultrasound (to detect adult worms — 'filarial dance sign')",
                "Antibody ELISA test"
            ],
            "care": [
                "Diethylcarbamazine (DEC) — main antiparasitic drug",
                "Albendazole (combination therapy)",
                "Limb elevation and compression garments for lymphedema",
                "Strict hygiene and skin care of affected limbs",
                "Mosquito control and insecticide-treated bed nets",
                "Mass Drug Administration (MDA) programs in endemic areas"
            ]
        },
        "Crohns Disease": {
            "description": "A chronic inflammatory bowel disease (IBD) that can affect any part of the gastrointestinal tract, causing inflammation that penetrates deep into bowel wall tissue.",
            "causes": "Autoimmune reaction where immune system attacks gut; triggered by genetic and environmental factors.",
            "tests": [
                "Colonoscopy with biopsy (gold standard)",
                "MRI Enterography (assesses small bowel)",
                "CT Scan abdomen",
                "Fecal Calprotectin (marker of gut inflammation)",
                "CRP and ESR (inflammatory markers)",
                "Complete Blood Count (anemia is common)"
            ],
            "care": [
                "Aminosalicylates (5-ASA drugs) for mild disease",
                "Corticosteroids for acute flare-ups",
                "Immunomodulators (Azathioprine, Methotrexate)",
                "Biologics: Anti-TNF agents (Infliximab, Adalimumab)",
                "Low-fiber, easily digestible diet during flares",
                "Nutritional support (sometimes enteral nutrition)",
                "Surgery if complications (obstruction, fistula, abscess)",
                "Lifelong specialist gastroenterologist follow-up"
            ]
        },
        "Herpes Zoster": {
            "description": "Also called Shingles. A painful skin rash caused by reactivation of the Varicella-Zoster virus (same virus that causes chickenpox), which lies dormant in nerve tissue.",
            "causes": "Reactivation of latent Varicella-Zoster Virus (VZV), often triggered by immune suppression, stress, or aging.",
            "tests": [
                "Clinical diagnosis (characteristic dermatomal rash pattern)",
                "Tzanck Smear (from vesicle base)",
                "PCR of vesicle fluid (most sensitive)",
                "Varicella-Zoster IgM and IgG antibody serology"
            ],
            "care": [
                "Antiviral therapy: Acyclovir, Valacyclovir, or Famciclovir (start within 72 hours)",
                "Pain management: Paracetamol, NSAIDs, Gabapentin (for nerve pain)",
                "Keep rash dry and clean; calamine lotion for itching",
                "Avoid contact with immunocompromised individuals and pregnant women",
                "Herpes Zoster vaccine (Shingrix) for prevention in 50+ age group",
                "Postherpetic neuralgia management if pain persists after rash heals"
            ]
        },
        "Myocardial Infarction": {
            "description": "Commonly called a Heart Attack. Occurs when blood flow to a part of the heart muscle is blocked for long enough that heart muscle begins to die.",
            "causes": "Rupture of atherosclerotic plaque in coronary artery causing blood clot formation.",
            "tests": [
                "ECG (Electrocardiogram) — immediate ST elevation (STEMI) detection",
                "Troponin I and T blood test (gold standard biomarker)",
                "CK-MB (Creatine Kinase-MB)",
                "Echocardiogram",
                "Coronary Angiography (defines which artery is blocked)"
            ],
            "care": [
                "MEDICAL EMERGENCY — call ambulance immediately",
                "Aspirin 325mg immediately (chewed)",
                "Nitroglycerin for chest pain",
                "Primary PCI (stenting) — best treatment within 90 minutes",
                "Thrombolysis (clot-busting drugs) if PCI not available",
                "Beta-blockers, ACE inhibitors, Statins post-MI",
                "Cardiac rehabilitation after discharge",
                "Lifestyle modification: quit smoking, low-fat diet, exercise"
            ]
        },
        "Gastroenteritis": {
            "description": "Inflammation of the stomach and intestines (gut), commonly called stomach flu. Causes sudden onset of nausea, vomiting, diarrhea, and abdominal cramps.",
            "causes": "Viral (Rotavirus, Norovirus most common), bacterial (Salmonella, E. coli), or parasitic infections.",
            "tests": [
                "Usually clinical diagnosis",
                "Stool culture (if severe or prolonged)",
                "Stool microscopy (for parasites)",
                "Blood tests (if dehydration is severe)"
            ],
            "care": [
                "ORS (Oral Rehydration Solution) — primary treatment",
                "IV fluids if unable to tolerate oral intake",
                "BRAT diet: Bananas, Rice, Applesauce, Toast",
                "Avoid dairy, fatty, spicy foods during illness",
                "Antiemetics (Ondansetron) for severe vomiting",
                "Antibiotics only if bacterial cause confirmed",
                "Strict hand hygiene to prevent spread"
            ]
        },
        "Heat Stroke": {
            "description": "A life-threatening condition where the body's temperature regulation fails and core body temperature rises above 40°C (104°F), causing organ damage and neurological dysfunction.",
            "causes": "Prolonged exposure to high temperatures, physical exertion in heat, dehydration, or hot and humid environments.",
            "tests": [
                "Core body temperature measurement (rectal thermometer — most accurate)",
                "Blood tests: CBC, electrolytes, kidney and liver function",
                "Coagulation profile (DIC risk)",
                "Blood glucose",
                "CT Brain (if confusion or coma)"
            ],
            "care": [
                "EMERGENCY — move to cool environment immediately",
                "Rapid cooling: ice packs on neck, groin, armpits; cool water misting",
                "IV fluids for rehydration",
                "Monitor core temperature continuously",
                "Airway management if unconscious",
                "Avoid giving water to unconscious patient orally",
                "Hospitalization in ICU for severe cases",
                "Prevent: stay hydrated, avoid peak sun hours, wear light clothing"
            ]
        },
        "Sinusitis": {
            "description": "Inflammation or swelling of the tissue lining the sinuses (air-filled spaces in the skull), causing them to become blocked and filled with fluid.",
            "causes": "Viral upper respiratory infection, bacterial infection, allergies, nasal polyps, or deviated nasal septum.",
            "tests": [
                "Clinical diagnosis in most cases",
                "Nasal endoscopy",
                "CT Scan of sinuses (gold standard for chronic cases)",
                "Nasal swab culture (if bacterial cause suspected)",
                "Allergy testing (if allergic sinusitis suspected)"
            ],
            "care": [
                "Saline nasal irrigation (Neti pot) — clears mucus",
                "Nasal decongestant sprays (short-term use only — max 3 days)",
                "Intranasal corticosteroid sprays (Budesonide, Fluticasone)",
                "Steam inhalation",
                "Antibiotics (Amoxicillin) only if bacterial — typically 10–14 days",
                "Antihistamines if allergic cause",
                "Surgery (FESS — functional endoscopic sinus surgery) for chronic/recurrent cases"
            ]
        },
        "Fibromyalgia": {
            "description": "A chronic disorder characterized by widespread musculoskeletal pain, fatigue, sleep problems, and often cognitive difficulties (fibro fog). No structural abnormality is found.",
            "causes": "Exact cause unknown; involves central sensitization where the brain amplifies pain signals abnormally.",
            "tests": [
                "Clinical diagnosis based on widespread pain index and symptom severity scale",
                "Blood tests to rule out other conditions (ANA, ESR, CRP, Thyroid function, CBC)",
                "No specific blood test confirms fibromyalgia"
            ],
            "care": [
                "Regular low-impact aerobic exercise (most effective long-term treatment)",
                "Cognitive Behavioral Therapy (CBT)",
                "Medications: Pregabalin (Lyrica), Duloxetine, Amitriptyline",
                "Good sleep hygiene",
                "Stress management: yoga, mindfulness",
                "Physical therapy",
                "Avoid overexertion — pace activities",
                "Patient education and support groups"
            ]
        },
        "Asthma": {
            "description": "A chronic inflammatory airway disease causing recurrent episodes of wheezing, breathlessness, chest tightness, and coughing, particularly at night or early morning.",
            "causes": "Allergies (dust, pollen, pet dander), exercise, cold air, respiratory infections, or irritants like smoke.",
            "tests": [
                "Spirometry (measures airflow — key diagnostic test)",
                "Peak Expiratory Flow Rate (PEFR) monitoring",
                "Bronchodilator reversibility test",
                "Allergy skin prick tests or serum IgE",
                "FeNO (Fractional exhaled Nitric Oxide) test",
                "Chest X-ray (to rule out other causes)"
            ],
            "care": [
                "Reliever inhaler: Short-acting Beta-2 agonist (Salbutamol) for acute symptoms",
                "Preventer inhaler: Inhaled corticosteroids (Budesonide, Beclomethasone) daily",
                "Long-acting Beta-2 agonists (Formoterol) for persistent asthma",
                "Avoid known triggers",
                "Asthma action plan for self-management",
                "Oral corticosteroids for severe exacerbations",
                "Proper inhaler technique education"
            ]
        },
        "Dengue Hemorrhagic Fever": {
            "description": "A severe, potentially fatal complication of dengue infection where blood vessels become damaged and leaky, causing internal bleeding and platelet count to drop dangerously low.",
            "causes": "Dengue virus (DENV serotypes 1–4) transmitted by Aedes aegypti mosquito, usually during secondary infection.",
            "tests": [
                "NS1 Antigen test (positive in first 5 days)",
                "Dengue IgM and IgG antibody test",
                "Complete Blood Count (platelet count, hematocrit rise is key)",
                "Liver function tests (ALT/AST often elevated)",
                "Clotting profile (PT, aPTT)",
                "Ultrasound abdomen (detect fluid leakage — ascites, pleural effusion)"
            ],
            "care": [
                "HOSPITALIZATION mandatory",
                "Platelet count monitoring every 6–12 hours",
                "IV fluids (crystalloids) — strict fluid management",
                "Platelet transfusion if count drops below 10,000 or active bleeding",
                "Paracetamol for fever — AVOID Aspirin and NSAIDs (increase bleeding risk)",
                "Mosquito control: nets, repellents, eliminate stagnant water",
                "Dengue vaccine (Dengvaxia) for seropositive individuals"
            ]
        },
        "Type 1 Diabetes": {
            "description": "An autoimmune condition where the immune system destroys insulin-producing beta cells in the pancreas, resulting in no insulin production. Typically diagnosed in children and young adults.",
            "causes": "Autoimmune destruction of pancreatic beta cells; genetic and environmental triggers.",
            "tests": [
                "Fasting Blood Glucose (> 126 mg/dL on two occasions)",
                "HbA1c (> 6.5%)",
                "C-peptide level (very low or absent in T1D)",
                "Anti-GAD antibodies, Anti-insulin antibodies (autoimmune markers)",
                "Random Blood Glucose with symptoms"
            ],
            "care": [
                "Lifelong Insulin therapy (multiple daily injections or insulin pump)",
                "Blood glucose self-monitoring (4–7 times daily)",
                "Carbohydrate counting for meal planning",
                "HbA1c check every 3 months",
                "Regular screening for complications (eyes, kidneys, nerves)",
                "Hypoglycemia management: keep glucose tablets handy",
                "Continuous Glucose Monitoring (CGM) devices"
            ]
        },
        "Tuberculosis": {
            "description": "A serious bacterial infection primarily affecting the lungs but can spread to any organ. It spreads through airborne droplets from coughs of infected individuals.",
            "causes": "Mycobacterium tuberculosis bacteria transmitted via inhalation of infectious droplets.",
            "tests": [
                "Sputum AFB (Acid Fast Bacilli) smear and culture (gold standard)",
                "GeneXpert / CBNAAT test (rapid molecular test — also detects drug resistance)",
                "Chest X-ray (typical apical infiltrates, cavities)",
                "Tuberculin Skin Test / Mantoux Test",
                "IGRA (Interferon Gamma Release Assay) blood test",
                "CT Chest (if X-ray inconclusive)"
            ],
            "care": [
                "DOTS (Directly Observed Treatment Short-course) — 6 months minimum",
                "First-line drugs: HRZE regimen (Isoniazid, Rifampicin, Pyrazinamide, Ethambutol)",
                "Strict medication adherence — missing doses causes drug resistance",
                "Respiratory isolation during infectious phase",
                "Nutritional support (malnutrition worsens TB)",
                "Contact tracing for family and close contacts",
                "BCG vaccine at birth for prevention"
            ]
        },
        "Dehydration": {
            "description": "A condition where the body loses more fluids than it takes in, impairing normal body functions. Can range from mild to severe and life-threatening.",
            "causes": "Diarrhea, vomiting, excessive sweating, insufficient fluid intake, fever, or burns.",
            "tests": [
                "Clinical assessment (skin turgor, dry mouth, sunken eyes)",
                "Blood tests: electrolytes (sodium, potassium), BUN, creatinine",
                "Urine specific gravity (concentrated urine indicates dehydration)",
                "Blood pressure and heart rate monitoring"
            ],
            "care": [
                "ORS (Oral Rehydration Solution) for mild to moderate dehydration",
                "IV fluids (Normal Saline or Ringer's Lactate) for severe dehydration",
                "Treat underlying cause (diarrhea, vomiting, fever)",
                "Frequent small sips of water if vomiting",
                "Avoid caffeine and alcohol",
                "Monitor urine output (aim for pale yellow urine)"
            ]
        },
        "UTI": {
            "description": "Urinary Tract Infection — a bacterial infection affecting any part of the urinary system (urethra, bladder, ureters, kidneys). More common in women than men.",
            "causes": "Bacteria (usually E. coli) entering the urinary tract via the urethra.",
            "tests": [
                "Urine Routine and Microscopy (pus cells, bacteria)",
                "Urine Culture and Sensitivity (identifies bacteria and best antibiotic)",
                "Dipstick urine test (nitrites and leukocyte esterase positive)",
                "Ultrasound kidney-bladder (if upper UTI or recurrent UTI suspected)",
                "Blood CBC and CRP (if kidney infection — pyelonephritis — suspected)"
            ],
            "care": [
                "Antibiotics based on culture: Nitrofurantoin, Trimethoprim, or Ciprofloxacin",
                "Increased water intake (flush bacteria from urinary tract)",
                "Complete the full antibiotic course",
                "Urinate after sexual activity (preventive)",
                "Avoid holding urine for long periods",
                "Cranberry supplements (mild preventive effect)",
                "Wipe front to back (women)",
                "Repeat urine culture after treatment to confirm cure"
            ]
        },
        "Psoriasis": {
            "description": "A chronic autoimmune skin disease that causes rapid buildup of skin cells, resulting in scaling, red patches, and inflammation. It is not contagious.",
            "causes": "Immune system malfunction triggering overproduction of skin cells; genetics and environmental factors play a role.",
            "tests": [
                "Clinical diagnosis based on skin appearance",
                "Skin biopsy (to confirm diagnosis if uncertain)",
                "Blood tests to rule out psoriatic arthritis (RF, anti-CCP)",
                "Joint X-ray if joint involvement suspected"
            ],
            "care": [
                "Topical corticosteroids (first-line for mild psoriasis)",
                "Topical Vitamin D analogues (Calcipotriol)",
                "Phototherapy (UV-B light therapy) for moderate cases",
                "Methotrexate, Cyclosporine (for severe cases)",
                "Biologics: TNF inhibitors, IL-17/IL-23 inhibitors (for refractory cases)",
                "Moisturize regularly to prevent skin cracking",
                "Avoid triggers: stress, smoking, alcohol, skin injury",
                "Coal tar preparations for scalp psoriasis"
            ]
        },
        "Vitamin D Deficiency": {
            "description": "A condition where the body lacks sufficient Vitamin D, which is essential for calcium absorption, bone health, immune function, and muscle strength.",
            "causes": "Inadequate sunlight exposure, poor dietary intake, malabsorption, obesity, or dark skin in low-sunlight regions.",
            "tests": [
                "Serum 25-hydroxyvitamin D [25(OH)D] blood test (key diagnostic test)",
                "Serum Calcium and Phosphate levels",
                "Parathyroid Hormone (PTH) — elevated in deficiency",
                "Bone density scan (DEXA) if osteoporosis suspected",
                "X-ray (for rickets assessment in children)"
            ],
            "care": [
                "Vitamin D3 (Cholecalciferol) supplementation — dose based on deficiency severity",
                "Calcium supplementation if dietary intake is low",
                "Sunlight exposure: 15–30 minutes daily on skin",
                "Vitamin D-rich foods: fatty fish, egg yolks, fortified milk",
                "Repeat 25(OH)D level after 8–12 weeks of supplementation",
                "Treat underlying malabsorption if present"
            ]
        },
        "Hyperthyroidism": {
            "description": "A condition where the thyroid gland produces excessive thyroid hormones, accelerating the body's metabolism and causing a range of symptoms from weight loss to heart palpitations.",
            "causes": "Graves' disease (most common autoimmune cause), toxic multinodular goiter, thyroid nodules, or excessive iodine intake.",
            "tests": [
                "Thyroid Function Test: TSH (suppressed), Free T3 and Free T4 (elevated)",
                "Anti-TSH Receptor Antibody (TRAb) — elevated in Graves' disease",
                "Thyroid Ultrasound",
                "Radioactive Iodine Uptake Scan (RAIU) — shows overactive tissue",
                "ECG (if palpitations or atrial fibrillation)"
            ],
            "care": [
                "Antithyroid drugs: Carbimazole or Methimazole (block hormone production)",
                "Beta-blockers (Propranolol) — controls palpitations and tremor",
                "Radioactive Iodine (RAI) therapy (permanently reduces thyroid activity)",
                "Surgery (Thyroidectomy) in selected cases",
                "Avoid iodine-rich foods (kelp, iodized salt in excess)",
                "Regular thyroid function monitoring every 4–6 weeks during treatment"
            ]
        },
        "Ankylosing Spondylitis": {
            "description": "A chronic inflammatory arthritis that primarily affects the spine, causing vertebrae to fuse together over time, leading to stiffness and reduced mobility. Also affects other joints and organs.",
            "causes": "Autoimmune condition strongly associated with HLA-B27 gene mutation.",
            "tests": [
                "HLA-B27 genetic test (positive in ~90% of patients)",
                "X-ray of sacroiliac joints and spine (sacroiliitis is hallmark finding)",
                "MRI sacroiliac joints (more sensitive for early disease)",
                "CRP and ESR (inflammatory markers)",
                "Complete Blood Count"
            ],
            "care": [
                "NSAIDs (Indomethacin, Naproxen) — first-line treatment",
                "Daily physiotherapy and back exercises (critical to maintain posture)",
                "Biologics: Anti-TNF agents (Etanercept, Adalimumab) for moderate-severe disease",
                "IL-17 inhibitors (Secukinumab) — newer option",
                "Posture training and swimming (low-impact exercise)",
                "Avoid smoking — accelerates spinal fusion",
                "Sleep on firm mattress, avoid pillow under head",
                "Regular ophthalmology check (uveitis is a complication)"
            ]
        },
        "Common Cold": {
            "description": "A mild viral infection of the upper respiratory tract (nose and throat), caused by over 200 different viruses. The most frequent illness in humans.",
            "causes": "Rhinoviruses (most common), Coronaviruses, RSV — spread through droplets and contact with contaminated surfaces.",
            "tests": [
                "No tests required in most cases — purely clinical diagnosis",
                "Throat swab (if streptococcal infection needs to be ruled out)",
                "Rapid antigen test (to rule out influenza)"
            ],
            "care": [
                "Rest and adequate fluid intake",
                "Paracetamol or Ibuprofen for fever and discomfort",
                "Saline nasal drops or spray",
                "Honey and warm lemon water (soothe throat)",
                "Steam inhalation",
                "Avoid antibiotics — not effective for viral infection",
                "Usually resolves within 7–10 days",
                "Frequent hand washing to prevent spreading"
            ]
        },
        "Food Poisoning": {
            "description": "An illness caused by consuming contaminated food or beverages. Symptoms typically appear rapidly and include nausea, vomiting, diarrhea, and abdominal cramps.",
            "causes": "Bacteria (Salmonella, Staphylococcus, Campylobacter, E. coli), viruses (Norovirus), or toxins in improperly stored food.",
            "tests": [
                "Stool culture (identifies causative organism)",
                "Blood culture (if systemic infection suspected)",
                "Blood electrolytes (if severe dehydration)",
                "Stool microscopy for parasites"
            ],
            "care": [
                "ORS for rehydration — primary treatment",
                "Avoid solid food until vomiting subsides",
                "Gradually resume bland diet (BRAT diet)",
                "Antibiotics only if bacterial cause confirmed (Ciprofloxacin, Azithromycin)",
                "Antiemetics (Ondansetron) for severe nausea",
                "Avoid dairy, fatty, spicy foods during recovery",
                "Prevent: proper food storage, cooking temperatures, hand hygiene"
            ]
        },
        "Osteoarthritis": {
            "description": "The most common form of arthritis, caused by the breakdown of cartilage in joints, primarily affecting the knees, hips, spine, and hands. More common in older adults.",
            "causes": "Aging, joint overuse, obesity, previous joint injury, or genetic predisposition.",
            "tests": [
                "X-ray of affected joint (shows joint space narrowing, bone spurs — key diagnostic)",
                "MRI (more detailed cartilage assessment)",
                "Blood tests to rule out inflammatory arthritis (RF, anti-CCP, CRP)",
                "Synovial fluid analysis (joint fluid aspiration)"
            ],
            "care": [
                "Weight loss (reduces joint load — most important modifiable factor)",
                "Regular low-impact exercise: swimming, cycling, walking",
                "Physiotherapy and strengthening exercises",
                "Paracetamol for mild pain",
                "Topical NSAIDs (Diclofenac gel)",
                "Oral NSAIDs for moderate pain (with stomach protection)",
                "Intra-articular corticosteroid injections",
                "Knee replacement surgery for severe cases"
            ]
        },
        "Nephrotic Syndrome": {
            "description": "A kidney disorder where damage to the glomeruli (filtering units) causes massive protein loss in urine, leading to low blood protein, severe swelling, and high cholesterol.",
            "causes": "Primary: Minimal Change Disease (most common in children), Membranous nephropathy. Secondary: Diabetes, Lupus, infections.",
            "tests": [
                "Urine protein: creatinine ratio (massive proteinuria > 3.5g/day)",
                "24-hour urine protein collection",
                "Serum albumin (low)",
                "Serum cholesterol and triglycerides (elevated)",
                "Kidney biopsy (to identify exact type)",
                "Renal function tests (creatinine, BUN)"
            ],
            "care": [
                "Corticosteroids (Prednisolone) — first-line for most types",
                "Immunosuppressants (Cyclophosphamide, Tacrolimus) for steroid-resistant cases",
                "Diuretics (Furosemide) for edema",
                "ACE inhibitors or ARBs (reduce protein loss)",
                "Low-salt, low-fat diet",
                "Albumin infusion for severe hypoalbuminemia",
                "Anticoagulation (clot risk is high due to protein C/S loss)",
                "Statin therapy for high cholesterol"
            ]
        },
        "Measles": {
            "description": "A highly contagious viral disease characterized by fever, cough, runny nose, red eyes, and a distinctive spreading skin rash. Preventable by vaccine.",
            "causes": "Measles virus (Morbillivirus), spread through respiratory droplets — one of the most contagious diseases known.",
            "tests": [
                "Clinical diagnosis (characteristic Koplik's spots inside cheek + rash pattern)",
                "Measles IgM antibody test",
                "Viral PCR from throat or nasal swab",
                "Measles IgG (for immunity assessment)"
            ],
            "care": [
                "No specific antiviral treatment — supportive care",
                "Rest and fluid intake",
                "Vitamin A supplementation (reduces complications, especially in children)",
                "Paracetamol for fever",
                "Isolate patient for 4 days after rash onset",
                "MMR (Measles-Mumps-Rubella) vaccine — best prevention",
                "Hospitalization if complications develop (pneumonia, encephalitis)"
            ]
        },
        "Sickle Cell Disease": {
            "description": "A hereditary blood disorder where red blood cells become rigid and sickle-shaped, blocking blood flow in vessels and causing pain crises, anemia, and organ damage.",
            "causes": "Inherited mutation in the hemoglobin gene (HbS) — autosomal recessive disorder.",
            "tests": [
                "Hemoglobin Electrophoresis (gold standard — confirms HbSS)",
                "Peripheral Blood Smear (shows sickle-shaped cells)",
                "Complete Blood Count (low hemoglobin)",
                "Newborn Screening (heel-prick test)",
                "Genetic Testing",
                "Reticulocyte count"
            ],
            "care": [
                "Hydroxyurea (reduces frequency of pain crises)",
                "Folic acid supplementation (supports red blood cell production)",
                "Pain management during crises: NSAIDs, Opioids",
                "IV fluids during vaso-occlusive crises",
                "Blood transfusions (for severe anemia or stroke)",
                "Bone marrow transplant (only potential cure)",
                "Pneumococcal and other vaccines (high infection risk)",
                "Penicillin prophylaxis in children under 5"
            ]
        },
        "Dengue Fever": {
            "description": "A mosquito-borne viral illness endemic to tropical regions, causing severe flu-like symptoms with high fever, intense body pain, and characteristic skin rash.",
            "causes": "Dengue virus (DENV, 4 serotypes) transmitted by Aedes aegypti and Aedes albopictus mosquitoes.",
            "tests": [
                "NS1 Antigen Test (positive in first 1–5 days of fever)",
                "Dengue IgM and IgG antibody test (after day 5)",
                "Complete Blood Count (low platelet count, elevated hematocrit)",
                "Liver function tests",
                "RT-PCR (most sensitive in early phase)"
            ],
            "care": [
                "No specific antiviral treatment — supportive care",
                "Paracetamol for fever — AVOID Aspirin and Ibuprofen (bleeding risk)",
                "Oral hydration: ORS, coconut water, juices",
                "Monitor platelet count every 24 hours",
                "Rest and avoid physical exertion",
                "Hospitalize if platelet < 50,000 or warning signs appear",
                "Eliminate mosquito breeding sites (stagnant water)",
                "Use mosquito repellents, nets, and full-sleeve clothing"
            ]
        },
        "Liver Cirrhosis": {
            "description": "Advanced-stage liver disease where healthy liver tissue is replaced by scar tissue, permanently impairing liver function. An irreversible but manageable condition.",
            "causes": "Chronic alcohol use, Hepatitis B or C infection, Non-alcoholic fatty liver disease (NAFLD), or autoimmune hepatitis.",
            "tests": [
                "Liver Function Tests (LFT): Bilirubin, ALT, AST, Albumin, PT",
                "Ultrasound abdomen (shows shrunken nodular liver, splenomegaly)",
                "FibroScan (non-invasive liver stiffness measurement)",
                "Liver Biopsy (gold standard for staging)",
                "Endoscopy (esophageal varices detection)",
                "AFP (Alpha-fetoprotein) — screens for liver cancer"
            ],
            "care": [
                "Treat underlying cause (stop alcohol, antiviral for HBV/HCV)",
                "Avoid all alcohol completely",
                "Low-salt diet (reduces fluid retention/ascites)",
                "Diuretics (Spironolactone + Furosemide) for ascites",
                "Beta-blockers (Propranolol) to prevent variceal bleeding",
                "Lactulose (prevents hepatic encephalopathy)",
                "6-monthly ultrasound + AFP for liver cancer surveillance",
                "Liver transplant (only cure for end-stage cirrhosis)"
            ]
        },
        "Chickenpox": {
            "description": "A highly contagious viral infection causing an itchy blister-like rash all over the body. Common in children but can be more severe in adults.",
            "causes": "Varicella-Zoster Virus (VZV), spread through direct contact with blisters or airborne droplets.",
            "tests": [
                "Clinical diagnosis in most cases (characteristic rash)",
                "Tzanck Smear (from vesicle base)",
                "PCR for Varicella-Zoster Virus",
                "VZV IgM antibody (acute infection)",
                "VZV IgG (for immunity confirmation)"
            ],
            "care": [
                "Calamine lotion and antihistamines (Chlorphenamine) for itching",
                "Paracetamol for fever — AVOID Aspirin (risk of Reye's syndrome in children)",
                "Keep nails trimmed short to prevent scratching",
                "Antiviral (Acyclovir) within 24 hours of rash onset (for adults, immunocompromised)",
                "Isolate until all blisters have crusted over (usually day 5–7)",
                "Varicella vaccine (Varivax) — safe and effective prevention",
                "Cool oatmeal baths for skin soothing"
            ]
        },
        "COVID-19": {
            "description": "A respiratory infectious disease caused by SARS-CoV-2 coronavirus, ranging from mild flu-like symptoms to severe pneumonia and multi-organ failure.",
            "causes": "SARS-CoV-2 virus, spread through respiratory droplets, aerosols, and contact with contaminated surfaces.",
            "tests": [
                "RT-PCR nasal/throat swab (gold standard)",
                "Rapid Antigen Test (RAT) — quick but less sensitive",
                "Chest CT or X-ray (ground-glass opacities in pneumonia)",
                "CBC, CRP, D-dimer, IL-6, Ferritin (severity assessment)",
                "SpO2 monitoring (oxygen saturation)"
            ],
            "care": [
                "Rest and isolation for at least 5 days from symptom onset",
                "Paracetamol for fever and body ache",
                "Adequate fluid intake",
                "Monitor SpO2 — seek hospital if below 94%",
                "Antiviral: Nirmatrelvir/Ritonavir (Paxlovid) for high-risk patients",
                "Dexamethasone (for hospitalized patients requiring oxygen)",
                "COVID-19 vaccination — primary prevention",
                "Prone positioning (lie on stomach) if breathing difficulties"
            ]
        },
        "Angina": {
            "description": "Chest pain or discomfort caused by reduced blood flow to the heart muscle, usually due to coronary artery disease. It is a symptom, not a disease, and signals the heart is not getting enough oxygen.",
            "causes": "Narrowing of coronary arteries by atherosclerosis (plaque buildup); can be triggered by exertion, stress, or cold weather.",
            "tests": [
                "ECG (Electrocardiogram) — during pain or stress test",
                "Stress Test / Exercise Treadmill Test (ETT)",
                "Echocardiogram",
                "Coronary Angiography (definitive — shows artery narrowing)",
                "Cardiac CT Angiography",
                "Troponin (to rule out heart attack)"
            ],
            "care": [
                "Sublingual Nitroglycerin (immediate pain relief)",
                "Long-acting nitrates for prevention",
                "Beta-blockers (Metoprolol) — reduce heart workload",
                "Calcium channel blockers",
                "Aspirin (antiplatelet) daily",
                "Statins (lower cholesterol and stabilize plaque)",
                "Lifestyle: quit smoking, low-fat diet, regular exercise",
                "Coronary artery stenting or bypass surgery if severe"
            ]
        },
        "Parkinsons Disease": {
            "description": "A progressive neurological disorder affecting movement, caused by degeneration of dopamine-producing neurons in the brain. Characterized by tremor, rigidity, and slow movement.",
            "causes": "Exact cause unknown; loss of dopaminergic neurons in substantia nigra of brain; genetic and environmental factors.",
            "tests": [
                "Clinical diagnosis by neurologist (no definitive test)",
                "DaTscan (SPECT imaging) — shows dopamine transporter deficit",
                "MRI Brain (to rule out other causes)",
                "UPDRS (Unified Parkinson's Disease Rating Scale) assessment",
                "Response to Levodopa trial (diagnostic clue)"
            ],
            "care": [
                "Levodopa/Carbidopa (most effective — gold standard medication)",
                "Dopamine agonists (Pramipexole, Ropinirole)",
                "MAO-B inhibitors (Rasagiline, Selegiline)",
                "Deep Brain Stimulation (DBS) for advanced cases",
                "Physiotherapy (improves gait and balance)",
                "Speech therapy (if speech affected)",
                "Occupational therapy (daily activities adaptation)",
                "Regular exercise (slows progression)"
            ]
        },
        "Meningitis": {
            "description": "A medical emergency involving inflammation of the meninges (membranes surrounding the brain and spinal cord), usually due to infection. Can be fatal within 24 hours if untreated.",
            "causes": "Bacterial (Neisseria meningitidis, Streptococcus pneumoniae most common), viral (Enteroviruses), or fungal causes.",
            "tests": [
                "Lumbar Puncture / Spinal Tap (CSF analysis — gold standard)",
                "CT Brain (before LP if focal neurological signs present)",
                "Blood Culture",
                "Complete Blood Count",
                "CRP and Procalcitonin (elevated in bacterial)",
                "CSF Gram stain, culture, and PCR"
            ],
            "care": [
                "MEDICAL EMERGENCY — hospitalize immediately",
                "IV antibiotics stat: Ceftriaxone or Benzylpenicillin (do not delay for LP)",
                "Dexamethasone (reduces brain inflammation — start before antibiotics)",
                "IV fluids",
                "Isolate patient (bacterial meningitis is contagious)",
                "Acyclovir if viral (herpes) meningitis suspected",
                "Monitor for raised intracranial pressure, seizures, hearing loss",
                "Meningococcal vaccine and pneumococcal vaccine for prevention"
            ]
        },
        "Cellulitis": {
            "description": "A common bacterial skin infection that affects the deep layers of skin and the tissue beneath it. It appears as a swollen, red area of skin that is warm and tender.",
            "causes": "Bacteria (Staphylococcus aureus and Streptococcus) enter through cuts, wounds, insect bites, or skin cracks.",
            "tests": [
                "Clinical diagnosis (red, warm, swollen, tender skin)",
                "Blood culture (if systemic infection — high fever, sepsis signs)",
                "Complete Blood Count (elevated WBC)",
                "CRP and ESR",
                "Wound swab culture",
                "Ultrasound (to rule out abscess — needs drainage)"
            ],
            "care": [
                "Antibiotics: Cefalexin or Flucloxacillin (mild-moderate oral therapy)",
                "IV Antibiotics (Benzylpenicillin or Flucloxacillin) for severe cases",
                "Elevate the affected limb to reduce swelling",
                "Rest and adequate hydration",
                "Mark the border of redness with pen to monitor spread",
                "Wound cleaning and dressing",
                "Surgical drainage if abscess develops",
                "Treat underlying skin conditions (eczema, athlete's foot) to prevent recurrence"
            ]
        },
        "Rheumatoid Arthritis": {
            "description": "A chronic systemic autoimmune disease primarily affecting the synovial joints, causing inflammation, pain, swelling, and eventual joint destruction — symmetrically affecting both sides.",
            "causes": "Autoimmune attack on joint lining; combination of genetic (HLA-DR4) and environmental factors (smoking, infections).",
            "tests": [
                "Rheumatoid Factor (RF) — positive in ~70%",
                "Anti-CCP antibody (most specific test)",
                "ESR and CRP (inflammatory markers)",
                "Complete Blood Count (anemia of chronic disease)",
                "X-ray of hands and feet (joint erosions in advanced disease)",
                "MRI or Ultrasound of joints (early synovitis detection)"
            ],
            "care": [
                "DMARDs: Methotrexate (cornerstone treatment — start early)",
                "Hydroxychloroquine, Sulfasalazine (combination with MTX)",
                "Biologics: Anti-TNF agents (Etanercept, Adalimumab) if DMARDs fail",
                "JAK inhibitors (Tofacitinib) — newer oral targeted therapy",
                "NSAIDs for pain relief",
                "Corticosteroids for acute flares (short-term)",
                "Regular physiotherapy and joint-protection techniques",
                "Smoking cessation (major risk factor)"
            ]
        },
        "Obesity Hypoventilation": {
            "description": "A condition in obese individuals where excess weight makes it very difficult to breathe properly, especially during sleep, leading to dangerously low oxygen and high CO2 levels in the blood.",
            "causes": "Severe obesity (BMI > 30) causing mechanical restriction of breathing, combined with reduced respiratory drive.",
            "tests": [
                "Arterial Blood Gas (ABG) — shows hypercapnia (high CO2) and hypoxia",
                "Polysomnography (Sleep Study) — for associated Sleep Apnea",
                "Chest X-ray and spirometry",
                "Echocardiogram (right heart failure — Cor Pulmonale)",
                "Serum bicarbonate (chronically elevated)"
            ],
            "care": [
                "Weight loss — most effective treatment",
                "Non-invasive Positive Pressure Ventilation (NIPPV/BiPAP) during sleep",
                "CPAP therapy for associated Obstructive Sleep Apnea",
                "Low-calorie diet and behavioral modification",
                "Bariatric surgery for morbid obesity",
                "Pulmonary rehabilitation",
                "Avoid sedatives and alcohol — worsen hypoventilation",
                "Oxygen therapy if hypoxemia is severe"
            ]
        },
        "Kidney Stones": {
            "description": "Hard mineral and salt deposits that form inside the kidneys. They can affect the urinary tract from the kidneys to the bladder and are extremely painful when passing.",
            "causes": "Dehydration, high sodium/protein diet, family history, obesity, gout, or certain metabolic disorders.",
            "tests": [
                "CT KUB (non-contrast CT of kidney-ureter-bladder) — gold standard",
                "Ultrasound kidney-bladder (first-line, radiation-free)",
                "X-ray KUB (calcium stones visible, uric acid stones are not)",
                "Urine Routine (blood in urine — hematuria)",
                "Serum Calcium, Uric Acid, Phosphate",
                "Stone analysis (if stone is passed or removed)"
            ],
            "care": [
                "Increase water intake to 2.5–3 liters/day (most important preventive measure)",
                "Pain management: NSAIDs (Ketorolac), Tamsulosin (relaxes ureter)",
                "Stones < 5mm: usually pass spontaneously with hydration",
                "ESWL (Shock Wave Lithotripsy) for 5–20mm stones",
                "Ureteroscopy or laser lithotripsy for larger stones",
                "PCNL (Percutaneous Nephrolithotomy) for very large kidney stones",
                "Low-sodium, low-protein diet",
                "Reduce oxalate-rich foods (spinach, nuts) for calcium-oxalate stones"
            ]
        },
        "Sepsis": {
            "description": "A life-threatening medical emergency where the body's response to infection causes widespread inflammation, leading to organ failure. Can progress to septic shock if untreated.",
            "causes": "Can originate from any infection (pneumonia, UTI, abdominal infection, skin infection) caused by bacteria, viruses, or fungi.",
            "tests": [
                "Blood Culture x2 (before antibiotics if possible)",
                "Complete Blood Count",
                "Lactate level (> 2 mmol/L indicates tissue hypoperfusion)",
                "Procalcitonin (bacterial infection marker)",
                "CRP, ESR",
                "Urine culture, Chest X-ray, LFT, RFT",
                "Coagulation profile (DIC risk)"
            ],
            "care": [
                "MEDICAL EMERGENCY — Sepsis 1-hour bundle",
                "IV broad-spectrum antibiotics within 1 hour (Piperacillin-Tazobactam or Meropenem)",
                "IV fluid resuscitation: 30ml/kg crystalloid bolus",
                "Vasopressors (Norepinephrine) if BP doesn't respond to fluids",
                "Oxygen therapy or mechanical ventilation",
                "Source control (drain abscess, remove infected catheter)",
                "ICU admission for monitoring",
                "De-escalate antibiotics based on culture results"
            ]
        },
        "Type 2 Diabetes": {
            "description": "A chronic metabolic disorder where the body either doesn't produce enough insulin or doesn't use it effectively, resulting in high blood sugar levels. Most common type of diabetes.",
            "causes": "Insulin resistance due to obesity, sedentary lifestyle, genetic factors, and poor diet. Develops gradually over years.",
            "tests": [
                "Fasting Blood Glucose (≥ 126 mg/dL on two occasions)",
                "HbA1c (≥ 6.5%) — reflects average blood sugar over 3 months",
                "Oral Glucose Tolerance Test (OGTT)",
                "Postprandial Blood Glucose (2-hour > 200 mg/dL)",
                "Lipid profile, Urine microalbumin, Kidney and liver function"
            ],
            "care": [
                "Lifestyle modification: weight loss, regular exercise, healthy diet (first-line)",
                "Metformin (first-line oral medication)",
                "SGLT2 inhibitors (Empagliflozin) — also protect heart and kidneys",
                "GLP-1 agonists (Semaglutide) — promote weight loss",
                "Insulin therapy (if oral drugs insufficient)",
                "HbA1c check every 3 months",
                "Annual screening for complications: eyes, kidneys, feet, heart",
                "Blood pressure and cholesterol management"
            ]
        },
        "Bronchitis": {
            "description": "Inflammation of the bronchial tubes (airways carrying air to the lungs). Can be acute (short-term, usually following a respiratory infection) or chronic (long-term, often from smoking).",
            "causes": "Acute: Viral infection (influenza, RSV). Chronic: Long-term cigarette smoking or exposure to air pollutants.",
            "tests": [
                "Clinical diagnosis for acute bronchitis",
                "Chest X-ray (to rule out pneumonia)",
                "Spirometry (for chronic bronchitis — part of COPD evaluation)",
                "Sputum culture (if bacterial cause suspected)",
                "Complete Blood Count"
            ],
            "care": [
                "Rest and adequate fluid intake",
                "Honey and warm ginger tea for cough relief",
                "Paracetamol for fever",
                "Bronchodilator inhaler (Salbutamol) for wheeze",
                "Avoid smoke and air pollutants",
                "Antibiotics only if bacterial cause confirmed (unusual)",
                "Quit smoking — critical for chronic bronchitis",
                "Mucolytics (Bromhexine) to thin mucus"
            ]
        },
        "Peptic Ulcer": {
            "description": "Open sores that develop on the lining of the stomach, upper small intestine, or esophagus due to erosion by stomach acid. Helicobacter pylori infection is the most common cause.",
            "causes": "H. pylori bacterial infection (most common), chronic NSAID use (Aspirin, Ibuprofen), or rarely acid hypersecretion (Zollinger-Ellison syndrome).",
            "tests": [
                "Upper GI Endoscopy (OGD) — gold standard, visualizes ulcer directly",
                "H. pylori testing: Urea Breath Test, Stool Antigen Test, or endoscopic biopsy",
                "Barium Meal X-ray (less common today)",
                "Blood test for H. pylori antibodies",
                "Serum Gastrin (to rule out Zollinger-Ellison)"
            ],
            "care": [
                "H. pylori eradication: Triple therapy — PPI + Clarithromycin + Amoxicillin for 14 days",
                "Proton Pump Inhibitors (Omeprazole, Pantoprazole) — reduce acid production",
                "H2 blockers (Ranitidine) as alternative",
                "Stop NSAIDs if possible",
                "Antacids for symptom relief",
                "Avoid spicy food, alcohol, caffeine, smoking",
                "Eat small, frequent meals",
                "Endoscopic therapy or surgery for bleeding or perforated ulcers"
            ]
        },
        "Malaria": {
            "description": "A life-threatening parasitic disease transmitted through bites of infected female Anopheles mosquitoes. Common in tropical and subtropical regions including India, Africa, and Southeast Asia.",
            "causes": "Plasmodium parasites (P. falciparum, P. vivax, P. malariae, P. ovale). P. falciparum causes the most severe disease.",
            "tests": [
                "Peripheral Blood Smear (thick and thin films) — gold standard",
                "Rapid Diagnostic Test (RDT) — rapid antigen detection",
                "Quantitative Buffy Coat (QBC) test",
                "PCR for malaria (most sensitive — used to identify species)",
                "Complete Blood Count (thrombocytopenia is common)"
            ],
            "care": [
                "P. falciparum (severe): IV Artesunate — first-line",
                "Artemisinin-based Combination Therapy (ACT): Artemether-Lumefantrine",
                "P. vivax: Chloroquine + Primaquine (radical cure to prevent relapse)",
                "Antipyretics for fever (Paracetamol)",
                "IV fluids for dehydration",
                "Monitor blood glucose, hemoglobin, and platelet count",
                "Antimalarial prophylaxis for travelers",
                "Insecticide-treated bed nets and mosquito repellents"
            ]
        },
        "Chronic Kidney Disease": {
            "description": "A long-term progressive loss of kidney function over months to years. Often silent in early stages, eventually leading to kidney failure requiring dialysis or transplant.",
            "causes": "Diabetes mellitus (most common), hypertension, glomerulonephritis, recurrent UTIs, or polycystic kidney disease.",
            "tests": [
                "Serum Creatinine and BUN",
                "eGFR (estimated Glomerular Filtration Rate) — staging of CKD (1–5)",
                "Urine Albumin:Creatinine Ratio (microalbuminuria)",
                "Ultrasound kidney (size, echogenicity)",
                "Hemoglobin (anemia of CKD)",
                "Serum Electrolytes (potassium, phosphate, calcium)",
                "Kidney Biopsy (in selected cases to determine cause)"
            ],
            "care": [
                "Control blood pressure strictly (target < 130/80 mmHg)",
                "Blood sugar control if diabetic",
                "ACE inhibitors or ARBs (slow progression, reduce proteinuria)",
                "Low-protein, low-potassium, low-phosphate diet",
                "Avoid NSAIDs and nephrotoxic drugs",
                "Erythropoietin injections for anemia",
                "Phosphate binders (Calcium carbonate) and Vitamin D supplements",
                "Hemodialysis or peritoneal dialysis at stage 5 (eGFR < 15)"
            ]
        },
        "Rubella": {
            "description": "A contagious viral disease characterized by a distinctive pink skin rash. Also called German Measles. Mild in children but extremely dangerous in pregnant women (causes fetal abnormalities).",
            "causes": "Rubella virus, spread via respiratory droplets.",
            "tests": [
                "Rubella IgM antibody (confirms recent infection)",
                "Rubella IgG (confirms immunity or past infection)",
                "Viral PCR from nasopharyngeal swab",
                "Clinical diagnosis (characteristic rash and lymphadenopathy)"
            ],
            "care": [
                "No specific antiviral — supportive care only",
                "Rest and adequate fluid intake",
                "Paracetamol for fever",
                "CRITICAL: Pregnant women exposed to rubella — emergency medical evaluation",
                "MMR (Measles-Mumps-Rubella) vaccine — best prevention",
                "Rubella IgG screening in pre-conception care",
                "Isolate patient from pregnant women"
            ]
        },
        "Osteomyelitis": {
            "description": "A serious infection of the bone, usually caused by bacteria. Can occur in any bone and can be acute (rapid onset) or chronic (develops over time).",
            "causes": "Bacteria (Staphylococcus aureus most common) reaching bone through bloodstream, surgery, trauma, or nearby infection.",
            "tests": [
                "MRI (gold standard — most sensitive for bone marrow changes)",
                "X-ray (bone changes visible only after 10–21 days)",
                "Bone Scan (Technetium-99 scintigraphy)",
                "Complete Blood Count, CRP, ESR, Blood Culture",
                "Bone Biopsy and Culture (identifies causative organism)",
                "White Blood Cell Scan"
            ],
            "care": [
                "Prolonged IV antibiotics: 4–6 weeks (based on culture sensitivity)",
                "Cloxacillin or Vancomycin for Staphylococcal infection",
                "Oral antibiotics thereafter for 4–6 additional weeks",
                "Surgical debridement (removal of infected/dead bone) if chronic",
                "Immobilization of affected limb",
                "Wound management and dressing",
                "Nutritional support and adequate protein intake",
                "Hyperbaric oxygen therapy (adjunctive in chronic cases)"
            ]
        },
        "Gallstones": {
            "description": "Hardened deposits of bile components that form in the gallbladder. Often asymptomatic but can cause severe abdominal pain when they block bile ducts.",
            "causes": "Excess cholesterol in bile, bile salt imbalance, obesity, rapid weight loss, female sex, or pregnancy.",
            "tests": [
                "Ultrasound abdomen (first-line — highly accurate for gallstones)",
                "MRCP (Magnetic Resonance Cholangiopancreatography) for common bile duct stones",
                "ERCP (diagnostic and therapeutic)",
                "CT Scan abdomen",
                "Liver function tests (bilirubin, ALP elevated if bile duct involved)",
                "Complete Blood Count"
            ],
            "care": [
                "Asymptomatic stones: watchful waiting",
                "Laparoscopic Cholecystectomy (surgical removal of gallbladder) — definitive treatment",
                "Low-fat diet to reduce biliary colic",
                "ERCP + stone removal for common bile duct stones",
                "Ursodeoxycholic acid (dissolves small cholesterol stones — slow and limited)",
                "Pain management: NSAIDs, Antispasmodics",
                "Antibiotics if acute cholecystitis (infection of gallbladder)"
            ]
        },
        "Hepatitis B": {
            "description": "A serious liver infection caused by the Hepatitis B virus (HBV). Can be acute or chronic; chronic infection can lead to liver cirrhosis and liver cancer.",
            "causes": "HBV virus transmitted through blood, unprotected sexual contact, sharing needles, or from mother to baby during childbirth.",
            "tests": [
                "HBsAg (Hepatitis B Surface Antigen) — positive indicates infection",
                "Anti-HBs (surface antibody) — indicates immunity/recovery",
                "HBeAg and Anti-HBe (marker of replication activity)",
                "HBV DNA (viral load — quantifies virus in blood)",
                "Liver Function Tests",
                "Liver Biopsy or FibroScan (for fibrosis staging)"
            ],
            "care": [
                "Acute HBV: supportive care (rest, hydration, avoid alcohol)",
                "Chronic HBV antivirals: Tenofovir or Entecavir (long-term, sometimes lifelong)",
                "Regular monitoring: LFT, HBV DNA, AFP every 6 months",
                "Ultrasound every 6 months (liver cancer surveillance)",
                "Avoid alcohol completely",
                "Hepatitis B vaccine + Immunoglobulin for newborns of HBsAg+ mothers",
                "HBV vaccine — 3-dose schedule for all unvaccinated individuals"
            ]
        },
        "Chikungunya": {
            "description": "A viral disease transmitted by Aedes mosquitoes, causing sudden fever and severe joint pain that can persist for months. Joint pain is often the most debilitating symptom.",
            "causes": "Chikungunya virus (CHIKV), transmitted by Aedes aegypti and Aedes albopictus mosquitoes.",
            "tests": [
                "Chikungunya IgM and IgG antibody test (after day 5)",
                "RT-PCR (most sensitive in first 5 days of fever)",
                "Complete Blood Count (low WBC and platelets)",
                "CRP and ESR (elevated)",
                "Clinical diagnosis during outbreak with typical presentation"
            ],
            "care": [
                "No specific antiviral — supportive care",
                "Rest and high fluid intake",
                "Paracetamol for fever and pain — AVOID Aspirin and NSAIDs initially",
                "NSAIDs (Naproxen) can be used after dengue is ruled out",
                "Chloroquine has shown benefit for joint pain in some studies",
                "Joint physiotherapy for prolonged arthralgia",
                "Cold compresses for swollen joints",
                "Mosquito control: repellents, full-sleeve clothing, eliminate stagnant water"
            ]
        },
        "Scabies": {
            "description": "A contagious skin infestation caused by microscopic mites that burrow into the skin, causing intense itching (especially at night) and a pimple-like rash.",
            "causes": "Sarcoptes scabiei mite, spread through prolonged skin-to-skin contact or sharing bedding/clothing with an infected person.",
            "tests": [
                "Clinical diagnosis (itching worse at night, characteristic burrows in webspaces)",
                "Dermoscopy (visualizes mite at burrow end)",
                "Skin scraping microscopy (identifies mite, eggs, or feces)",
                "Ink test (highlights burrow tracks)"
            ],
            "care": [
                "Permethrin 5% cream (apply all over body from neck down, leave 8 hours, wash off) — gold standard",
                "Ivermectin oral (for crusted/Norwegian scabies or treatment failure)",
                "All family members and close contacts should be treated simultaneously",
                "Wash all clothing, bedding, towels in hot water (60°C) and dry in hot dryer",
                "Antihistamines (Cetirizine) for itching",
                "Topical Calamine for itch relief",
                "Itching may persist 2–4 weeks after successful treatment"
            ]
        },
        "Hypertension": {
            "description": "Chronically elevated blood pressure (≥ 140/90 mmHg), often called the 'Silent Killer' because it usually has no symptoms but damages vital organs over time.",
            "causes": "Primary (essential) hypertension — most common, no single cause. Secondary: Kidney disease, sleep apnea, thyroid disorders, or medication side effects.",
            "tests": [
                "Blood Pressure measurement on multiple occasions",
                "Ambulatory Blood Pressure Monitoring (ABPM) — 24-hour monitoring",
                "Blood tests: Electrolytes, Creatinine, Blood Glucose, Lipid Profile",
                "Urine Routine (protein, blood)",
                "ECG (left ventricular hypertrophy)",
                "Echocardiogram",
                "Fundoscopy (hypertensive retinopathy)"
            ],
            "care": [
                "Lifestyle first: low-salt diet (DASH diet), exercise 150 mins/week, weight loss",
                "Quit smoking and limit alcohol",
                "First-line drugs: ACE inhibitors, ARBs, Calcium Channel Blockers, or Thiazide diuretics",
                "Target BP: < 130/80 mmHg (general), < 140/90 in elderly",
                "Regular BP monitoring at home",
                "Manage comorbidities (diabetes, dyslipidemia)",
                "Annual cardiac and kidney function assessment"
            ]
        },
        "Hepatitis C": {
            "description": "A viral liver infection caused by Hepatitis C virus (HCV). Often asymptomatic for decades, gradually causing liver damage, cirrhosis, and liver cancer.",
            "causes": "HCV transmitted primarily through blood (shared needles, blood transfusions before 1992, unsterilized medical equipment). No vaccine exists.",
            "tests": [
                "Anti-HCV antibody test (initial screening)",
                "HCV RNA PCR (confirms active infection, measures viral load)",
                "HCV Genotype (determines treatment regimen)",
                "Liver Function Tests",
                "FibroScan or Liver Biopsy (fibrosis staging)",
                "AFP and Ultrasound (cancer surveillance in cirrhosis)"
            ],
            "care": [
                "Direct-Acting Antivirals (DAAs) — cure rate > 95%",
                "Common regimens: Sofosbuvir + Velpatasvir (Epclusa), Glecaprevir + Pibrentasvir (Mavyret)",
                "Treatment duration: 8–12 weeks typically",
                "SVR (Sustained Virologic Response) = functional cure",
                "Avoid alcohol completely",
                "Regular liver surveillance even after cure if cirrhosis present",
                "No specific vaccine available — prevention through harm reduction"
            ]
        },
        "Leukemia": {
            "description": "Cancer of blood-forming tissues including bone marrow, causing abnormal white blood cell production that crowds out healthy blood cells. Can be acute (fast-growing) or chronic (slow-growing).",
            "causes": "Exact cause often unknown; risk factors include radiation exposure, certain chemicals (benzene), genetic syndromes (Down syndrome), and some viruses.",
            "tests": [
                "Complete Blood Count (very high or abnormal WBC — key finding)",
                "Peripheral Blood Smear (blast cells visible)",
                "Bone Marrow Biopsy and Aspiration (gold standard)",
                "Flow Cytometry (cell type classification)",
                "Cytogenetics / Karyotyping (chromosome analysis)",
                "Molecular markers (BCR-ABL for CML, FLT3 for AML)"
            ],
            "care": [
                "AML: Induction Chemotherapy (Cytarabine + Anthracycline)",
                "ALL: Multi-agent chemotherapy + CNS prophylaxis",
                "CML: Tyrosine Kinase Inhibitors (Imatinib, Nilotinib) — highly effective",
                "CLL: Watchful waiting (early) or Ibrutinib/Venetoclax (advanced)",
                "Allogeneic Stem Cell Transplant (bone marrow transplant) for eligible patients",
                "Supportive: blood transfusions, platelet transfusions, G-CSF",
                "Infection prevention (immunocompromised state)",
                "Regular hematology follow-up and CBC monitoring"
            ]
        },
        "Eczema": {
            "description": "Also known as Atopic Dermatitis. A chronic inflammatory skin condition causing dry, itchy, inflamed skin. Very common in children but can occur at any age.",
            "causes": "Overactive immune response, skin barrier dysfunction, genetic predisposition, allergens, stress, or environmental factors.",
            "tests": [
                "Clinical diagnosis (characteristic distribution and appearance)",
                "Skin Patch Test (to identify contact allergens)",
                "IgE level (often elevated in atopic individuals)",
                "Skin biopsy (rarely needed — to rule out other conditions)",
                "Skin swab (if secondary bacterial infection suspected)"
            ],
            "care": [
                "Regular moisturizing — cornerstone of eczema management (thick emollients)",
                "Topical corticosteroids for flares (Hydrocortisone for mild, Mometasone for moderate)",
                "Topical calcineurin inhibitors (Tacrolimus, Pimecrolimus) — steroid-sparing",
                "Antihistamines for itch (Cetirizine, Fexofenadine)",
                "Avoid triggers: soap, detergents, certain fabrics, stress",
                "Wet wrap therapy for severe flares",
                "Dupilumab (biologic injection) for moderate-severe atopic dermatitis",
                "Short lukewarm baths with gentle, fragrance-free soap"
            ]
        },
        "Migraine": {
            "description": "A neurological condition causing recurrent moderate-to-severe headaches, often on one side of the head, accompanied by nausea, vomiting, and sensitivity to light and sound. Can last 4–72 hours.",
            "causes": "Exact cause unknown; involves brain chemistry changes, trigeminovascular system, and genetic factors. Triggers include stress, hormonal changes, certain foods, and sleep disruption.",
            "tests": [
                "Clinical diagnosis based on ICHD-3 criteria",
                "MRI Brain (to rule out secondary causes in new or atypical headaches)",
                "CT Brain (if sudden severe headache — thunderclap headache)",
                "No specific blood test confirms migraine"
            ],
            "care": [
                "Acute treatment: Triptans (Sumatriptan, Rizatriptan) — migraine-specific",
                "NSAIDs (Ibuprofen, Naproxen) for mild attacks",
                "Antiemetics (Metoclopramide, Ondansetron)",
                "Dark, quiet room and rest during attack",
                "Preventive therapy (if > 4 attacks/month): Propranolol, Topiramate, Amitriptyline",
                "CGRP monoclonal antibodies (Erenumab) — newer preventives",
                "Keep a headache diary to identify triggers",
                "Avoid known triggers: irregular sleep, skipped meals, bright lights, caffeine withdrawal"
            ]
        },
        "Lupus": {
            "description": "Systemic Lupus Erythematosus (SLE) is a chronic autoimmune disease where the immune system attacks its own tissues and organs — affecting skin, joints, kidneys, brain, and other organs.",
            "causes": "Unknown exact cause; combination of genetic predisposition, hormones (more common in women), UV light, infections, and certain medications.",
            "tests": [
                "ANA (Antinuclear Antibody) — screening test, high sensitivity",
                "Anti-dsDNA antibody (specific for SLE)",
                "Anti-Smith antibody (highly specific)",
                "Complement levels (C3, C4 — low during flare)",
                "Complete Blood Count (anemia, low WBC, low platelets)",
                "Urinalysis and 24-hour urine protein (lupus nephritis screening)",
                "Kidney Biopsy (if nephritis suspected)"
            ],
            "care": [
                "Hydroxychloroquine (Plaquenil) — backbone of lupus treatment for all patients",
                "NSAIDs (for joint pain and mild symptoms)",
                "Corticosteroids for flares",
                "Immunosuppressants (Azathioprine, Mycophenolate, Cyclophosphamide) for organ involvement",
                "Belimumab (biologic) for refractory cases",
                "Sun protection (SPF 50+ sunscreen, protective clothing)",
                "Regular monitoring: CBC, renal function, urine protein",
                "Avoid UV light — major trigger for flares"
            ]
        },
        "Anemia": {
            "description": "A condition where there are insufficient healthy red blood cells to carry adequate oxygen to body tissues. Causes fatigue, weakness, and pallor. Has many subtypes depending on the cause.",
            "causes": "Iron deficiency (most common worldwide), B12/folate deficiency, chronic disease, blood loss, hemolysis, or bone marrow failure.",
            "tests": [
                "Complete Blood Count (low hemoglobin, low hematocrit)",
                "Peripheral Blood Smear",
                "Serum Iron, TIBC, Ferritin (iron stores)",
                "Vitamin B12 and Folate levels",
                "Reticulocyte Count (bone marrow response)",
                "Hemoglobin Electrophoresis (sickle cell, thalassemia)",
                "Bone Marrow Biopsy (if aplastic anemia or malignancy suspected)"
            ],
            "care": [
                "Iron deficiency: Oral Iron supplementation (Ferrous Sulfate) with Vitamin C",
                "IV Iron (Ferric Carboxymaltose) if oral not tolerated or severe",
                "B12 deficiency: Cyanocobalamin injections or high-dose oral B12",
                "Folate deficiency: Folic acid supplementation",
                "Blood transfusion for severe symptomatic anemia",
                "Treat underlying cause (bleeding, chronic disease)",
                "Iron-rich diet: red meat, leafy greens, legumes, fortified cereals",
                "Erythropoietin for anemia of chronic kidney disease"
            ]
        },
        "Iron Deficiency": {
            "description": "The most common nutritional deficiency worldwide, where the body lacks enough iron to produce adequate hemoglobin, eventually leading to anemia if untreated.",
            "causes": "Poor dietary iron intake, blood loss (heavy menstruation, GI bleeding), malabsorption (celiac disease), or increased demand (pregnancy, growth).",
            "tests": [
                "Serum Ferritin (most sensitive marker of iron stores — low in deficiency)",
                "Serum Iron (low)",
                "TIBC — Total Iron Binding Capacity (high)",
                "Transferrin Saturation (low)",
                "Complete Blood Count (low hemoglobin, microcytic hypochromic anemia)",
                "Peripheral Blood Smear"
            ],
            "care": [
                "Oral Iron: Ferrous Sulfate or Ferrous Gluconate (elemental iron 150–200mg/day)",
                "Take iron with Vitamin C (enhances absorption)",
                "Take on empty stomach (better absorption, but may cause GI upset)",
                "IV Iron (if oral iron not tolerated or severe deficiency)",
                "Treat underlying cause (GI bleeding, heavy periods)",
                "Iron-rich diet: Red meat, chicken, fish, lentils, spinach, tofu",
                "Avoid tea/coffee/calcium near iron dosing (inhibit absorption)",
                "Recheck CBC and Ferritin after 8–12 weeks"
            ]
        },
        "Mumps": {
            "description": "A contagious viral disease caused by the Mumps virus, primarily affecting the salivary (parotid) glands, causing swelling and pain in the jaw and face.",
            "causes": "Mumps virus (Paramyxovirus), spread through saliva and respiratory droplets.",
            "tests": [
                "Clinical diagnosis (parotid gland swelling — key sign)",
                "Mumps IgM antibody test",
                "Mumps PCR from saliva, urine, or CSF",
                "Serum Amylase (elevated due to parotid inflammation)",
                "Blood CBC"
            ],
            "care": [
                "No specific antiviral — supportive care",
                "Rest and adequate fluid intake",
                "Paracetamol or Ibuprofen for pain and fever",
                "Cold or warm packs on swollen glands for comfort",
                "Soft diet (chewing is painful)",
                "Isolate patient for 5 days from onset of swelling",
                "MMR vaccine — highly effective prevention",
                "Monitor for complications: orchitis in men, meningitis, deafness"
            ]
        },
        "Leptospirosis": {
            "description": "A bacterial zoonotic disease transmitted from animals to humans through water or soil contaminated with infected animal urine. Common during floods. Can cause severe liver and kidney failure.",
            "causes": "Leptospira bacteria, usually contracted through contact with flood water, mud, or urine of infected animals (rats, cattle, dogs).",
            "tests": [
                "Microscopic Agglutination Test (MAT) — gold standard serological test",
                "ELISA IgM antibody (rapid screening)",
                "Leptospira PCR (blood or urine — early diagnosis)",
                "Complete Blood Count, Liver Function Tests, Renal Function Tests",
                "Urine Routine (jaundice + kidney involvement = Weil's disease)"
            ],
            "care": [
                "Antibiotics: Doxycycline (mild cases), IV Penicillin G or Ceftriaxone (severe)",
                "Supportive: IV fluids, dialysis if renal failure (Weil's disease)",
                "Liver and kidney function monitoring",
                "Avoid flood water contact (preventive measure)",
                "Doxycycline prophylaxis for high-risk flood exposure (200mg once weekly)",
                "Protective footwear in endemic areas",
                "Rat control around living areas"
            ]
        },
        "Pericarditis": {
            "description": "Inflammation of the pericardium (the two-layered, fluid-filled sac surrounding the heart), causing sharp chest pain that typically improves on leaning forward.",
            "causes": "Viral infections (most common — Coxsackievirus, Echovirus), bacterial, autoimmune (Lupus), post-heart attack, or trauma.",
            "tests": [
                "ECG (saddle-shaped ST elevation in multiple leads — classic finding)",
                "Echocardiogram (detect pericardial effusion/fluid)",
                "CRP and ESR (elevated)",
                "Complete Blood Count",
                "Troponin (to rule out myocarditis)",
                "Chest X-ray (enlarged cardiac silhouette if large effusion)"
            ],
            "care": [
                "NSAIDs (Ibuprofen or Aspirin) — first-line anti-inflammatory",
                "Colchicine (added to NSAIDs — significantly reduces recurrence)",
                "Rest and avoid strenuous activity for at least 3 months",
                "Corticosteroids for cases not responding to NSAIDs",
                "Treat underlying cause",
                "Pericardiocentesis (needle drainage) if large effusion causing cardiac tamponade"
            ]
        },
        "Hypothyroidism": {
            "description": "A condition where the thyroid gland doesn't produce enough thyroid hormones, slowing down the body's metabolism and causing a wide range of symptoms.",
            "causes": "Hashimoto's thyroiditis (autoimmune — most common), thyroid surgery, radioactive iodine treatment, iodine deficiency, or certain medications (Lithium, Amiodarone).",
            "tests": [
                "TSH (Thyroid Stimulating Hormone) — elevated in hypothyroidism",
                "Free T4 (low in overt hypothyroidism)",
                "Free T3",
                "Anti-TPO antibody (positive in Hashimoto's thyroiditis)",
                "Thyroid Ultrasound",
                "Lipid Profile (hypothyroidism causes dyslipidemia)"
            ],
            "care": [
                "Levothyroxine (T4 replacement) — taken daily, lifelong",
                "Take on empty stomach 30–60 minutes before breakfast",
                "TSH recheck every 6–8 weeks until stable, then every 6 months",
                "Adjust dose during pregnancy (requirement increases)",
                "Iodine-adequate diet (iodized salt)",
                "Avoid taking with calcium, iron, or antacids (reduce absorption)",
                "Selenium supplementation may help in Hashimoto's"
            ]
        },
        "HIV/AIDS": {
            "description": "HIV (Human Immunodeficiency Virus) attacks and destroys CD4 T-cells of the immune system. AIDS (Acquired Immunodeficiency Syndrome) is the advanced stage of HIV infection with severe immune failure.",
            "causes": "HIV virus transmitted through unprotected sexual contact, sharing needles, blood transfusions, or from mother to child during birth/breastfeeding.",
            "tests": [
                "HIV Rapid Antibody Test (ELISA) — screening test",
                "Western Blot (confirmatory test)",
                "HIV RNA PCR / Viral Load (measures virus in blood)",
                "CD4 T-cell Count (staging — < 200/μL = AIDS)",
                "Complete Blood Count, LFT, RFT (baseline before treatment)",
                "STI screening, Hepatitis B/C co-infection testing"
            ],
            "care": [
                "ART (Antiretroviral Therapy) — lifelong, start immediately after diagnosis",
                "Common first-line: Tenofovir + Lamivudine + Dolutegravir",
                "Goal: Undetectable viral load (< 50 copies/mL)",
                "CD4 count and Viral Load monitoring every 3–6 months",
                "PrEP (Pre-Exposure Prophylaxis) for high-risk individuals",
                "PEP (Post-Exposure Prophylaxis) within 72 hours of exposure",
                "Opportunistic infection prophylaxis (Cotrimoxazole if CD4 < 200)",
                "Regular screening for TB, sexually transmitted infections, cervical cancer"
            ]
        },
        "Arrhythmia": {
            "description": "Any disorder of the heart's electrical system that causes the heart to beat too fast (tachycardia), too slow (bradycardia), or irregularly. Ranges from benign to life-threatening.",
            "causes": "Coronary artery disease, heart failure, electrolyte imbalances, thyroid disease, caffeine/alcohol excess, drugs, or genetic conditions.",
            "tests": [
                "ECG (Electrocardiogram) — primary diagnostic tool",
                "24-hour Holter Monitor (continuous ECG monitoring)",
                "Event Monitor (worn for weeks — captures intermittent arrhythmias)",
                "Echocardiogram",
                "Electrophysiology Study (EPS) — maps electrical pathways",
                "Blood: Thyroid function, Electrolytes, CBC"
            ],
            "care": [
                "Antiarrhythmic drugs: Amiodarone, Flecainide, Metoprolol (depends on type)",
                "Anticoagulation (Warfarin or DOACs) for atrial fibrillation (stroke prevention)",
                "Electrical Cardioversion (for AF or SVT restoration)",
                "Catheter Ablation (destroys arrhythmia-causing tissue)",
                "Pacemaker implantation (for bradycardia)",
                "ICD (Implantable Cardioverter Defibrillator) for life-threatening arrhythmias",
                "Avoid caffeine, alcohol, and stimulants",
                "Correct electrolyte imbalances (potassium, magnesium)"
            ]
        },
        "Pleuritis": {
            "description": "Also called Pleurisy. Inflammation of the pleura (the two-layered membrane surrounding the lungs), causing sharp chest pain that worsens with breathing, coughing, or sneezing.",
            "causes": "Viral infection (most common), bacterial pneumonia, TB, pulmonary embolism, Lupus, or rheumatoid arthritis.",
            "tests": [
                "Chest X-ray (detect pleural effusion — fluid)",
                "CT Chest (detailed lung and pleural assessment)",
                "Ultrasound chest (guide fluid aspiration)",
                "Pleural Fluid Analysis (if effusion present — protein, glucose, LDH, cytology)",
                "Blood tests: CBC, CRP, ANA, RF (for underlying cause)"
            ],
            "care": [
                "Treat the underlying cause (antibiotics for bacterial, antivirals for viral)",
                "NSAIDs (Ibuprofen) — reduces inflammation and pain",
                "Colchicine (especially for recurrent pleuritis)",
                "Avoid deep breathing if painful (lie on affected side for comfort)",
                "Thoracentesis (needle drainage) if large pleural effusion",
                "Corticosteroids if autoimmune cause"
            ]
        },
        "Vertigo": {
            "description": "A sensation of spinning or dizziness where you or your surroundings feel like they are moving or rotating. Most commonly caused by inner ear problems.",
            "causes": "BPPV (most common — calcium crystals in inner ear), Meniere's disease, Labyrinthitis, Vestibular neuritis, or rarely brain lesions.",
            "tests": [
                "Dix-Hallpike Maneuver (diagnoses BPPV — positive if nystagmus triggered)",
                "MRI Brain (to rule out central cause — stroke, tumor)",
                "Audiometry (hearing test for Meniere's disease)",
                "Caloric Testing (inner ear function)",
                "Blood tests (electrolytes, glucose, thyroid — rule out metabolic causes)"
            ],
            "care": [
                "BPPV: Epley Maneuver (canalith repositioning — highly effective, immediate relief)",
                "Vestibular suppressants: Prochlorperazine, Betahistine (short-term)",
                "Antihistamines (Cinnarizine) for nausea and vertigo",
                "Vestibular rehabilitation exercises",
                "Avoid sudden head movements",
                "Treat Meniere's: low-salt diet, diuretics, betahistine",
                "Sit or lie down during attacks to prevent falls"
            ]
        },
        "Urticaria": {
            "description": "Commonly known as Hives. A skin reaction causing raised, itchy welts (wheals) that appear suddenly and can occur anywhere on the body. Can be acute or chronic.",
            "causes": "Allergic reactions (foods, drugs, insect stings), infections, autoimmune causes, cold/heat/pressure, or often unknown (chronic idiopathic urticaria).",
            "tests": [
                "Clinical diagnosis in most cases",
                "Allergy skin prick test or specific IgE blood test",
                "Complete Blood Count and ESR",
                "Thyroid function and anti-TPO (autoimmune urticaria link)",
                "Food or drug challenge test",
                "Cold/pressure/dermographism physical testing"
            ],
            "care": [
                "Non-sedating Antihistamines — first-line (Cetirizine, Loratadine, Fexofenadine)",
                "Sedating antihistamines (Chlorphenamine) for nighttime itch",
                "Higher doses of antihistamines for chronic urticaria (up to 4x standard dose)",
                "Omalizumab (anti-IgE biologic injection) for antihistamine-resistant chronic urticaria",
                "Short course oral corticosteroids for severe acute flares",
                "Identify and avoid triggers",
                "Epinephrine (Adrenaline) auto-injector if anaphylaxis risk"
            ]
        },
        "Gout": {
            "description": "A form of inflammatory arthritis caused by excess uric acid in the blood crystallizing in joints, causing sudden severe pain, redness, and swelling — typically in the big toe.",
            "causes": "High purine diet (red meat, organ meat, seafood, alcohol), genetic predisposition, kidney disease, or certain medications (Thiazide diuretics).",
            "tests": [
                "Serum Uric Acid (elevated — >7 mg/dL in men, >6 in women)",
                "Joint Fluid Analysis (identifies monosodium urate crystals — gold standard)",
                "X-ray (punched-out erosions in chronic gout)",
                "Ultrasound (double contour sign — urate deposits)",
                "Blood tests: CBC, Creatinine, Lipid profile",
                "DECT Scan (dual-energy CT — identifies urate deposits)"
            ],
            "care": [
                "Acute attack: NSAIDs (Indomethacin, Naproxen) — first-line",
                "Colchicine (within 12 hours of attack onset — very effective)",
                "Oral corticosteroids if NSAIDs/Colchicine contraindicated",
                "Long-term urate lowering: Allopurinol (target uric acid < 6 mg/dL)",
                "Febuxostat (alternative to Allopurinol)",
                "Increase water intake (2–3 liters/day)",
                "Avoid purine-rich foods: red meat, organ meat, shellfish",
                "Avoid alcohol, especially beer",
                "Lose weight if overweight"
            ]
        },
        "Hepatitis A": {
            "description": "A highly contagious liver infection caused by Hepatitis A virus (HAV). Unlike Hepatitis B and C, it does not become chronic. Most people recover completely within weeks.",
            "causes": "HAV virus transmitted via fecal-oral route — contaminated food/water, or close contact with infected person. Common in areas with poor sanitation.",
            "tests": [
                "Anti-HAV IgM antibody (positive — confirms acute infection)",
                "Anti-HAV IgG antibody (confirms past infection or immunity)",
                "Liver Function Tests (elevated ALT, AST, Bilirubin)",
                "Bilirubin levels (conjugated and unconjugated)",
                "Prothrombin Time (PT) — assesses liver function severity"
            ],
            "care": [
                "No specific antiviral — supportive treatment",
                "Rest and adequate fluid intake",
                "Avoid alcohol completely during recovery (and 6 months after)",
                "High-carbohydrate, low-fat diet",
                "Paracetamol for fever (at low doses — avoid excess in liver disease)",
                "Avoid NSAIDS, sedatives, and hepatotoxic drugs",
                "Hepatitis A vaccine — 2-dose schedule, highly effective prevention",
                "Strict hand hygiene, safe food/water practices"
            ]
        },
    }

    meaning = D.get(disease, {
        "description": "Disease information not found.",
        "causes": "N/A",
        "tests": [],
        "care": []
    })

    return meaning


# ─── Example Usage ───────────────────────────────────────────────────────────
if __name__ == "__main__":
    result = getMeaning("Malaria")
    print("Disease: Malaria")
    print(f"Description: {result['description']}")
    print(f"\nCauses: {result['causes']}")
    print(f"\nDiagnostic Tests:")
    for t in result['tests']:
        print(f"  - {t}")
    print(f"\nTreatment & Care:")
    for c in result['care']:
        print(f"  - {c}")
