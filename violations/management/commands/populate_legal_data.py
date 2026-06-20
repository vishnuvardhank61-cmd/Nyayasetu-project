import os
import django
from django.core.management.base import BaseCommand
from rights.models import FundamentalRight, RightCategory
from violations.models import ViolationSituation

class Command(BaseCommand):
    help = 'Populates the database with simplified legal content (Articles 12-35 and Situations)'

    def handle(self, *args, **options):
        self.stdout.write("Defining categories...")
        # Ensure categories exist
        rights_cat, _ = RightCategory.objects.get_or_create(name="Fundamental Rights")
        
        # --- DATA FOR ARTICLES 12-35 (Engaging & Child-Friendly) ---
        rights_data = [
            {
                "article_number": "12",
                "title": "Who Follows the Rules? (The 'State')",
                "simple_explanation": "Imagine the government is the principal of a giant school. This rule says that ANY office run by the government (like the police, a public hospital, or a government school) MUST obey your Fundamental Rights. They can't make excuses!",
                "legal_explanation": "In this part, 'the State' includes the Government and Parliament of India, State Governments, and all local authorities within the territory of India.",
                "violation_example": "If a government-owned swimming pool refuses to let you enter because of your religion, you can sue them because they count as 'The State'.",
                "what_to_do": "Ensure the organization is run by the government. If they are, you can file a case against them directly in the High Court.",
                "where_to_complain": "Supreme Court of India or High Courts.",
                "court_remedy": "Writ petitions (Mandamus, Certiorari, etc.)",
                "keywords": "government, state, office, police, hospital, school, principal, agency, authority, official, public, municipal, bribery, bribe, demand money, extortion"
            },
            {
                "article_number": "13",
                "title": "The Ultimate Eraser (Bad Laws are Void)",
                "simple_explanation": "The Constitution is the Boss! If any politician or government tries to pass a new law that steals away your rights, this Article acts like a giant eraser and instantly makes that bad law 'null and void' (it gets cancelled!).",
                "legal_explanation": "All laws in force in the territory of India that are inconsistent with Fundamental Rights shall, to the extent of such inconsistency, be void.",
                "violation_example": "If the city council passes a law saying 'Kids aren't allowed to complain about bad roads,' the courts will use Article 13 to completely destroy that rule.",
                "what_to_do": "Challenge the unconstitutional law in a High Court or the Supreme Court.",
                "where_to_complain": "Supreme Court or High Court.",
                "court_remedy": "Judicial Review to strike down the law.",
                "keywords": "bad law, rule, illegal order, council, politician, unconstitutional, cancel, void, rights stolen"
            },
            {
                "article_number": "14",
                "title": "Equality Before the Law",
                "simple_explanation": "The Law wears a blindfold. It doesn't care if you are a billionaire, a famous celebrity, or a normal student. If a famous actor breaks a traffic signal, they face the exact same rule as you do. Absolute equality!",
                "legal_explanation": "The State shall not deny to any person equality before the law or the equal protection of the laws within the territory of India.",
                "violation_example": "If the police let a rich politician's son go free after an accident but arrest a poor driver for the exact same thing, it violates Article 14.",
                "what_to_do": "Point out the discrimination in court and demand Equal Protection.",
                "where_to_complain": "High Court (Article 226) or Supreme Court (Article 32).",
                "court_remedy": "Declaration of the act as discriminatory and unconstitutional.",
                "keywords": "equality, equal, fair, unfair, rich, poor, celebrity, same rule, discrimination, bias, partiality, favor, free, arrest"
            },
            {
                "article_number": "15",
                "title": "Zero Tolerance for Discrimination",
                "simple_explanation": "No one can stop you from entering a park, eating at a restaurant, or using a public water tap just because of your religion, your race, what caste you belong to, or whether you are a boy or a girl. You belong everywhere!",
                "legal_explanation": "The State shall not discriminate against any citizen on grounds only of religion, race, caste, sex, place of birth or any of them.",
                "violation_example": "A shopping mall guard refuses to let a family inside because they are from a specific community or caste.",
                "what_to_do": "Record the incident, gather witnesses, and report it to the police or human rights commission.",
                "where_to_complain": "Local Police Station or Human Rights Commission.",
                "court_remedy": "Orders to stop discrimination and potential compensation.",
                "keywords": "religion, race, caste, sex, gender, boy, girl, birthplace, enter, park, restaurant, mall, shop, water, discrimination, denied access, refuse, banned"
            },
            {
                "article_number": "17",
                "title": "Abolition of Untouchability",
                "simple_explanation": "Treating someone as 'untouchable' is one of the worst crimes in India. It is completely banned. You cannot force someone to sit separately, use different cups, or clean hazardous waste because of their background.",
                "legal_explanation": "'Untouchability' is abolished and its practice in any form is forbidden. It is an offence punishable in accordance with the law.",
                "violation_example": "A tea stall owner keeps separate cups for people of certain castes and refuses to wash them.",
                "what_to_do": "Immediately report to the police under the SC/ST (Prevention of Atrocities) Act. It is a non-bailable crime.",
                "where_to_complain": "Nearest Police Station.",
                "court_remedy": "Strict criminal prosecution and jail time for the offender.",
                "keywords": "untouchable, untouchability, caste, dalit, separate, separate cup, clean, hazardous, discrimination, force, SC/ST, atrocities"
            },
            {
                "article_number": "21",
                "title": "The Right to Life & Personal Liberty",
                "simple_explanation": "This is the most powerful right! It doesn't just mean you get to stay alive; it means you have the right to live with DIGNITY. You have the right to breathe clean air, drink safe water, and have your privacy respected.",
                "legal_explanation": "No person shall be deprived of his life or personal liberty except according to procedure established by law.",
                "violation_example": "A factory dumps toxic chemicals into your neighborhood's water supply, making everyone incredibly sick.",
                "what_to_do": "File a public interest petition (PIL) in the High Court or Supreme Court.",
                "where_to_complain": "High Court or Supreme Court.",
                "court_remedy": "Immediate shutdown of the factory, heavy fines, and cleanup orders.",
                "keywords": "life, liberty, dignity, privacy, clean air, safe water, toxic, pollution, factory, arrest, illegal detention, health, noise, harass, fake encounter, police"
            },
            {
                "article_number": "21A",
                "title": "The Right to Education",
                "simple_explanation": "Education is not a luxury; it is your fundamental right! If you are between 6 and 14 years old, the government MUST provide you with free and compulsory education.",
                "legal_explanation": "The State shall provide free and compulsory education to all children of the age of six to fourteen years.",
                "violation_example": "A government-run school demands a huge 'admission fee' or 'donation' and kicks out a poor student who can't pay.",
                "what_to_do": "Report the greedy school directly to the District Education Officer (DEO).",
                "where_to_complain": "District Education Office or Child Rights Commission.",
                "court_remedy": "Order for immediate free admission and suspension of the school principal.",
                "keywords": "education, school, child, 6 to 14, free, compulsory, admission fee, donation, principal, student, class, study, RTE, right to education"
            },
            {
                "article_number": "24",
                "title": "No Child Labor in Dangerous Places",
                "simple_explanation": "Kids are meant to hold pencils, not power tools! No child under the age of 14 is allowed to work in any dangerous factory, mine, or construction site. Full stop.",
                "legal_explanation": "No child below the age of fourteen years shall be employed to work in any factory or mine or engaged in any other hazardous employment.",
                "violation_example": "You discover a 12-year-old child being forced to make firecrackers in a highly explosive factory.",
                "what_to_do": "Immediately call Childline (1098) or alert the local police. Do not wait.",
                "where_to_complain": "Child Welfare Committee (CWC) or Police.",
                "court_remedy": "Rescue of the child, rehabilitation, and jail for the factory owner.",
                "keywords": "child labor, kids, under 14, work, factory, mine, construction, dangerous, hazardous, forced, childline, 1098, child abuse"
            },
            {
                "article_number": "32",
                "title": "The Heart and Soul: Right to Remedies",
                "simple_explanation": "What good are rules if no one enforces them? Article 32 is your superpower. It says if ANY of your rights are broken, you don't even have to talk to the police—you can go STRAIGHT to the Supreme Court of India for justice!",
                "legal_explanation": "The right to move the Supreme Court by appropriate proceedings for the enforcement of the rights conferred by this Part is guaranteed.",
                "violation_example": "The police illegally lock up an innocent person without letting them see a judge or lawyer.",
                "what_to_do": "A family member or friend can use Article 32 to directly demand the Supreme Court to intervene.",
                "where_to_complain": "Supreme Court of India.",
                "court_remedy": "The Supreme Court issues powerful orders (Writs) like Habeas Corpus to release the person instantly.",
                "keywords": "remedy, justice, supreme court, writ, habeas corpus, illegal lock up, prison, jail, enforce rights, demand, court"
            }
        ]

        # Populate Rights
        for r in rights_data:
            FundamentalRight.objects.update_or_create(
                article_number=r['article_number'],
                defaults={
                    'title': r['title'],
                    'category': rights_cat,
                    'simple_explanation': r['simple_explanation'],
                    'legal_explanation': r['legal_explanation'],
                    'violation_example': r['violation_example'],
                    'what_to_do': r['what_to_do'],
                    'where_to_complain': r['where_to_complain'],
                    'keywords': r.get('keywords', '')
                }
            )

        # --- DATA FOR VIOLATION SITUATIONS ---
        situations_data = [
            # --- TRAFFIC (5) ---
            {
                "title": "Traffic Police seizing vehicle for No License",
                "category": "traffic",
                "is_legal": True,
                "simple_explanation": "Driving without a valid license is illegal, and police have the power to impound your vehicle to ensure road safety.",
                "step_by_step_guide": "1. Do not resist the officer.\n2. Provide your name and address.\n3. Request a formal 'Seizure Memo' or 'Impoundment Receipt'.\n4. Visit the designated RTO or Traffic Court to pay the fine and retrieve your vehicle.",
                "where_to_complain": "Traffic Police Headquarters or Local Magistrate Court.",
                "legal_remedies": "Payment of the fine under the Motor Vehicles Act.",
                "compensation_details": "None, as the action is legal. However, any damage to the vehicle while impounded can be contested.",
                "prevention_tips": "Always carry a digital copy of your DL in mParivahan or DigiLocker.",
                "real_life_example": "Arun was caught driving without his wallet. The bike was seized. He showed his digital DL the next day at court and paid the fine to release it.",
                "landmark_judgment": "S. Rajaseekaran v. Union of India (2014) - The SC emphasized road safety and issued 12 directions including stricter enforcement of license laws."
            },
            {
                "title": "Drunk Driving (DUI) Check",
                "category": "traffic",
                "is_legal": True,
                "simple_explanation": "Driving under the influence of alcohol (above 30mg per 100ml of blood) is a major offence.",
                "step_by_step_guide": "1. Cooperate with the Breathalyzer test.\n2. If you fail, the police can arrest you without a warrant.\n3. The vehicle will be impounded unless someone sober can take it.\n4. You must appear in court; do not try to settle with a bribe.",
                "where_to_complain": "Court (to contest the BAC reading if faulty).",
                "legal_remedies": "Defending the case in court based on procedure irregularities.",
                "compensation_details": "None. Punishments include jail time or heavy fines (₹10,000+).",
                "prevention_tips": "Never drink and drive. Use a cab or a designated driver.",
                "real_life_example": "Sameer was caught at a checkpoint. He tried to argue, but the test was clear. He lost his license for 3 months and paid a ₹10,000 fine.",
                "landmark_judgment": "State of Tamil Nadu v. K. Balu (2017) - The SC banned the sale of liquor within 500 meters of national and state highways to curb drink-driving accidents."
            },
            {
                "title": "Jumping a Red Light",
                "category": "traffic",
                "is_legal": True,
                "simple_explanation": "Violating traffic signals is a punishable offence and causes accidents.",
                "step_by_step_guide": "1. If stopped, ask for a 'Challan'.\n2. Do NOT hand over your original documents if they don't have a valid reason to seize them.\n3. Pay the fine online via the e-Challan portal or at the spot if the machinery is available.",
                "where_to_complain": "Traffic Police Head Office.",
                "legal_remedies": "Contesting the challan in virtual court if the signal was faulty.",
                "compensation_details": "None.",
                "prevention_tips": "Always slow down when the light turns yellow.",
                "real_life_example": "Priya jumped a light at night. An automated camera caught her. She received a message and paid the ₹500 fine online immediately.",
                "landmark_judgment": "M.C. Mehta v. Union of India (1997) - The SC issued specific directions for traffic discipline in Delhi, holding that road safety is a facet of the Right to Life."
            },
            {
                "title": "Seizing a vehicle without a receipt",
                "category": "traffic",
                "is_legal": False,
                "simple_explanation": "Even if the seizure is legal, the officer MUST provide a formal receipt or 'Seizure Memo' immediately.",
                "step_by_step_guide": "1. Demand the receipt persistently.\n2. Note the officer's name and the spot location.\n3. If they refuse, call 112 (Police) and report the theft of the vehicle by an unidentified officer.\n4. Take a video of the officer driving away without giving you papers.",
                "where_to_complain": "Joint Commissioner of Police (Traffic).",
                "legal_remedies": "Complaint of theft or illegal seizure against the officer.",
                "compensation_details": "Restoration of the vehicle with potential departmental action against the officer.",
                "prevention_tips": "Do not leave the spot until you get a document, or have a witness record the event.",
                "real_life_example": "A delivery boy's bike was taken without a memo. He called the helpline, and the officer was forced to issue a back-dated receipt and was later reprimanded.",
                "landmark_judgment": "State represented by Inspector of Police v. N.M.T. Joy Immaculate (2004) - Emphasized that every seizure must be followed by strict procedural documentation."
            },
            {
                "title": "Minor driving a vehicle",
                "category": "traffic",
                "is_legal": False,
                "simple_explanation": "Minors (under 18) are not allowed to drive. The owner/parent of the vehicle is strictly liable for jail time and heavy fines (₹25,000+).",
                "step_by_step_guide": "1. The minor will be taken to juvenile justice board if involved in accident.\n2. The owner will be arrested and charged under the MV Act.\n3. The vehicle registration will be cancelled for 1 year.",
                "where_to_complain": "Local Police Station.",
                "legal_remedies": "Defense in JJB for the minor; criminal defense for the owner.",
                "compensation_details": "Owner must pay massive fines and potentially victims' compensation.",
                "prevention_tips": "Never give keys to children. Educate them on the life-long consequences of a criminal record.",
                "real_life_example": "A 16-year-old took his father's car out. He hit a cyclist. The father was jailed for 3 years, and the family had to pay 10 Lakhs in damages.",
                "landmark_judgment": "Motor Vehicles (Amendment) Act 2019 - Strict provisions making parents/guardians directly responsible for crimes committed by minors using their vehicles."
            },

            # --- POLICE (5) ---
            {
                "title": "Police Officer asking for a bribe",
                "category": "police",
                "is_legal": False,
                "simple_explanation": "Bribery is a serious crime under the Prevention of Corruption Act. No officer can demand money to 'let you go' or 'help' you.",
                "step_by_step_guide": "1. Politely refuse to pay.\n2. Ask for a legal 'Challan' or Receipt.\n3. Note the officer's name and buckle number.\n4. Report the incident to the Anti-Corruption Bureau (ACB).",
                "where_to_complain": "Anti-Corruption Bureau (ACB) or Vigilance Department.",
                "legal_remedies": "Criminal prosecution of the officer.",
                "compensation_details": "No direct money, but helps in cleaning the system.",
                "prevention_tips": "Carry all documents and maintain body-cam or dash-cam if possible.",
                "real_life_example": "A cab driver was asked for ₹200 for 'entry'. He recorded the audio and sent it to the ACB. The officer was suspended following a trap.",
                "landmark_judgment": "P. Sirajuddin v. State of Madras (1970) - The SC held that before public servants are charged with corruption, there must be a thorough preliminary investigation to prevent harassment of honest officers while ensuring the corrupt are caught."
            },
            {
                "title": "Police refusing to file an FIR",
                "category": "police",
                "is_legal": False,
                "simple_explanation": "Registration of an FIR is mandatory for cognizable (serious) offences like theft, assault, or fraud.",
                "step_by_step_guide": "1. Quote the 'Lalita Kumari' Supreme Court judgment.\n2. If refused, send the complaint to the SP/DCP via registered post.\n3. File a 'Zero FIR' elsewhere if needed.\n4. Use Section 156(3) of CrPC/BNSS to ask a Magistrate to order the FIR.",
                "where_to_complain": "SP Office, Commissioner, or Magistrate Court.",
                "legal_remedies": "Writ of Mandamus or Magistrate's order to investigate.",
                "compensation_details": "None directly, but starts the legal engine.",
                "prevention_tips": "Always keep a written, dated copy of your complaint for the SP.",
                "real_life_example": "Ramesh's car was stolen. The local PS said 'find it yourself'. Ramesh went to the SP, who ordered the FIR immediately.",
                "landmark_judgment": "Lalita Kumari v. Govt. of U.P. (2014) - A 5-judge bench of the SC made it mandatory for police to file an FIR if the complaint discloses a cognizable offence."
            },
            {
                "title": "Illegal Detention (More than 24 hours)",
                "category": "police",
                "is_legal": False,
                "simple_explanation": "The Constitution (Article 22) mandates that every arrested person must be produced before a Magistrate within 24 hours (excluding travel time).",
                "step_by_step_guide": "1. Relatives should go to the local Magistrate or High Court immediately.\n2. File a 'Habeas Corpus' petition if the location is unknown.\n3. Request to see the 'Arrest Memo' to verify the time of arrest.",
                "where_to_complain": "High Court (Habeas Corpus) or Magistrate.",
                "legal_remedies": "Immediate release and potential action against the police for illegal confinement.",
                "compensation_details": "Court may grant 'Constitutional Damages' for violation of liberty.",
                "prevention_tips": "Inform a lawyer or family as soon as you are picked up by police.",
                "real_life_example": "A youth was kept in a lockup for 3 days without a judge seeing him. His father filed a petition, and the HC ordered his release and suspended the SHO.",
                "landmark_judgment": "D.K. Basu v. State of West Bengal (1997) - The SC laid down 11 mandatory guidelines for arrest and detention to prevent custodial torture and illegal detention."
            },
            {
                "title": "Police Search of House without a Warrant",
                "category": "police",
                "is_legal": False,
                "simple_explanation": "Police generally need a search warrant from a court to enter your home, unless there's an extreme emergency like chasing a criminal in real-time.",
                "step_by_step_guide": "1. Ask to see the Search Warrant.\n2. Note if they are in uniform and have identity cards.\n3. Ensure two independent witnesses from the neighborhood are present during the search.\n4. Ensure a 'Search Memo' is prepared listing everything seized.",
                "where_to_complain": "Senior Police Officers or Magistrate.",
                "legal_remedies": "Application to declare the search illegal and return seized property.",
                "compensation_details": "None directly, but protects your privacy.",
                "prevention_tips": "Do not let unknown people in without verifying their ID.",
                "real_life_example": "Police raided a student's hostel without a warrant looking for a protest leader. The students successfully challenged this in court as a violation of privacy.",
                "landmark_judgment": "K.S. Puttaswamy v. Union of India (2017) - Declared the Right to Privacy as a Fundamental Right under Article 21, protecting the 'sanctity of the home' from arbitrary entry."
            },
            {
                "title": "Handcuffing without Court Permission",
                "category": "police",
                "is_legal": False,
                "simple_explanation": "Handcuffing is an extreme step and should only be used if the person is likely to escape or is extremely violent. Police need to record the reason in the diary.",
                "step_by_step_guide": "1. Ask why you are being handcuffed if you are cooperating.\n2. Report the handcuffing to the Magistrate as soon as you are produced.\n3. The Magistrate can initiate action against the police for unnecessary humiliation.",
                "where_to_complain": "Magistrate Court.",
                "legal_remedies": "Compensation for the loss of dignity and departmental action against the officer.",
                "compensation_details": "Courts have awarded up to ₹10,000 to ₹50,000 for illegal handcuffing.",
                "prevention_tips": "Stay calm and cooperate visibly so there is no excuse for force.",
                "real_life_example": "A journalist was handcuffed in Odisha after being arrested on a thin charge. The HC criticized the police and ordered a fine on the officers.",
                "landmark_judgment": "Prem Shankar Shukla v. Delhi Administration (1980) - The SC held that handcuffing is an insult to human dignity and shouldn't be used routine or to humiliate."
            },

            # --- WORKPLACE (5) ---
            {
                "title": "Employer refuses to pay salary for 3 months",
                "category": "workplace",
                "is_legal": False,
                "simple_explanation": "Non-payment of wages for work done is a violation of the employment contract and the Payment of Wages Act.",
                "step_by_step_guide": "1. Send a formal demand notice via email/letter.\n2. Collect evidence of your attendance (logs, emails).\n3. File a complaint with the Labor Commissioner.\n4. If no resolution, file a case in Labor Court.",
                "where_to_complain": "Labor Commissioner's Office or Labor Court.",
                "legal_remedies": "Recovery of wages with interest.",
                "compensation_details": "Can claim up to 10 times the unpaid amount as penalty in some cases.",
                "prevention_tips": "Keep copies of your appointment letter and all monthly pay stubs.",
                "real_life_example": "An IT professional was not paid for a quarter. He moved the Labor Court, which froze the company's bank account until he was paid.",
                "landmark_judgment": "State of Punjab v. Jagjit Singh (2016) - The SC applied the principle of 'Equal Pay for Equal Work' for temporary employees as well."
            },
            {
                "title": "Workplace Sexual Harassment (POSH)",
                "category": "workplace",
                "is_legal": False,
                "simple_explanation": "Any unwelcome sexual gesture, physical contact, or demand for sexual favors at work is a crime.",
                "step_by_step_guide": "1. Report to your company's Internal Complaints Committee (ICC) in writing.\n2. Request interim relief (transfer or leave) if needed.\n3. If the company ignores you, go to the Local Complaints Committee (LCC).\n4. You can also file a parallel FIR at the police station.",
                "where_to_complain": "Internal Complaints Committee (ICC) or District Officer.",
                "legal_remedies": "Action under the PoSH Act, 2013 and criminal charges under BNS.",
                "compensation_details": "Victim can be awarded monetary compensation from the perpetrator's salary.",
                "prevention_tips": "Understand your company's PoSH policy. Maintain documentation of all incidents.",
                "real_life_example": "An intern was being harassed by a senior. She complained to the ICC. The ICC conducted an inquiry and recommended the senior's termination.",
                "landmark_judgment": "Vishaka v. State of Rajasthan (1997) - A landmark case where the SC provided guidelines to prevent sexual harassment at workplaces prior to the 2013 Act."
            },
            {
                "title": "Denial of Overtime Pay",
                "category": "workplace",
                "is_legal": False,
                "simple_explanation": "If you work beyond standard hours (usually 8-9 hours), you are entitled to overtime pay at twice the normal rate.",
                "step_by_step_guide": "1. Document your extra hours daily.\n2. Raise the issue with HR politely first.\n3. If rejected, file a complaint with the State Labor Department.\n4. Use your biometric logs as evidence.",
                "where_to_complain": "Labor Inspector or Labor Court.",
                "legal_remedies": "Direction to pay arrears of overtime with penalties.",
                "compensation_details": "Recovery of the due amount.",
                "prevention_tips": "Avoid 'logging out' and then continuing to work; stay on the clock.",
                "real_life_example": "Security guards were being made to work 12 hours but paid for 8. They filed a group complaint and won 2 years of back-dated overtime pay.",
                "landmark_judgment": "Workmen of MTNL v. MTNL (2015) - Emphasized the statutory right of employees to receive overtime wages if they work beyond prescribed limits."
            },
            {
                "title": "Termination during Pregnancy (Maternity Leave)",
                "category": "workplace",
                "is_legal": False,
                "simple_explanation": "It is illegal to fire a woman because of her pregnancy or while she is on maternity leave.",
                "step_by_step_guide": "1. Ensure you have given formal notice of your pregnancy.\n2. If terminated, do not sign any 'voluntary resignation'.\n3. File a complaint under the Maternity Benefit Act with the Labor Commissioner.\n4. Challenge the 'wrongful termination' in court.",
                "where_to_complain": "Labour Commissioner or Civil Court.",
                "legal_remedies": "Reinstatement with full back-wages and benefits.",
                "compensation_details": "Mental agony damages and full maternity pay.",
                "prevention_tips": "Always keep a paper trail of your maternity leave request and approval.",
                "real_life_example": "A woman was told 'not to come back' after her maternity leave. She sued and the company was forced to pay her 2 years' salary as settlement.",
                "landmark_judgment": "Municipal Corporation of Delhi v. Female Workers (2000) - The SC held that maternity benefits are available even to daily-wage workers, as it's a social justice issue."
            },
            {
                "title": "Denial of Safe Drinking Water at Work",
                "category": "workplace",
                "is_legal": False,
                "simple_explanation": "Every employer is mandated by the Factories Act and Shop Act to provide clean drinking water and hygienic toilets.",
                "step_by_step_guide": "1. Talk to your union or fellow workers.\n2. Note the lack of hygiene with photos.\n3. File a complaint with the Factory Inspector or Labor Officer.\n4. If it causes health issues, report to the Health Department.",
                "where_to_complain": "Factory Inspector or Local Municipality.",
                "legal_remedies": "Fines on employer and order to rectify facilities immediately.",
                "compensation_details": "None directly, but saves your health.",
                "prevention_tips": "Inspect the workplace facilities before signing the contract.",
                "real_life_example": "Women in a garment factory fell sick due to dirty water. They complained to the SDM, who shut the factory for 2 days until a RO purifier was installed.",
                "landmark_judgment": "Occupational Health and Safety Code 2020 - Consolidates basic rights of workers including water, lighting, and ventilation as mandatory standards."
            },

            # --- DOMESTIC (5) ---
            {
                "title": "Domestic Violence (Physical/Emotional)",
                "category": "domestic",
                "is_legal": False,
                "simple_explanation": "Violence or threats within a domestic relationship is a crime, regardless of whether it's by a spouse or relative.",
                "step_by_step_guide": "1. Get to a safe place immediately.\n2. Call 181 (Women's Helpline) or 112 (Police).\n3. Go to a hospital for a medical report even for small injuries.\n4. Contact a Protection Officer to file a 'Domestic Incident Report' (DIR).\n5. File for a protection or residence order in court.",
                "where_to_complain": "Women's Helpline (181), Police (112), or Protection Officer.",
                "legal_remedies": "Protection orders, monetary relief, and custody under the DV Act.",
                "compensation_details": "Monthly maintenance and medical coverage.",
                "prevention_tips": "Keep a 'Safety Bag' with your ID and money in case you need to flee.",
                "real_life_example": "Sarita was being beaten by her in-laws. She called 181, stayed in a shelter, and the court ordered her in-laws to leave the house so she could live there safely.",
                "landmark_judgment": "Satish Chander Ahuja v. Sneha Ahuja (2020) - The SC clarified that 'shared household' includes properties where the woman lives, even if they aren't owned by the husband."
            },
            {
                "title": "Dowry Demand after Marriage",
                "category": "domestic",
                "is_legal": False,
                "simple_explanation": "Demanding cash or gifts as a condition of marriage is a serious crime under the Dowry Prohibition Act.",
                "step_by_step_guide": "1. Record any phone calls or save messages where demands are made.\n2. Report to the local police or the Dowry Prohibition Officer.\n3. Do NOT give in to the demands as it usually leads to more harassment.\n4. File an FIR under Section 498A (Cruelty) if it accompanies harassment.",
                "where_to_complain": "Police Station or Dowry Prohibition Officer.",
                "legal_remedies": "Arrest of the offenders and return of any dowry items already given.",
                "compensation_details": "None, but offenders face up to 5-7 years in jail.",
                "prevention_tips": "Maintain a clear list of customary bridal gifts signed by both families to prevent them from being called 'dowry' later.",
                "real_life_example": "Kavita's husband's family demanded a car 1 year after marriage. She filed a complaint with evidence, and the police arrested the husband and his parents.",
                "landmark_judgment": "Arnesh Kumar v. State of Bihar (2014) - The SC issued guidelines to prevent arbitrary arrests in 498A cases while ensuring genuine victims are protected."
            },
            {
                "title": "Refusal to pay Maintenance to Parents",
                "category": "domestic",
                "is_legal": False,
                "simple_explanation": "Children (sons and daughters) are legally obligated to maintain their elderly parents if the parents cannot sustain themselves.",
                "step_by_step_guide": "1. Parents can file an application at the Maintenance Tribunal (at the SDM level).\n2. No lawyer is strictly required for parents to file this.\n3. The Tribunal can order children to pay a monthly amount (max ₹10,000 usually, varies by state).\n4. Non-payment can lead to jail time for the children.",
                "where_to_complain": "Maintenance Tribunal / SDM Office.",
                "legal_remedies": "Monthly maintenance orders under the Senior Citizens Act.",
                "compensation_details": "Direct monthly cash deposit to parents' accounts.",
                "prevention_tips": "Seniors should know about the Maintenance Act before transferring all property to children.",
                "real_life_example": "An 80-year-old was left at a bus stand. He approached the SDM, who ordered his triplets to pay ₹3,000 each per month and return him to his house.",
                "landmark_judgment": "Sunny Paul v. State of NCT Delhi (2017) - The High Court held that parents can even evict abusive children from their property under the Maintenance Act."
            },
            {
                "title": "Triple Talaq (Instant Divorce)",
                "category": "domestic",
                "is_legal": False,
                "simple_explanation": "The practice of instant 'Triple Talaq' has been declared criminal and unconstitutional. It has NO legal effect now.",
                "step_by_step_guide": "1. If a husband gives instant talaq, do NOT leave the house.\n2. Inform the nearest police station immediately.\n3. The husband can be jailed for up to 3 years.\n4. You are entitled to subsistence allowance and custody of children.",
                "where_to_complain": "Police Station.",
                "legal_remedies": "Criminal case under the Muslim Women (Protection of Rights on Marriage) Act.",
                "compensation_details": "Subsistence allowance for lifestyle maintenance.",
                "prevention_tips": "Know your rights in a Nikahnama; you can add conditions against multiple marriages.",
                "real_life_example": "A Woman was given talaq over WhatsApp. She filed an FIR. The husband was arrested, and the court declared the talaq void, ordering him to pay her monthly expenses.",
                "landmark_judgment": "Shayara Bano v. Union of India (2017) - The SC declared instant triple talaq unconstitutional by a 3:2 majority, calling it 'arbitrary' and 'whimsical'."
            },
            {
                "title": "Parental opposition to Inter-caste Marriage",
                "category": "domestic",
                "is_legal": True,
                "simple_explanation": "As long as you are adults (18F / 21M), you have the right to marry anyone of your choice. Parents cannot legally stop or threaten you.",
                "step_by_step_guide": "1. Marry under the Special Marriage Act or personal laws.\n2. If threatened with 'honor killing', move the High Court for 'Protection of Life'.\n3. Inform the local SP about the threat.\n4. Stay in a safe-house if provided by the state.",
                "where_to_complain": "High Court (for Protection) or SP Office.",
                "legal_remedies": "Police protection orders and arrest of family members for intimidation.",
                "compensation_details": "None, but ensures life safety.",
                "prevention_tips": "Register your marriage immediately to get a legal certificate.",
                "real_life_example": "A couple from different castes fled to Delhi. The boy's family threatened them. They approached the HC, which ordered the police to provide them a safe-room for 1 month.",
                "landmark_judgment": "Lata Singh v. State of U.P. (2006) - The SC held that once a person is a major, they can marry whomever they like and no one, including parents, can threaten them."
            },

            # --- DISCRIMINATION (5) ---
            {
                "title": "Discrimination in Renting a House",
                "category": "discrimination",
                "is_legal": False,
                "simple_explanation": "Refusing to rent based on caste, religion, or community is against constitutional values of equality.",
                "step_by_step_guide": "1. Try to get the refusal reason in writing or on record.\n2. Report to the local police if it involves caste slurs (SC/ST Act).\n3. If it's a large society, complain to the Registrar of Societies.\n4. Highlight the issue on social media to build community pressure.",
                "where_to_complain": "Police Station or Registrar of Societies.",
                "legal_remedies": "Prosecution under the SC/ST Act if applicable.",
                "compensation_details": "None directly, but helps change society rules.",
                "prevention_tips": "Always ask for society 'Bylaws' to see if their rules are actually legal.",
                "real_life_example": "Bachelors were banned from a society. They challenged the bylaws in court, and the judge ruled that 'food habits' or 'marital status' cannot be used to ban residents.",
                "landmark_judgment": "Zoroastrian Co-operative Housing Society v. District Registrar (2005) - Ironically allowed some restrictive membership, but newer rulings lean towards Article 15(2) forbidding discrimination in public housing."
            },
            {
                "title": "Denial of Entry to Public Temple or Well",
                "category": "discrimination",
                "is_legal": False,
                "simple_explanation": "Article 17 abolished Untouchability. Any denial of access to public resources on the basis of caste is a major crime.",
                "step_by_step_guide": "1. Record the incident if possible.\n2. File an immediate FIR under the Protection of Civil Rights Act.\n3. Inform the District Magistrate (DM) of the social discrimination.\n4. Contact a human rights NGO for legal backing.",
                "where_to_complain": "Local Police Station (PCR Act) or District Magistrate.",
                "legal_remedies": "Mandatory entry with police protection and criminal charges for the discriminators.",
                "compensation_details": "Severe fines on the offenders.",
                "prevention_tips": "Be aware of local 'customs' that might be illegal; do not fear to challenge then.",
                "real_life_example": "A community was stopped from using a village pond. The DM intervened, personally escorted them to the pond, and filed cases against the villagers who threatened them.",
                "landmark_judgment": "Indian Young Lawyers Association v. State of Kerala (2018) - The Sabarimala verdict, emphasizing that biological factors (menstruation) cannot be used to discriminate in religious places."
            },
            {
                "title": "Caste-based Slurs in Public",
                "category": "discrimination",
                "is_legal": False,
                "simple_explanation": "Using derogatory caste names in a public place with intent to humiliate is a non-bailable offence.",
                "step_by_step_guide": "1. Maintain composure and do not retaliate with violence.\n2. Note down the exact words used and the names of any witnesses present.\n3. File a complaint under the SC/ST Atrocities Act at the nearest station.\n4. Ensure the FIR is filed under the correct sections of the Atrocities Act.",
                "where_to_complain": "Police Station (SC/ST Wing).",
                "legal_remedies": "Immediate arrest of the perpetrator without bail in most cases.",
                "compensation_details": "Victims are entitled to monetary compensation from the government for the humiliation suffered.",
                "prevention_tips": "Report the very first instance of such abuse to discourage future incidents.",
                "real_life_example": "A man was insulted at his workplace using caste slurs. He filed a case, the offender was arrested, and the government provided ₹50,000 as immediate relief to the victim.",
                "landmark_judgment": "Hitesh Verma v. State of Uttarakhand (2020) - Clarified that for an offence under the SC/ST Act, the insult must occur within 'public view'."
            },
            {
                "title": "Discrimination against Transgender Persons",
                "category": "discrimination",
                "is_legal": False,
                "simple_explanation": "Transgender persons have equal rights to education, employment, and healthcare. Harassing them is a crime.",
                "step_by_step_guide": "1. If denied a job/admission, send a legal notice quoting the NALSA judgment.\n2. File a complaint with the National/State Council for Transgender Persons.\n3. Report physical harassment to the local police.",
                "where_to_complain": "Police Station or Transgender Welfare Board.",
                "legal_remedies": "Enforcement of the Transgender Persons (Protection of Rights) Act 2019.",
                "compensation_details": "Action against employers/institutions for discrimination.",
                "prevention_tips": "Apply for the Transgender ID card provided by the government to ease documentation.",
                "real_life_example": "A transwoman was denied a room in a hostel. She sued, and the court ordered the hostel to provide her a room and fined the warden.",
                "landmark_judgment": "National Legal Services Authority (NALSA) v. Union of India (2014) - The SC recognized transgender people as a 'third gender' and granted them fundamental rights."
            },
            {
                "title": "Schools refusing admission based on EWS status",
                "category": "discrimination",
                "is_legal": False,
                "simple_explanation": "RTE Act mandates 25% seats for Economically Weaker Section (EWS) students. A private school cannot refuse admission if selected in the lottery.",
                "step_by_step_guide": "1. Keep the lottery allotment letter safe.\n2. If school refuses, report to the District Education Officer (DEO).\n3. File a complaint on the state's RTE portal.\n4. If still no admission, file a writ petition in the High Court.",
                "where_to_complain": "District Education Officer or RTE Helpline.",
                "legal_remedies": "Magistrate's order to admit the child and cancellation of school's recognition.",
                "compensation_details": "None directly, but secures child's future.",
                "prevention_tips": "Double-check your income certificate for any spelling errors as schools use them to reject kids.",
                "real_life_example": "A gardener's son was denied admission in a top school despite winning the lottery. The DEO visited the school and personally ensured the child was admitted within 48 hours.",
                "landmark_judgment": "Society for Unaided Private Schools v. Union of India (2012) - The SC upheld the constitutionality of the RTE Act's 25% quota for underprivileged children."
            },

            # --- MEDICAL (5) ---
            {
                "title": "Hospital refusing Emergency Treatment",
                "category": "medical",
                "is_legal": False,
                "simple_explanation": "Right to Life (Article 21) means no hospital can deny emergency care just because you can't pay immediately.",
                "step_by_step_guide": "1. Remind the hospital of the 'Parmanand Katara' case.\n2. Call 112 or local police to the hospital.\n3. If you have to pay, keep the receipt as proof for later legal action.\n4. Take a video of the refusal if safe.",
                "where_to_complain": "Chief Medical Officer (CMO) or State Medical Council.",
                "legal_remedies": "Cancellation of hospital license and negligence suits.",
                "compensation_details": "Damages if the delay led to health complications or death.",
                "prevention_tips": "Identify 'Network Hospitals' of your insurance or government schemes like Ayushman Bharat.",
                "real_life_example": "A private hospital refused to admit a heart patient without a ₹50,000 deposit. The patient's son called the police. The hospital was forced to admit him and later fined ₹5 Lakhs by the Health Dept.",
                "landmark_judgment": "Parmanand Katara v. Union of India (1989) - The SC ruled that every doctor/hospital has a total obligation to provide medical assistance to preserve life without waiting for legal formalities."
            },
            {
                "title": "Overcharging for Medicines/MRP Violation",
                "category": "medical",
                "is_legal": False,
                "simple_explanation": "Selling medicines above the Maximum Retail Price (MRP) or charging for free government supplies is illegal.",
                "step_by_step_guide": "1. Check the MRP on the back of the medicine leaf.\n2. Ask for a printed bill (never take a handwritten slip).\n3. If overcharged, complain to the Drug Inspector or on the 'Pharma Sahi Daam' app.\n4. Contact the National Consumer Helpline.",
                "where_to_complain": "Drug Inspector or Pharma Sahi Daam App.",
                "legal_remedies": "Seizure of stock and cancellation of chemist's license.",
                "compensation_details": "Refund of the extra amount paid.",
                "prevention_tips": "Compare prices on online pharmacy apps to know the real cost.",
                "real_life_example": "A pharmacy sold masks during COVID for 10x the price. A customer reported them. The Drug Inspector raided and sealed the shop within 24 hours.",
                "landmark_judgment": "Essential Commodities Act (1955) - Powers the government to control prices and distribution of essential items including life-saving drugs."
            },
            {
                "title": "Detaining a Patient for Unpaid Bills",
                "category": "medical",
                "is_legal": False,
                "simple_explanation": "A hospital cannot 'imprison' or refuse to discharge a patient simply because the bill hasn't been paid fully.",
                "step_by_step_guide": "1. Request a detailed bill break-up.\n2. Inform the hospital that detention is a crime (unlawful confinement).\n3. Relatives should call the police (112) to the hospital.\n4. Offer to pay a portion and provide a written undertaking for the rest to get discharge.\n5. File a police complaint for illegal detention.",
                "where_to_complain": "Local Police Station or Human Rights Commission.",
                "legal_remedies": "Writ of Habeas Corpus to release the patient immediately.",
                "compensation_details": "Damages for the time spent in illegal confinement.",
                "prevention_tips": "Ask for 'estimated costs' in writing at the time of admission.",
                "real_life_example": "A hospital refused to let a woman take her baby home until 2 Lakhs were paid. The HC took up the case and ruled that hospitals ARE NOT jailors; they must use civil courts for debt recovery, not detention.",
                "landmark_judgment": "Deepti Bhandari v. State of Maharashtra (2014) - The High Court slammed a hospital for detaining a patient and clearly stated that hospitals have no right to keep anybody under detention for unpaid bills."
            },
            {
                "title": "Medical Negligence (Wrong surgery/treatment)",
                "category": "medical",
                "is_legal": False,
                "simple_explanation": "If a doctor fails to exercise a reasonable degree of care resulting in injury or death, it is medical negligence.",
                "step_by_step_guide": "1. Collect all original medical records and test reports.\n2. Get an opinion from another independent doctor about the mistake.\n3. File a complaint with the State Medical Council for license suspension.\n4. File a case in Consumer Court for compensation.",
                "where_to_complain": "State Medical Council or Consumer Forum.",
                "legal_remedies": "Cancellation of doctor's license and heavy monetary compensation.",
                "compensation_details": "Recent awards have gone from 5 Lakhs to 11 Crores depending on the severity.",
                "prevention_tips": "Always get a 'Second Opinion' for major surgeries.",
                "real_life_example": "A surgeon left a sponge inside a patient. The patient suffered for a year. The Consumer court awarded 15 Lakhs and the doctor's license was suspended for 6 months.",
                "landmark_judgment": "Jacob Mathew v. State of Punjab (2005) - The SC laid down guidelines for criminal prosecution of doctors, stating they shouldn't be harassed but also shouldn't be exempt from gross negligence."
            },
            {
                "title": "Retention of Dead Body for Bills",
                "category": "medical",
                "is_legal": False,
                "simple_explanation": "Hospitals MUST release the dead body of a patient to their relatives immediately. Delaying it for money is a violation of human dignity.",
                "step_by_step_guide": "1. Do not sign any 'IOU' under pressure.\n2. Call the police (112) to the hospital immediately.\n3. File a complaint for 'Criminal Intimidation' and 'Unlawful Confinement' of the body.\n4. Report the hospital to the Health Minister/Portal.",
                "where_to_complain": "Local Police and SDM.",
                "legal_remedies": "Direction to release the body immediately and heavy fines on the hospital.",
                "compensation_details": "Compensation for mental trauma as high as 10-20 Lakhs.",
                "prevention_tips": "If a hospital starts demanding money daily, seek a transfer to a government facility early.",
                "real_life_example": "A family had to wait 24 hours to get their father's body. The High Court intervened and not only ordered the release but made the hospital waive the entire bill due to their unethical behavior.",
                "landmark_judgment": "Common Cause v. Union of India (2018) - Emphasized the right to die with dignity and that the 'dignity' includes fair treatment of the body as well."
            },

            # --- CONSUMER (5) ---
            {
                "title": "Ecommerce Fraud (Fake product received)",
                "category": "consumer",
                "is_legal": False,
                "simple_explanation": "If a platform sends a wrong or fake item and ignores your return request, it's a violation of consumer rights.",
                "step_by_step_guide": "1. ALWAYS film an unboxing video for high-value items.\n2. Raise a complaint on the official app/website immediately.\n3. If rejected, call the National Consumer Helpline (1915).\n4. File an online case at 'e-Daakhil' portal.\n5. Send a formal legal notice to the company's head office.",
                "where_to_complain": "National Consumer Helpline (1915) or e-Daakhil Portal.",
                "legal_remedies": "Refund plus interest plus compensation for mental agony.",
                "compensation_details": "Can often get 2-3 times the value of the product as damages.",
                "prevention_tips": "Check seller ratings and never buy from unknown Instagram/FB shops without COD.",
                "real_life_example": "Anil got a soap bar instead of a phone. He had a video. The consumer court ordered the company to pay him ₹50,000 for the harassment and refund the phone cost.",
                "landmark_judgment": "Consumer Protection Act 2019 - Includes E-commerce for the first time, making platforms liable for the products sold by their sellers."
            },
            {
                "title": "Insurance Claim Denial without Reason",
                "category": "consumer",
                "is_legal": False,
                "simple_explanation": "Insurance companies often deny claims using 'complicated fine print'. You have the right to a clear, written reason for denial.",
                "step_by_step_guide": "1. Request the 'Rejection Letter' with specific clause numbers.\n2. Complain to the company's internal Grievance Redressal Officer (GRO).\n3. If not resolved in 30 days, approach the Insurance Ombudsman (totally free).\n4. File a Consumer Court case if the amount is high.",
                "where_to_complain": "Insurance Ombudsman or IRDAI (Bima Bharosa).",
                "legal_remedies": "Order for full payment of claim with interest.",
                "compensation_details": "Benefit as per the insurance policy.",
                "prevention_tips": "Never hide 'Pre-existing diseases' while buying; it's the main reason for denial.",
                "real_life_example": "A man's heart surgery claim was denied. He went to the Ombudsman, who found the denial was based on an illegal interpretation. The company had to pay the full 4 Lakhs within 15 days.",
                "landmark_judgment": "Amrit Lal Sood v. Kaushalya Devi (1998) - The SC held that insurance companies cannot escape liability simply because of some obscure policy language."
            },
            {
                "title": "False Advertising (Misleading Promises)",
                "category": "consumer",
                "is_legal": False,
                "simple_explanation": "If a product claims to do something (e.g. 'grow hair in 3 days') and it's scientifically impossible, it is 'Misleading Advertising'.",
                "step_by_step_guide": "1. Save the advertisement (take a screenshot/photo).\n2. Report the ad to the 'Advertisements Standards Council of India' (ASCI).\n3. File a complaint with the CCPA (Central Consumer Protection Authority).\n4. Demand a refund from the brand.",
                "where_to_complain": "CCPA or ASCI.",
                "legal_remedies": "Banning of the ad and heavy fines on the brand and celebrity endorser.",
                "compensation_details": "Refund of the product cost.",
                "prevention_tips": "If a product sounds too good to be true, it probably is.",
                "real_life_example": "A coaching center claimed all top 10 rankers were their students. CCPA found it false and fined them ₹10 Lakhs for misleading parents.",
                "landmark_judgment": "Consumer Protection (Misleading Advertisements) Guidelines 2022 - Holds celebrities equally liable for the false claims made in ads they endorse."
            },
            {
                "title": "MRP Violations (Selling above price)",
                "category": "consumer",
                "is_legal": False,
                "simple_explanation": "It's illegal to sell any packaged item above the MRP (Maximum Retail Price). Hotels/Airports cannot charge extra for 'service' on packaged water.",
                "step_by_step_guide": "1. Point out the MRP on the bottle/pack.\n2. If they insist, pay and take a bill showing the higher price.\n3. Tweet/Mail the screenshot of the bill to the Metrology Department of your state.\n4. Call 1915 (Consumer Helpline) immediately.",
                "where_to_complain": "Metrology Department or National Consumer Helpline.",
                "legal_remedies": "Seizure of stock and cancellation of business license.",
                "compensation_details": "Refund of the extra amount.",
                "prevention_tips": "Always check the bottom or back of the bottle/packet for the price before ordering.",
                "real_life_example": "A multiplex was selling water for ₹60 when MRP was ₹20. A girl sued them and won ₹15,000 as compensation for her fight.",
                "landmark_judgment": "Federation of Hotels and Restaurants Association of India v. Union of India (2017) - Initially allowed hotels to charge extra for service, but newer Legal Metrology rules strictly enforce MRP on all packaged goods."
            },
            {
                "title": "Banks calling at odd hours for recovery",
                "category": "consumer",
                "is_legal": False,
                "simple_explanation": "Recovery agents cannot harass you. They can ONLY call between 8 AM and 7 PM and cannot use abusive language.",
                "step_by_step_guide": "1. Record all abusive calls.\n2. Note the agent's name and the bank they claim to represent.\n3. Complain to the Bank Manager first.\n4. If no change, file a complaint with the RBI Banking Ombudsman.",
                "where_to_complain": "RBI Banking Ombudsman (CMS Portal).",
                "legal_remedies": "Heavy penalty on the bank and compensation for harassment.",
                "compensation_details": "RBI has fined banks up to 1 Crore for aggressive recovery tactics.",
                "prevention_tips": "Do not share contacts of your friends/family with recovery agents; it is a privacy violation.",
                "real_life_example": "A man's neighbors were called and told about his debt. He went to the Ombudsman, and the bank was forced to apologize and pay him ₹25,000 for the loss of reputation.",
                "landmark_judgment": "ICICI Bank v. Shanti Devi (2008) - The SC held that banks cannot use muscle-men for recovery; they must follow the law of the land."
            },

            # --- OTHER (5) ---
            {
                "title": "Cyber Harassment or Revenge Porn",
                "category": "other",
                "is_legal": False,
                "simple_explanation": "Sharing private photos online without consent or harassing someone via digital platforms is a highly grave crime.",
                "step_by_step_guide": "1. Do NOT delete anything; take screenshots immediately.\n2. Record the URL of the offending profile/website.\n3. Report to the portal (cybercrime.gov.in).\n4. Use the 'StopNCII.org' tool to prevent the spread of photos.\n5. Visit the nearest Cyber Police Station.",
                "where_to_complain": "Cyber Crime Portal (cybercrime.gov.in) or Cyber Cell.",
                "legal_remedies": "Removal of content and arrest under the IT Act and BNS.",
                "compensation_details": "No direct money, but protects your dignity.",
                "prevention_tips": "Never share sensitive passwords or private media even with close friends.",
                "real_life_example": "A student's account was hacked and private chats leaked. She went to the Cyber Cell, who tracked the hacker and removed all data from the servers within 24 hours.",
                "landmark_judgment": "State of West Bengal v. Animesh Boxi (2018) - The first case in India where a person was convicted for 'Cyber Pornography' and 'Revenge Porn' using digital evidence."
            },
            {
                "title": "Public Nuisance (Noise/Garbage)",
                "category": "other",
                "is_legal": False,
                "simple_explanation": "Loudspeakers after 10 PM or dumping garbage in public places is a violation of environmental and public laws.",
                "step_by_step_guide": "1. Call 112 (Police) for noise after 10 PM.\n2. For garbage, take a photo and upload it on your city's 'Swachhata App'.\n3. File a complaint with the local Municipality or RWA.\n4. Request the SDM to take action under Section 133 of CrPC for public nuisance.",
                "where_to_complain": "Local Municipality or Police (112).",
                "legal_remedies": "Cease and Desist orders and fines on the nuisance makers.",
                "compensation_details": "None, but improves living conditions.",
                "prevention_tips": "Know your local noise-level limits for residential areas.",
                "real_life_example": "A factory was running 24/7 in a residential area. Neighbors used the 'Nuisance' law to move the court. The court ordered the factory to sound-proof or shut down at night.",
                "landmark_judgment": "Noise Pollution (Regulation and Control) Rules 2000 - Strictly bans the use of loudspeakers between 10:00 PM and 6:00 AM."
            },
            {
                "title": "Animal Cruelty (Beating/Starving Pets)",
                "category": "other",
                "is_legal": False,
                "simple_explanation": "Animals have constitutional rights to be treated with compassion. Hurting them is a crime.",
                "step_by_step_guide": "1. Take a video as evidence if you see abuse.\n2. Call an Animal Welfare NGO or the local police.\n3. File an FIR under the Prevention of Cruelty to Animals Act.\n4. Call for the 'rescue' of the animal if it's in danger.",
                "where_to_complain": "Local Police or Animal Welfare Board of India.",
                "legal_remedies": "Fines and imprisonment for the owner/abuser.",
                "compensation_details": "None.",
                "prevention_tips": "Report early signs of abuse before they become fatal.",
                "real_life_example": "A man was beating his dog with a chain. Neighbors filmed it. The police arrested him and handed the dog over to an NGO for adoption.",
                "landmark_judgment": "Animal Welfare Board of India v. A. Nagaraja (2014) - The SC extended the Right to Life (Article 21) to include animals, banning cruel practices like Jallikattu (then)."
            },
            {
                "title": "Government official delaying RTI response",
                "category": "other",
                "is_legal": False,
                "simple_explanation": "Public Information Officers (PIO) must respond to RTI requests within 30 days. Delaying it is illegal.",
                "step_by_step_guide": "1. Wait for 30 days plus 5 days for post.\n2. File a 'First Appeal' with the senior officer in the same department.\n3. If still no response, file a 'Second Appeal' with the Information Commission (State or Central).\n4. The Information Commission can fine the PIO ₹250 per day of delay.",
                "where_to_complain": "First Appellate Authority or State Information Commission.",
                "legal_remedies": "Orders to release information and departmental action against the officer.",
                "compensation_details": "Minimal, but ensures accountability.",
                "prevention_tips": "File RTI online whenever possible it's easier to track.",
                "real_life_example": "Vishal asked for road construction bills via RTI. The officer ignored it. Vishal appealed, and the Commission fined the officer ₹5,000 for the 20-day delay.",
                "landmark_judgment": "RBI v. Jayantilal N. Mistry (2015) - The SC held that public interest overrides fiduciary relationships, making it harder for banks/PSUs to deny RTI info."
            },
            {
                "title": "Illegal Tree Cutting in the neighborhood",
                "category": "other",
                "is_legal": False,
                "simple_explanation": "In most Indian cities, you need permission from the 'Tree Officer' even to cut a tree inside your private property.",
                "step_by_step_guide": "1. Ask the people cutting the tree for the official 'Permission Letter'.\n2. Note the date and take photos.\n3. Call the local 'Tree Helpline' or the Forest Department.\n4. If police don't help, contact an environmental NGO.",
                "where_to_complain": "Tree Officer (Forest Dept) or NGT.",
                "legal_remedies": "Seizure of cutting equipment and heavy fines (up to 1 Lakh per tree).",
                "compensation_details": "Offender can be ordered to plant 10 new trees for every 1 cut.",
                "prevention_tips": "Know your local 'Tree Preservation Act' rules.",
                "real_life_example": "A builder cut 5 old trees at night. Neighbors informed the Forest Dept. The builder was fined 5 Lakhs and the construction was halted for 3 months.",
                "landmark_judgment": "T.N. Godavarman Thirumulpud v. Union of India (1996) - A continuous mandamus case where the SC oversees forest protection across India."
            }
        ]

        # Populate Situations
        for s in situations_data:
            ViolationSituation.objects.update_or_create(
                title=s['title'],
                defaults=s
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated legal data!'))
