from django.core.management.base import BaseCommand
from rights.models import RightCategory, FundamentalRight

class Command(BaseCommand):
    help = "Seed fundamental rights data (starter set)"

    def handle(self, *args, **kwargs):
        categories = {
            "Equality": RightCategory.objects.get_or_create(name="Equality")[0],
            "Freedom": RightCategory.objects.get_or_create(name="Freedom")[0],
            "Exploitation": RightCategory.objects.get_or_create(name="Exploitation")[0],
            "Religion": RightCategory.objects.get_or_create(name="Religion")[0],
            "Culture & Education": RightCategory.objects.get_or_create(name="Culture & Education")[0],
        }

        rights_data = [
            {
    "article_number": "12",
    "title": "Meaning of ‘State’ (Who must follow Fundamental Rights)",
    "category": categories["Equality"],
    "legal_explanation": (
        "Article 12 explains what 'State' means for Fundamental Rights. It includes the Government and Parliament of India, "
        "the Government and Legislatures of States, and all local or other authorities under the control of the government. "
        "This matters because Fundamental Rights are mainly enforceable against the 'State' and its bodies."
    ),
    "simple_explanation": (
        "Fundamental Rights mostly protect you from misuse of power by government offices. "
        "So if a government department, police, government college, or municipality treats you unfairly, you can challenge it."
    ),
    "violation_example": (
        "A government college makes an illegal rule that blocks a group of students from admission without valid reason."
    ),
    "what_to_do": (
        "1) Confirm the office/institution is government-controlled.\n"
        "2) Collect proof: notices, letters, screenshots, recordings, witness names.\n"
        "3) Write a short complaint with dates and facts.\n"
        "4) Ask for written acknowledgment.\n"
        "5) Escalate to a higher officer if ignored.\n"
        "6) If still not fixed, take legal help."
    ),
    "where_to_complain": (
        "Department grievance cell, higher officials (SP/DCP/Collector), State Human Rights Commission, "
        "Legal Services Authority, or court."
    ),
    "court_remedy": (
        "High Court (Article 226) or Supreme Court (Article 32) depending on seriousness and urgency."
    ),
    "case_references": "",
    "keywords": "state definition, government authority, public body, local authority, fundamental rights enforce"
},
{
    "article_number": "13",
    "title": "Laws against Fundamental Rights are invalid",
    "category": categories["Equality"],
    "legal_explanation": (
        "Article 13 says the State cannot make any law that takes away or reduces Fundamental Rights. "
        "If a law violates Fundamental Rights, it becomes void to the extent of the violation. "
        "This is how courts strike down unconstitutional rules."
    ),
    "simple_explanation": (
        "No rule is bigger than your Fundamental Rights. If a rule breaks your rights, it can be challenged and removed."
    ),
    "violation_example": (
        "A rule bans peaceful protests everywhere without any reason or fair procedure."
    ),
    "what_to_do": (
        "1) Get the exact rule/order in writing.\n"
        "2) Identify which right it violates (equality, speech, liberty, etc.).\n"
        "3) Collect proof of harm caused.\n"
        "4) Use RTI if you need official documents.\n"
        "5) Take legal advice and prepare a writ petition if needed."
    ),
    "where_to_complain": "Legal Services Authority, High Court, Supreme Court (in serious cases).",
    "court_remedy": "Constitutional challenge through writ petition (Article 226 / Article 32).",
    "case_references": "",
    "keywords": "unconstitutional law, void law, writ petition, rights violation, challenge rule"
},
           {
    "article_number": "17",
    "title": "Abolition of Untouchability",
    "category": categories["Equality"],
    "legal_explanation": (
        "Article 17 abolishes untouchability and forbids its practice in any form. "
        "It is enforceable through criminal laws (like SC/ST protection laws) and other legal remedies."
    ),
    "simple_explanation": (
        "Nobody can treat you as ‘lower’ because of caste. You cannot be denied entry, services, water, or respect due to caste."
    ),
    "violation_example": (
        "A person is denied entry into a shop/temple or forced to sit separately due to caste."
    ),
    "what_to_do": (
        "1) Stay safe first; avoid confrontation if it can turn violent.\n"
        "2) Note date/time/place and names.\n"
        "3) Collect evidence: witnesses, photos, videos.\n"
        "4) File a police complaint/FIR (if applicable).\n"
        "5) If police don’t act, escalate to senior officers.\n"
        "6) Seek legal aid or commission support."
    ),
    "where_to_complain": (
        "Police station, SC/ST cell, senior police officials (SP/DCP), District administration, "
        "State/National SC Commission (depending on your state setup)."
    ),
    "court_remedy": "Writ petition if authorities fail; criminal action under relevant laws.",
    "case_references": "",
    "keywords": "untouchability, caste discrimination, denial of service, atrocities, sc st"
},
{
    "article_number": "19",
    "title": "Freedom of Speech and Expression",
    "category": categories["Freedom"],
    "legal_explanation": (
        "Article 19(1)(a) protects the right to speak, write, publish, and express opinions. "
        "It is not absolute: the State can impose reasonable restrictions for reasons like public order, "
        "defamation, morality, and security of the State."
    ),
    "simple_explanation": (
        "You are free to express your views and criticize peacefully. "
        "But you should not spread hate, false harmful rumors, or threaten violence."
    ),
    "violation_example": (
        "A student is threatened for peacefully posting criticism of a policy, or a peaceful protest is stopped without fair reason."
    ),
    "what_to_do": (
        "1) Keep proof: screenshots, links, messages, videos.\n"
        "2) Write a short statement of what happened and when.\n"
        "3) If threatened online, report on the platform and save the complaint ID.\n"
        "4) For serious threats, report to cyber cell/police.\n"
        "5) Escalate if officials misuse power.\n"
        "6) Seek legal help if harassment continues."
    ),
    "where_to_complain": "Cyber cell, local police (for threats), human rights commission, legal aid services.",
    "court_remedy": "High Court (226) / Supreme Court (32) if government action violates speech rights.",
    "case_references": "",
    "keywords": "speech, expression, protest, opinion, censorship, criticism, social media"
},
{
    "article_number": "20",
    "title": "Protection in respect of conviction for offences",
    "category": categories["Freedom"],
    "legal_explanation": (
        "Article 20 protects people in criminal matters: "
        "(1) No punishment under a law made after the act (no ex-post facto criminal law), "
        "(2) No double punishment for the same offence (double jeopardy), "
        "(3) No forced self-incrimination (cannot be forced to confess)."
    ),
    "simple_explanation": (
        "You can’t be punished unfairly, punished twice for the same thing, or forced to confess by pressure."
    ),
    "violation_example": "Police force someone to sign a confession or threaten them to admit guilt.",
    "what_to_do": (
        "1) Ask for a lawyer / legal aid.\n"
        "2) Don’t sign papers you don’t understand.\n"
        "3) Note the names of officers and time/place.\n"
        "4) Inform family.\n"
        "5) Report misconduct to senior officials.\n"
        "6) Keep medical proof if there is physical abuse."
    ),
    "where_to_complain": "Magistrate, senior police officers, human rights commission, legal services authority.",
    "court_remedy": "Approach High Court/Supreme Court for protection; criminal complaint if needed.",
    "case_references": "",
    "keywords": "self incrimination, confession, double jeopardy, criminal protection, ex post facto"
},
{
    "article_number": "21",
    "title": "Protection of Life and Personal Liberty",
    "category": categories["Freedom"],
    "legal_explanation": (
        "Article 21 says no person shall be deprived of life or personal liberty except according to procedure established by law. "
        "Courts have expanded this to include dignity, privacy, fair procedure, and protection from arbitrary state action."
    ),
    "simple_explanation": (
        "You have the right to live safely and with dignity. Government cannot treat you unfairly or lock you up without proper procedure."
    ),
    "violation_example": "Illegal detention, custodial abuse, or authorities acting without proper process.",
    "what_to_do": (
        "1) Ask the reason and request it in writing.\n"
        "2) Contact family and lawyer immediately.\n"
        "3) Collect proof (CCTV requests, witnesses, medical reports).\n"
        "4) If it’s detention, approach Magistrate quickly.\n"
        "5) Escalate to senior officials.\n"
        "6) Use legal aid if you cannot afford a lawyer."
    ),
    "where_to_complain": "SP/DCP, Magistrate, State Human Rights Commission, Legal Services Authority.",
    "court_remedy": "Habeas corpus / writ petition in High Court or Supreme Court.",
    "case_references": "",
    "keywords": "life, liberty, dignity, illegal detention, police, habeas corpus, privacy"
},
            {
    "article_number": "22",
    "title": "Protection Against Arrest and Detention",
    "category": categories["Freedom"],
    "legal_explanation": (
        "Article 22 gives safeguards: person must be informed of grounds of arrest, allowed to consult a lawyer, "
        "and produced before a Magistrate within 24 hours (general rule). Preventive detention has separate rules."
    ),
    "simple_explanation": (
        "Police cannot secretly keep you. They must tell the reason, allow lawyer help, and take you to a Magistrate soon."
    ),
    "violation_example": "A person is held for more than 24 hours without being produced before a Magistrate.",
    "what_to_do": (
        "1) Ask: 'Why am I being arrested?' and request written grounds.\n"
        "2) Call family/lawyer.\n"
        "3) Note date/time, location, officers.\n"
        "4) Demand production before Magistrate.\n"
        "5) Seek legal aid if needed."
    ),
    "where_to_complain": "Magistrate, SP/DCP, State Human Rights Commission, Legal Services Authority.",
    "court_remedy": "Habeas corpus / writ petition for unlawful detention.",
    "case_references": "",
    "keywords": "arrest rights, detention, 24 hours, magistrate, lawyer"
},
{
    "article_number": "23",
    "title": "Prohibition of Human Trafficking and Forced Labour",
    "category": categories["Exploitation"],
    "legal_explanation": (
        "Article 23 prohibits trafficking in human beings, begar (forced labour), and similar exploitation. "
        "Violations are punishable under law and require state action to rescue and protect victims."
    ),
    "simple_explanation": (
        "No one can sell people, trap workers, or force someone to work without pay or freedom."
    ),
    "violation_example": "Workers are kept locked, not paid, threatened, and not allowed to leave (bonded labour situation).",
    "what_to_do": (
        "1) Ensure safety and contact trusted people.\n"
        "2) Collect location details and proof if safe.\n"
        "3) Report quickly; involve NGOs if needed.\n"
        "4) Request rescue/protection for victims.\n"
        "5) Follow up on FIR and action taken."
    ),
    "where_to_complain": "Police, Anti-Human Trafficking Unit, District Labour Officer, Child/Women protection bodies.",
    "court_remedy": "Criminal action + compensation; writ petition if authorities don’t act.",
    "case_references": "",
    "keywords": "trafficking, forced labour, bonded labour, rescue, exploitation"
},
{
    "article_number": "24",
    "title": "Prohibition of Child Labour in Hazardous Work",
    "category": categories["Exploitation"],
    "legal_explanation": (
        "Article 24 prohibits employing children below 14 years in factories, mines, or hazardous work. "
        "Child protection and labour laws support enforcement."
    ),
    "simple_explanation": (
        "Children should not be made to do dangerous work. They should be safe and in education."
    ),
    "violation_example": "A child works in a firecracker unit, chemicals shop, or risky construction site.",
    "what_to_do": (
        "1) Note place and employer details.\n"
        "2) Report to child protection/labour authorities.\n"
        "3) Provide evidence if safe (photo/location).\n"
        "4) Request rescue and rehabilitation.\n"
        "5) Follow up to ensure the child is protected."
    ),
    "where_to_complain": "Childline 1098, Labour Department, Police, District Child Protection Unit.",
    "court_remedy": "Action under child labour/juvenile protection laws; court if authorities ignore.",
    "case_references": "",
    "keywords": "child labour, hazardous work, childline 1098, factory, mine"
},
{
    "article_number": "25",
    "title": "Freedom of Religion",
    "category": categories["Religion"],
    "legal_explanation": (
        "Article 25 guarantees freedom of conscience and the right to profess, practice and propagate religion, "
        "subject to public order, morality and health."
    ),
    "simple_explanation": (
        "You can follow your religion peacefully. No one should force you to change beliefs or stop you without a valid reason."
    ),
    "violation_example": "Someone is threatened or stopped from peaceful worship, or forced to participate in a religious activity.",
    "what_to_do": (
        "1) Stay calm and avoid escalating.\n"
        "2) Record details and evidence.\n"
        "3) Report threats/violence to police.\n"
        "4) Inform local administration if public interference happens.\n"
        "5) Seek legal help if restriction is by authorities."
    ),
    "where_to_complain": "Local police (if threats/violence), District administration, Human Rights Commission.",
    "court_remedy": "Writ petition if unlawful restrictions by authorities.",
    "case_references": "",
    "keywords": "religion, worship, conscience, practice, propagate"
},
            {
    "article_number": "29",
    "title": "Protection of Interests of Minorities",
    "category": categories["Culture & Education"],
    "legal_explanation": (
        "Article 29 protects the right of any section of citizens to conserve their language, script or culture. "
        "It also prevents denial of admission in state-aided institutions on grounds like religion, race, caste, or language."
    ),
    "simple_explanation": (
        "Communities can protect their language and culture. Students should not be denied admission due to identity."
    ),
    "violation_example": "A student is denied admission because they belong to a minority community or speak a certain language.",
    "what_to_do": (
        "1) Ask for the reason in writing.\n"
        "2) Save messages/emails.\n"
        "3) Complain to the institution and education department.\n"
        "4) Escalate to commissions if needed.\n"
        "5) Seek legal aid if discrimination continues."
    ),
    "where_to_complain": "Education department grievance, minority commission (if applicable), legal services authority.",
    "court_remedy": "High Court writ petition for discriminatory admission denial.",
    "case_references": "",
    "keywords": "minority, language, culture, admission, discrimination"
},
{
    "article_number": "30",
    "title": "Minorities can establish and administer educational institutions",
    "category": categories["Culture & Education"],
    "legal_explanation": (
        "Article 30 gives minorities the right to establish and administer educational institutions. "
        "State aid policies should not discriminate unfairly against minority institutions."
    ),
    "simple_explanation": (
        "Minority groups can run their own schools/colleges to protect their identity, while following general laws."
    ),
    "violation_example": "A minority institution is treated unfairly or denied benefits only because it is minority-run.",
    "what_to_do": (
        "1) Collect the policy/order causing discrimination.\n"
        "2) Compare treatment with similar non-minority institutions.\n"
        "3) File a written grievance.\n"
        "4) Escalate to education department/commission.\n"
        "5) Seek legal help if not resolved."
    ),
    "where_to_complain": "Education department, minority commission (if applicable), court.",
    "court_remedy": "High Court writ petition to protect Article 30 rights.",
    "case_references": "",
    "keywords": "minority institution, education, administer, aid, discrimination"
},
{
    "article_number": "32",
    "title": "Right to Constitutional Remedies",
    "category": categories["Freedom"],
    "legal_explanation": (
        "Article 32 allows a person to approach the Supreme Court directly for enforcement of Fundamental Rights. "
        "Courts can issue writs like Habeas Corpus, Mandamus, Certiorari, Prohibition, and Quo Warranto."
    ),
    "simple_explanation": (
        "If your Fundamental Rights are violated, you can go to court for protection. Courts can order authorities to fix it."
    ),
    "violation_example": "Authorities ignore repeated complaints and continue violating equality or liberty rights.",
    "what_to_do": (
        "1) Collect proof and documents.\n"
        "2) Write timeline of events.\n"
        "3) Try grievance escalation where possible.\n"
        "4) Take legal aid/advocate support.\n"
        "5) File a writ petition if needed."
    ),
    "where_to_complain": "Supreme Court (Article 32) or High Court (Article 226).",
    "court_remedy": "Writ petitions for enforcement of rights.",
    "case_references": "",
    "keywords": "article 32, writ, constitutional remedy, supreme court, habeas corpus"
},
            {
    "article_number": "15",
    "title": "Prohibition of discrimination on grounds of religion, race, caste, sex or place of birth",
    "category": categories["Equality"],
    "legal_explanation": (
        "Article 15 prohibits discrimination by the State against any citizen on grounds of religion, race, caste, sex, or place of birth. "
        "This means the government cannot treat people differently based on these characteristics in areas like employment, education, or public facilities."
    ),
    "simple_explanation": (
        "The government cannot discriminate against you because of your religion, caste, gender, or where you were born. "
        "For example, government jobs, schools, and public places must be open to everyone equally."
    ),
    "violation_example": (
        "A government school refuses admission to students from a particular caste or religion."
    ),
    "what_to_do": (
        "1) Document the discriminatory action with evidence.\n"
        "2) File a complaint with the concerned department.\n"
        "3) Approach the State Human Rights Commission.\n"
        "4) File a writ petition in High Court."
    ),
    "where_to_complain": "State Human Rights Commission, High Court, or Supreme Court.",
    "court_remedy": "Writ of Mandamus to compel equal treatment.",
    "case_references": "",
    "keywords": "discrimination prohibition, equality, caste, religion, gender"
},
            {
    "article_number": "16",
    "title": "Equality of opportunity in matters of public employment",
    "category": categories["Equality"],
    "legal_explanation": (
        "Article 16 ensures equal opportunity for all citizens in matters of public employment. "
        "No citizen shall be discriminated against or ineligible for any employment or office under the State on grounds of religion, race, caste, sex, descent, place of birth, or residence."
    ),
    "simple_explanation": (
        "Government jobs must be open to everyone equally. You cannot be denied a government job just because of your religion, caste, gender, or where you were born."
    ),
    "violation_example": (
        "A government department refuses to hire qualified candidates from certain castes or religions."
    ),
    "what_to_do": (
        "1) Apply for the job and document any discriminatory rejection.\n"
        "2) File complaint with UPSC (for central jobs) or State Public Service Commission.\n"
        "3) Approach Central Administrative Tribunal or High Court."
    ),
    "where_to_complain": "UPSC/State PSC, Central Administrative Tribunal, High Court.",
    "court_remedy": "Writ of Mandamus for fair consideration.",
    "case_references": "",
    "keywords": "public employment, equal opportunity, government jobs, reservation"
},
            {
    "article_number": "18",
    "title": "Abolition of titles",
    "category": categories["Equality"],
    "legal_explanation": (
        "Article 18 abolishes all titles except military and academic distinctions. "
        "No citizen of India shall accept any title from any foreign State and no person holding any office of profit shall accept any title from the State."
    ),
    "simple_explanation": (
        "You cannot use fancy titles like 'Sir', 'Lord', or foreign titles. Only military ranks and academic degrees are allowed."
    ),
    "violation_example": (
        "A government official uses a foreign title or accepts a knighthood."
    ),
    "what_to_do": (
        "1) Report to the concerned authority.\n"
        "2) File complaint with Election Commission if it's a political matter."
    ),
    "where_to_complain": "Election Commission, concerned department.",
    "court_remedy": "Rarely litigated, but can be challenged if misused.",
    "case_references": "",
    "keywords": "titles abolition, foreign titles, military ranks, academic degrees"
},
            {
    "article_number": "26",
    "title": "Freedom to manage religious affairs",
    "category": categories["Religion"],
    "legal_explanation": (
        "Article 26 grants every religious denomination the right to establish and maintain institutions for religious and charitable purposes, "
        "manage its own affairs in matters of religion, and own and acquire movable and immovable property."
    ),
    "simple_explanation": (
        "Religious groups can manage their own religious matters, run their places of worship, and own property for religious purposes."
    ),
    "violation_example": (
        "Government interferes in the internal management of a religious institution."
    ),
    "what_to_do": (
        "1) Document the interference.\n"
        "2) Approach the religious institution's governing body.\n"
        "3) File writ petition in High Court."
    ),
    "where_to_complain": "High Court or Supreme Court.",
    "court_remedy": "Writ of Mandamus to prevent interference.",
    "case_references": "",
    "keywords": "religious freedom, religious institutions, property rights"
},
            {
    "article_number": "27",
    "title": "Freedom from payment of taxes for promotion of any religion",
    "category": categories["Religion"],
    "legal_explanation": (
        "Article 27 provides that no person shall be compelled to pay any taxes for the promotion or maintenance of any particular religion or religious denomination."
    ),
    "simple_explanation": (
        "You cannot be forced to pay taxes to support any religion. Your tax money cannot be used to promote one religion over others."
    ),
    "violation_example": (
        "Government uses tax money to build religious structures of only one religion."
    ),
    "what_to_do": (
        "1) File RTI to check fund utilization.\n"
        "2) File PIL in High Court if public interest is affected."
    ),
    "where_to_complain": "High Court or Supreme Court through PIL.",
    "court_remedy": "Writ of Mandamus to stop misuse of funds.",
    "case_references": "",
    "keywords": "religious taxation, secularism, public funds"
},
            {
    "article_number": "28",
    "title": "Freedom from religious instruction in educational institutions",
    "category": categories["Religion"],
    "legal_explanation": (
        "Article 28 prohibits religious instruction in any educational institution wholly maintained out of State funds. "
        "However, religious instruction is allowed in institutions established by religious communities."
    ),
    "simple_explanation": (
        "Government schools and colleges cannot teach religion as part of their curriculum. "
        "But religious schools can teach their own religion."
    ),
    "violation_example": (
        "A government school forces students to attend religious classes."
    ),
    "what_to_do": (
        "1) Report to school administration.\n"
        "2) File complaint with education department.\n"
        "3) Approach State Human Rights Commission."
    ),
    "where_to_complain": "Education Department, State Human Rights Commission, High Court.",
    "court_remedy": "Writ of Mandamus to stop religious instruction.",
    "case_references": "",
    "keywords": "religious education, government schools, secular education"
},
        ]

        created_count = 0
        for item in rights_data:
            obj, created = FundamentalRight.objects.get_or_create(
                article_number=item["article_number"],
                title=item["title"],
                defaults=item
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Seed complete. Added {created_count} new rights."))