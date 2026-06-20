"""
Comprehensive seed data management command for NyayaSetu.
Populates the database with sample rights, laws, complaints, and services.
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from accounts.models import CustomUser
from rights.models import FundamentalRight, RightCategory
from women_safety.models import WomenSafetyRight
from regions.models import State, RegionalLaw
from violations.models import ViolationConsequence
from helplines.models import Helpline
from police_stations.models import PoliceStation
from documents.models import GovernmentDocument
from applications.models import ApplicationService
import json

class Command(BaseCommand):
    help = 'Seed the database with sample data for NyayaSetu'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Clear existing data before seeding')

    def handle(self, *args, **options):
        if options['clear']:
            self.clear_database()
            self.stdout.write(self.style.WARNING('[SUCCESS] Database cleared'))

        try:
            self.create_superuser()
            self.create_rights_and_categories()
            self.create_women_safety_rights()
            self.create_states_and_laws()
            self.create_violation_consequences()
            self.create_helplines()
            self.create_police_stations()
            self.create_government_documents_and_services()
            self.create_workplace_laws()
            
            self.stdout.write(self.style.SUCCESS('[SUCCESS] Database seeded successfully!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'[ERROR] Error: {str(e)}'))

    def clear_database(self):
        """Clear all app data"""
        FundamentalRight.objects.all().delete()
        RightCategory.objects.all().delete()
        WomenSafetyRight.objects.all().delete()
        State.objects.all().delete()
        RegionalLaw.objects.all().delete()
        ViolationConsequence.objects.all().delete()
        Helpline.objects.all().delete()
        PoliceStation.objects.all().delete()
        GovernmentDocument.objects.all().delete()
        ApplicationService.objects.all().delete()

    def create_superuser(self):
        """Create admin superuser"""
        if not CustomUser.objects.filter(username='admin').exists():
            CustomUser.objects.create_superuser(
                username='admin',
                email='admin@nyayasetu.gov.in',
                password='Admin@123456',
                first_name='Administrator',
                user_type='admin'
            )
            self.stdout.write('[SUCCESS] Superuser created: admin@nyayasetu.gov.in')

    def create_rights_and_categories(self):
        """Create fundamental rights data (Articles 12-35)"""
        categories = [
            {'name': 'Equality Rights', 'description': 'Articles 14-18: Right to equality'},
            {'name': 'Freedom Rights', 'description': 'Articles 19-22: Fundamental freedoms'},
            {'name': 'Exploitation Rights', 'description': 'Articles 23-24: Protection from exploitation'},
            {'name': 'Religion Rights', 'description': 'Articles 25-28: Freedom of religion'},
            {'name': 'Cultural Rights', 'description': 'Articles 29-30: Cultural and educational rights'},
            {'name': 'Constitutional Remedies', 'description': 'Articles 32-35: Right to Constitutional Remedies'},
        ]

        for cat_data in categories:
            RightCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )

        # 20+ Laws Representation
        rights_data = [
            # Equality
            {'category_name': 'Equality Rights', 'article_number': '14', 'title': 'Right to Equality', 'legal_explanation': 'Equality before the law and equal protection of laws.', 'simple_explanation': 'The state treats everyone equally regardless of status.', 'violation_example': 'Law discriminates against a specific group without a logical reason.', 'what_to_do': 'File Writ Petition.', 'where_to_complain': 'High Court / Supreme Court', 'court_remedy': 'Striking down the discriminatory law or order.'},
            {'category_name': 'Equality Rights', 'article_number': '15', 'title': 'Prohibition of Discrimination', 'legal_explanation': 'No discrimination on grounds of religion, race, caste, sex or place of birth.', 'simple_explanation': 'You cannot be denied access to shops, public restaurants, or wells based on your caste or religion.', 'violation_example': 'A restaurant refusing entry to someone based on their caste.', 'what_to_do': 'File an FIR under civil rights protection act.', 'where_to_complain': 'Local Police Station and Courts', 'court_remedy': 'Criminal penalties for the offender.'},
            {'category_name': 'Equality Rights', 'article_number': '16', 'title': 'Equality of Opportunity in Public Employment', 'legal_explanation': 'Equal opportunity for all citizens in matters relating to employment or appointment to any office under the State.', 'simple_explanation': 'Everyone gets an equal chance to apply for government jobs subject to reservations.', 'violation_example': 'Being denied a government job application due to your religion.', 'what_to_do': 'Approach administrative tribunals or courts.', 'where_to_complain': 'Administrative Tribunals / High Court', 'court_remedy': 'Mandamus directing the state to consider the application.'},
            {'category_name': 'Equality Rights', 'article_number': '17', 'title': 'Abolition of Untouchability', 'legal_explanation': 'Untouchability is abolished and its practice in any form is forbidden.', 'simple_explanation': 'Treating someone as untouchable is a strict crime.', 'violation_example': 'Forcing someone to clean manual waste or preventing them from entering a temple.', 'what_to_do': 'File an immediate police FIR.', 'where_to_complain': 'Police Station (SC/ST Atrocities Act)', 'court_remedy': 'Non-bailable arrest of the offender.'},
            {'category_name': 'Equality Rights', 'article_number': '18', 'title': 'Abolition of Titles', 'legal_explanation': 'No title, not being a military or academic distinction, shall be conferred by the State.', 'simple_explanation': 'The government will not give out royal titles like Maharaja or Nawab anymore.', 'violation_example': 'A citizen accepting a title from a foreign state without President\'s consent.', 'what_to_do': 'Report to home ministry.', 'where_to_complain': 'Ministry of Home Affairs', 'court_remedy': 'Forfeiture of the title.'},
            
            # Freedom
            {'category_name': 'Freedom Rights', 'article_number': '19', 'title': 'Freedom of Speech and Expression', 'legal_explanation': 'Protection of certain rights regarding freedom of speech, assembly, association, movement, residence, and profession.', 'simple_explanation': 'You can express yourself, gather peacefully, travel, and choose your career.', 'violation_example': 'Being arrested for a critical but peaceful social media post.', 'what_to_do': 'File a writ of Habeas Corpus.', 'where_to_complain': 'High Court', 'court_remedy': 'Immediate release and compensation.'},
            {'category_name': 'Freedom Rights', 'article_number': '20', 'title': 'Protection in respect of Conviction for Offences', 'legal_explanation': 'Protection against ex post facto laws, double jeopardy, and self-incrimination.', 'simple_explanation': 'You cannot be forced to be a witness against yourself, nor punished twice for the same crime.', 'violation_example': 'Police torturing a suspect to confess to a crime.', 'what_to_do': 'Report to the Magistrate during production.', 'where_to_complain': 'Magistrate Court / NHRC', 'court_remedy': 'Confession invalidated, police officers suspended.'},
            {'category_name': 'Freedom Rights', 'article_number': '21', 'title': 'Right to Life and Personal Liberty', 'legal_explanation': 'No person shall be deprived of his life or personal liberty except according to procedure established by law.', 'simple_explanation': 'You have the right to live a life of dignity, including rights to privacy and clean environment.', 'violation_example': 'Unlawful detention or severe pollution affecting health.', 'what_to_do': 'File a writ petition in the Supreme/High Court.', 'where_to_complain': 'High Court / Supreme Court', 'court_remedy': 'Injunctions against polluters, release of detained person.'},
            {'category_name': 'Freedom Rights', 'article_number': '21A', 'title': 'Right to Education', 'legal_explanation': 'The State shall provide free and compulsory education to all children of the age of six to fourteen years.', 'simple_explanation': 'Children aged 6-14 must get free education.', 'violation_example': 'A government school refusing admission to a local child.', 'what_to_do': 'Complain to the District Education Officer.', 'where_to_complain': 'Education Department', 'court_remedy': 'Court order forcing the school to admit the child.'},
            {'category_name': 'Freedom Rights', 'article_number': '22', 'title': 'Protection against Arrest and Detention', 'legal_explanation': 'Right to be informed of grounds of arrest, right to consult a lawyer, and right to be produced before a magistrate within 24 hours.', 'simple_explanation': 'If arrested, police must tell you why, let you call a lawyer, and take you to a judge within a day.', 'violation_example': 'Being kept in a police lockup for 3 days without seeing a judge.', 'what_to_do': 'Family member should file Habeas Corpus.', 'where_to_complain': 'High Court', 'court_remedy': 'Immediate release of the illegally detained person.'},

            # Exploitation
            {'category_name': 'Exploitation Rights', 'article_number': '23', 'title': 'Prohibition of Traffic in Human Beings and Forced Labour', 'legal_explanation': 'Traffic in human beings and begar and other similar forms of forced labour are prohibited.', 'simple_explanation': 'Human trafficking and forcing people to work without pay is illegal.', 'violation_example': 'Keeping domestic help locked up and unpaid.', 'what_to_do': 'Call the anti-trafficking helpline or police.', 'where_to_complain': 'Police / Anti-Trafficking Cell', 'court_remedy': 'Rescue operations and severe criminal charges for the offender.'},
            {'category_name': 'Exploitation Rights', 'article_number': '24', 'title': 'Prohibition of Employment of Children in Factories, etc.', 'legal_explanation': 'No child below the age of fourteen years shall be employed to work in any factory or mine or engaged in any other hazardous employment.', 'simple_explanation': 'Children under 14 cannot work in dangerous places like mines or factories.', 'violation_example': 'A 10-year-old child found working in a firecracker factory.', 'what_to_do': 'Report to Childline (1098).', 'where_to_complain': 'NCPCR / Childline / Police', 'court_remedy': 'Rescue of child, fine on factory owner, rehabilitation fund.'},
            
            # Religion
            {'category_name': 'Religion Rights', 'article_number': '25', 'title': 'Freedom of Conscience and Free Profession, Practice and Propagation of Religion', 'legal_explanation': 'All persons are equally entitled to freedom of conscience and the right freely to profess, practise and propagate religion.', 'simple_explanation': 'You can choose to follow any religion or no religion at all.', 'violation_example': 'Mob preventing a peaceful religious procession without state orders.', 'what_to_do': 'File an FIR.', 'where_to_complain': 'Police', 'court_remedy': 'Police protection ordered by court.'},
            {'category_name': 'Religion Rights', 'article_number': '26', 'title': 'Freedom to Manage Religious Affairs', 'legal_explanation': 'Every religious denomination shall have the right to establish and maintain institutions for religious and charitable purposes.', 'simple_explanation': 'Religious groups can manage their own trusted affairs and properties.', 'violation_example': 'Government illegally seizing properties of a religious trust.', 'what_to_do': 'File a writ petition against the state action.', 'where_to_complain': 'High Court', 'court_remedy': 'Return of property management to the trust.'},
            
            # Cultural and Educational
            {'category_name': 'Cultural Rights', 'article_number': '29', 'title': 'Protection of Interests of Minorities', 'legal_explanation': 'Any section of the citizens residing in the territory of India having a distinct language, script or culture of its own shall have the right to conserve the same.', 'simple_explanation': 'Minority communities can protect their distinct language and culture.', 'violation_example': 'Banning the use of a minority language in an area.', 'what_to_do': 'Approach the courts.', 'where_to_complain': 'Supreme Court / High Court', 'court_remedy': 'Nullifying such unconstitutional bans.'},
            {'category_name': 'Cultural Rights', 'article_number': '30', 'title': 'Right of Minorities to Establish and Administer Educational Institutions', 'legal_explanation': 'All minorities, whether based on religion or language, shall have the right to establish and administer educational institutions of their choice.', 'simple_explanation': 'Minorities can set up their own schools to preserve their culture.', 'violation_example': 'State discriminatorily denying funding to a minority-run school.', 'what_to_do': 'File for a Mandamus writ.', 'where_to_complain': 'High Court', 'court_remedy': 'Restoration of fair funding.'},

            # Remedies
            {'category_name': 'Constitutional Remedies', 'article_number': '32', 'title': 'Remedies for enforcement of rights conferred by this Part', 'legal_explanation': 'The right to move the Supreme Court by appropriate proceedings for the enforcement of the rights conferred by this Part is guaranteed.', 'simple_explanation': 'The core right that allows you to enforce all other rights directly in the Supreme Court.', 'violation_example': 'When lower authorities ignore severe fundamental rights abuses.', 'what_to_do': 'File a PIL (Public Interest Litigation) or Writ Petition.', 'where_to_complain': 'Supreme Court of India', 'court_remedy': 'Issuance of writs like Habeas Corpus, Mandamus, Prohibition, Quo Warranto and Certiorari.'},
        ]

        for right_data in rights_data:
            category = RightCategory.objects.get(name=right_data.pop('category_name'))
            FundamentalRight.objects.get_or_create(
                article_number=right_data['article_number'],
                defaults={
                    'title': right_data['title'],
                    'legal_explanation': right_data['legal_explanation'],
                    'simple_explanation': right_data['simple_explanation'],
                    'violation_example': right_data['violation_example'],
                    'what_to_do': right_data['what_to_do'],
                    'where_to_complain': right_data['where_to_complain'],
                    'court_remedy': right_data['court_remedy'],
                    'category': category,
                }
            )

        self.stdout.write('[SUCCESS] Fundamental rights created')

    def create_women_safety_rights(self):
        """Create extended women safety laws"""
        laws = [
            {
                'title': 'Protection of Women from Domestic Violence Act, 2005',
                'category': 'domestic',
                'description': 'Protects women from physical, emotional, sexual, and economic abuse in a domestic setting.',
                'rights_provided': 'Right to reside in shared household, protection orders, monetary relief, custody orders for children.',
                'penalties': 'Breach of protection order is punishable by up to 1 year imprisonment or ₹20,000 fine. Abuser can be forced to pay child support and medical bills.',
                'how_to_get_help': '1. Call 181 Women Helpline or 112 Police.\n2. Contact a Protection Officer (PO) at the District Level.\n3. File a complaint with the Magistrate.\n4. Seek a Protection Order immediately.',
                'prevention_tips': 'Maintain a safety plan, keep emergency contacts handy, and document incidents of abuse.'
            },
            {
                'title': 'The Sexual Harassment of Women at Workplace (PoSH) Act, 2013',
                'category': 'workplace',
                'description': 'Mandates a safe working environment and an Internal Complaints Committee (ICC) in workplaces with 10 or more employees.',
                'rights_provided': '- Right to a safe working environment.\n- Right to inquiry by the ICC.\n- Interim relief like transfer or 3 months paid leave during inquiry.',
                'penalties': 'Employer can be fined up to ₹50,000 for non-compliance. Repeat offences can lead to cancellation of business license. The perpetrator can face dismissal or heavy fines.',
                'how_to_get_help': '1. File a written complaint to the company\'s ICC within 3 months.\n2. If no ICC exists, report to the Local Complaints Committee (LCC) in your district.\n3. You can also file a police FIR under IPC/BNS concurrently.',
                'prevention_tips': 'Read the company PoSH policy, attend awareness sessions, and don\'t bridge professional boundaries.'
            },
            {
                'title': 'Protection of Children from Sexual Offences (POCSO) Act, 2012',
                'category': 'child_safety',
                'description': 'A comprehensive law to protect children from offences of sexual assault, sexual harassment, and child pornography.',
                'rights_provided': '- Child-friendly reporting (police in plain clothes).\n- Right to have identity protected (no names in news).\n- Right to have statements recorded at the child\'s residence.',
                'penalties': 'Severe punishment ranging from 7 years to life imprisonment or even death penalty in aggravated cases. Mandatory minimum sentences for repeat offenders.',
                'how_to_get_help': '1. Call Childline (1098) or 112 immediately.\n2. Report to the Special Juvenile Police Unit (SJPU) or a local doctor.\n3. Mandatory reporting: Any adult who knows about the offence must report it or face punishment.',
                'prevention_tips': 'Educate children on "Safe Touch" and "Unsafe Touch". Listen to your child and look for behavioral changes.'
            },
            {
                'title': 'Dowry Prohibition Act, 1961',
                'category': 'family',
                'description': 'Strictly prohibits the practice of giving, taking, or demanding dowry in connection with marriage.',
                'rights_provided': '- Protection against harassed demands for money or gifts.\n- Legal assistance to recover property given as dowry.',
                'penalties': 'Demanding dowry: up to 2 years imprisonment + ₹10,000 fine. Giving/Taking dowry: Min 5 years imprisonment + fine up to ₹15,000 or value of dowry.',
                'how_to_get_help': '1. File an FIR at the local police station.\n2. Report to the Dowry Prohibition Officer of your area.\n3. File a complaint under the SC/ST Act if applicable.',
                'prevention_tips': 'Avoid cash transactions in weddings; maintain a list of customary gifts signed by both parties.'
            },
            {
                'title': 'Maternity Benefit Act, 1961 (Amended 2017)',
                'category': 'workplace',
                'description': 'Ensures the health of working mothers and their child by providing paid maternity leave and other benefits.',
                'rights_provided': '- 26 weeks of paid maternity leave.\n- Right to crèche facility if the workplace has 50+ employees.\n- Protection against dismissal during leave.',
                'penalties': 'Employer can be imprisoned for 3 to 12 months and fined up to ₹50,000 for denying benefits.',
                'how_to_get_help': '1. Give a formal written notice to the employer.\n2. If denied, report to the Labour Commissioner.\n3. File a suit in the Labour Court.',
                'prevention_tips': 'Inform employer at least 1 month in advance with medical proof.'
            },
        ]

        for data in laws:
            WomenSafetyRight.objects.get_or_create(title=data['title'], defaults=data)

        self.stdout.write('[SUCCESS] Women safety rights created')

    def create_states_and_laws(self):
        """Create basic states and regional laws"""
        states_data = [
            {'name': 'Andhra Pradesh', 'code': 'AP'}, {'name': 'Delhi', 'code': 'DL'},
            {'name': 'Karnataka', 'code': 'KA'}, {'name': 'Maharashtra', 'code': 'MH'},
            {'name': 'Tamil Nadu', 'code': 'TN'}, {'name': 'Telangana', 'code': 'TS'},
            {'name': 'Uttar Pradesh', 'code': 'UP'}, {'name': 'Kerala', 'code': 'KL'},
        ]
        for state_data in states_data:
            State.objects.get_or_create(name=state_data['name'], defaults={'code': state_data['code']})
            
        # Regional Laws
        ap = State.objects.filter(code='AP').first()
        mh = State.objects.filter(code='MH').first()
        dl = State.objects.filter(code='DL').first()
        
        laws = [
            {'title': 'Maharashtra Right to Public Services Act', 'state': mh, 'act_name': 'RTS Act', 'description': 'Empowers citizens to get public services transparently, efficiently and timely.', 'who_it_applies_to': 'Citizens of Maharashtra', 'how_to_comply': 'Apply through Aaple Sarkar portal.'},
            {'title': 'Andhra Pradesh Disha Act', 'state': ap, 'act_name': 'Disha Act', 'description': 'Expedites trial and ensures swift justice in cases involving specified offences against women and children.', 'who_it_applies_to': 'Victims of crimes against women in AP', 'how_to_comply': 'Report incidence via Disha App or local police.'},
            {'title': 'Delhi Right to Citizen Time Bound Delivery of Services Act', 'state': dl, 'act_name': 'Delhi e-SLA', 'description': 'Provides for the delivery of citizen related services by Govt. departments in Delhi within stipulated time.', 'who_it_applies_to': 'Residents of Delhi', 'how_to_comply': 'Apply via e-District Delhi portal.'},
        ]
        
        for law in laws:
            RegionalLaw.objects.get_or_create(title=law['title'], state=law['state'], defaults=law)
            
        self.stdout.write('[SUCCESS] States & Regional Laws created')

    def create_violation_consequences(self):
        """Map consequences for violating fundamental rights"""
        rights = FundamentalRight.objects.all()
        for right in rights:
            if right.article_number == '14':
                ViolationConsequence.objects.get_or_create(
                    fundamental_right=right,
                    defaults={'immediate_effects': 'Loss of opportunity, financial disadvantage, marginalization.', 'long_term_effects': 'Systemic inequality, loss of faith in government institutions.', 'legal_remedies': 'Writ of Mandamus, strike down of unconstitutional orders.', 'compensation_options': 'Damages for financial losses caused.', 'prevention_measures': 'Strict adherence to transparency and equal opportunity policies.'}
                )
            elif right.article_number == '21':
                ViolationConsequence.objects.get_or_create(
                    fundamental_right=right,
                    defaults={'immediate_effects': 'Physical harm, illegal detention, loss of livelihood or severe distress.', 'long_term_effects': 'Psychological trauma, chronic health issues, social stigma.', 'legal_remedies': 'Writ of Habeas Corpus, criminal prosecution of offending officers.', 'compensation_options': 'Ex-gratia payments, medical coverage, punitive damages against state.', 'prevention_measures': 'Strict CCTV compliance in police stations, environmental monitoring.'}
                )

    def create_helplines(self):
        """Create helpline data"""
        helplines = [
            {'name': 'Women Helpline (All India)', 'category': 'women_safety', 'phone': '181', 'description': '24/7 distress helpline for women.'},
            {'name': 'Police Emergency', 'category': 'police', 'phone': '112', 'description': 'National Emergency Number (replaces 100).'},
            {'name': 'Child Helpline', 'category': 'child_safety', 'phone': '1098', 'description': 'For children in need of care and protection.'},
            {'name': 'Cyber Crime Helpline', 'category': 'police', 'phone': '1930', 'description': 'Report cyber fraud immediately to freeze transactions.'},
            {'name': 'Senior Citizen Helpline', 'category': 'legal_aid', 'phone': '14567', 'description': 'National helpline for elderly support (Elderline).'},
            {'name': 'Legal Aid Services (NALSA)', 'category': 'legal_aid', 'phone': '15100', 'description': 'Free legal aid and advice line.'},
            {'name': 'National Consumer Helpline', 'category': 'legal_aid', 'phone': '1915', 'description': 'Report consumer fraud, defective products, or service deficits.'},
            {'name': 'Anti-Poison Intervention Center', 'category': 'medical', 'phone': '1066', 'description': 'Medical guidance for accidental poisoning or toxic exposure.'},
            {'name': 'Disaster Management Services', 'category': 'medical', 'phone': '108', 'description': 'Ambulance and severe health emergencies.'},
            {'name': 'National Commission for Women', 'category': 'women_safety', 'phone': '7827170170', 'description': 'WhatsApp and calling helpline strictly for women facing abuse.'},
            {'name': 'Kiran (Mental Health Helpline)', 'category': 'medical', 'phone': '1800-599-0019', 'description': 'Government mental health rehabilitation line for anxiety, depression, or distress.'},
            {'name': 'Anti-Ragging Helpline', 'category': 'child_safety', 'phone': '1800-180-5522', 'description': 'UGC mandated helpline for university students facing ragging.'},
        ]
        for h in helplines:
            Helpline.objects.get_or_create(name=h['name'], defaults=h)

    def create_police_stations(self):
        """Create sample police station data with coordinates"""
        dl, _ = State.objects.get_or_create(code='DL', defaults={'name': 'Delhi'})
        mh, _ = State.objects.get_or_create(code='MH', defaults={'name': 'Maharashtra'})
        ts, _ = State.objects.get_or_create(code='TS', defaults={'name': 'Telangana'})
        ka, _ = State.objects.get_or_create(code='KA', defaults={'name': 'Karnataka'})
        tn, _ = State.objects.get_or_create(code='TN', defaults={'name': 'Tamil Nadu'})
        wb, _ = State.objects.get_or_create(code='WB', defaults={'name': 'West Bengal'})
        up, _ = State.objects.get_or_create(code='UP', defaults={'name': 'Uttar Pradesh'})
        
        stations = [
            # Delhi
            {'name': 'Parliament Street Police Station', 'state': dl, 'district': 'New Delhi', 'city': 'New Delhi', 'address': 'Parliament Street, Connaught Place', 'phone': '011-23361100', 'latitude': 28.6255, 'longitude': 77.2139},
            {'name': 'Vasant Vihar Police Station', 'state': dl, 'district': 'South West', 'city': 'New Delhi', 'address': 'Vasant Vihar Marg', 'phone': '011-26141154', 'latitude': 28.5604, 'longitude': 77.1611},
            
            # Mumbai
            {'name': 'Bandra Police Station', 'state': mh, 'district': 'Mumbai Suburban', 'city': 'Mumbai', 'address': 'Hill Road, Bandra West', 'phone': '022-26423042', 'latitude': 19.0566, 'longitude': 72.8306},
            {'name': 'Cyber Crime Police Station BKC', 'state': mh, 'district': 'Mumbai', 'city': 'Mumbai', 'address': 'Bandra Kurla Complex', 'phone': '022-26504008', 'latitude': 19.0660, 'longitude': 72.8656},
            {'name': 'Colaba Police Station', 'state': mh, 'district': 'Mumbai City', 'city': 'Mumbai', 'address': 'Colaba Causeway', 'phone': '022-22856817', 'latitude': 18.9149, 'longitude': 72.8156},

            # Hyderabad (Telangana) General Police
            {'name': 'Madhapur Law & Order Police Station', 'state': ts, 'district': 'Ranga Reddy', 'city': 'Hyderabad', 'address': 'Ayyappa Society, Madhapur', 'phone': '040-27852329', 'latitude': 17.4486, 'longitude': 78.3908, 'office_type': 'police'},
            {'name': 'Jubilee Hills Police Station', 'state': ts, 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'Road No 71, Jubilee Hills', 'phone': '040-27852445', 'latitude': 17.4168, 'longitude': 78.4357, 'office_type': 'police'},
            {'name': 'Panjagutta Police Station', 'state': ts, 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'Nagarjuna Circle, Panjagutta', 'phone': '040-27852441', 'latitude': 17.4262, 'longitude': 78.4507, 'office_type': 'police'},
            {'name': 'Cyber Crime PS, Cyberabad', 'state': ts, 'district': 'Ranga Reddy', 'city': 'Hyderabad', 'address': 'Cyberabad Police Commissionerate, Gachibowli', 'phone': '040-27853610', 'latitude': 17.4300, 'longitude': 78.3600, 'office_type': 'police'},
            
            # Hyderabad Traffic Police
            {'name': 'Hyderabad Traffic Police Station - Cyberabad', 'state': ts, 'district': 'Ranga Reddy', 'city': 'Hyderabad', 'address': 'Gachibowli Junction', 'phone': '040-27852828', 'latitude': 17.4399, 'longitude': 78.3489, 'office_type': 'traffic'},
            {'name': 'Banjara Hills Traffic Police Station', 'state': ts, 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'Banjara Hills Road No 12', 'phone': '040-27852422', 'latitude': 17.4065, 'longitude': 78.4411, 'office_type': 'traffic'},
            
            # Hyderabad MeeSeva Centers
            {'name': 'MeeSeva Center Kukatpally', 'state': ts, 'district': 'Medchal-Malkajgiri', 'city': 'Hyderabad', 'address': 'Near KPHB Metro Station', 'phone': '1800-425-1110', 'latitude': 17.4947, 'longitude': 78.3996, 'office_type': 'meeseva'},
            {'name': 'MeeSeva Center Ameerpet', 'state': ts, 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'SR Nagar Main Road', 'phone': '1800-425-1110', 'latitude': 17.4359, 'longitude': 78.4452, 'office_type': 'meeseva'},
            {'name': 'MeeSeva Center Madhapur', 'state': ts, 'district': 'Ranga Reddy', 'city': 'Hyderabad', 'address': 'Hitech City Road', 'phone': '1800-425-1110', 'latitude': 17.4475, 'longitude': 78.3755, 'office_type': 'meeseva'},

            # Hyderabad Mandal Revenue Offices (MRO)
            {'name': 'Serilingampally Mandal Revenue Office', 'state': ts, 'district': 'Ranga Reddy', 'city': 'Hyderabad', 'address': 'Old Mumbai Highway, Serilingampally', 'phone': '040-23010454', 'latitude': 17.4834, 'longitude': 78.3223, 'office_type': 'mandal'},
            {'name': 'Shaikpet Mandal Revenue Office', 'state': ts, 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'Banjara Hills', 'phone': '040-23393165', 'latitude': 17.4116, 'longitude': 78.4055, 'office_type': 'mandal'},

            # Hyderabad Registration & Sub-Registrar Offices
            {'name': 'Sub-Registrar Office Kukatpally', 'state': ts, 'district': 'Medchal-Malkajgiri', 'city': 'Hyderabad', 'address': 'Moosapet', 'phone': '040-23712128', 'latitude': 17.4651, 'longitude': 78.4343, 'office_type': 'registration'},
            {'name': 'Sub-Registrar Office Banjara Hills', 'state': ts, 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'Yousufguda', 'phone': '040-23547844', 'latitude': 17.4352, 'longitude': 78.4239, 'office_type': 'registration'},
            
            # More Hyderabad Locations
            {'name': 'Gachibowli Police Station', 'state': ts, 'district': 'Ranga Reddy', 'city': 'Hyderabad', 'address': 'Old Mumbai Hwy, Gachibowli', 'phone': '040-27853406', 'latitude': 17.4398, 'longitude': 78.3488, 'office_type': 'police'},
            {'name': 'SR Nagar Police Station', 'state': ts, 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'Sanjeeva Reddy Nagar', 'phone': '040-27852431', 'latitude': 17.4365, 'longitude': 78.4447, 'office_type': 'police'},
            {'name': 'Abids Traffic Police Station', 'state': ts, 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'Abids Road', 'phone': '040-27852467', 'latitude': 17.3888, 'longitude': 78.4754, 'office_type': 'traffic'},
            {'name': 'KPHB Traffic Police Station', 'state': ts, 'district': 'Medchal-Malkajgiri', 'city': 'Hyderabad', 'address': 'KPHB Colony Phase 1', 'phone': '040-27852857', 'latitude': 17.4939, 'longitude': 78.4011, 'office_type': 'traffic'},
            {'name': 'MeeSeva Center Secunderabad', 'state': ts, 'district': 'Hyderabad', 'city': 'Secunderabad', 'address': 'SD Road, Secunderabad', 'phone': '1800-425-1110', 'latitude': 17.4399, 'longitude': 78.4983, 'office_type': 'meeseva'},
            {'name': 'Malkajgiri Mandal Revenue Office', 'state': ts, 'district': 'Medchal-Malkajgiri', 'city': 'Hyderabad', 'address': 'Malkajgiri Main Road', 'phone': '040-27050519', 'latitude': 17.4528, 'longitude': 78.5330, 'office_type': 'mandal'},
            {'name': 'Sub-Registrar Office Secunderabad', 'state': ts, 'district': 'Hyderabad', 'city': 'Secunderabad', 'address': 'Tarnaka Road', 'phone': '040-27003444', 'latitude': 17.4284, 'longitude': 78.5358, 'office_type': 'registration'},
            
            # Bangalore (Karnataka) & Citizen Centers
            {'name': 'Cubbon Park Police Station', 'state': ka, 'district': 'Bengaluru Urban', 'city': 'Bengaluru', 'address': 'Kasturba Road', 'phone': '080-22942544', 'latitude': 12.9772, 'longitude': 77.5959, 'office_type': 'police'},
            {'name': 'Koramangala Police Station', 'state': ka, 'district': 'Bengaluru Urban', 'city': 'Bengaluru', 'address': '8th Block, Koramangala', 'phone': '080-22942570', 'latitude': 12.9405, 'longitude': 77.6190, 'office_type': 'police'},
            {'name': 'Indiranagar Police Station', 'state': ka, 'district': 'Bengaluru Urban', 'city': 'Bengaluru', 'address': 'CMH Road, Indiranagar', 'phone': '080-22942547', 'latitude': 12.9784, 'longitude': 77.6408, 'office_type': 'police'},
            {'name': 'Bangalore One Center (MeeSeva Eq)', 'state': ka, 'district': 'Bengaluru Urban', 'city': 'Bengaluru', 'address': 'Jayanagar 4th Block', 'phone': '080-22222222', 'latitude': 12.9250, 'longitude': 77.5938, 'office_type': 'meeseva'},
            {'name': 'Sub-Registrar Office Gandhinagar', 'state': ka, 'district': 'Bengaluru Urban', 'city': 'Bengaluru', 'address': 'Gandhinagar', 'phone': '080-22262222', 'latitude': 12.9780, 'longitude': 77.5765, 'office_type': 'registration'},

            # Delhi Area Extensions
            {'name': 'Connaught Place Common Service Center', 'state': dl, 'district': 'New Delhi', 'city': 'New Delhi', 'address': 'Rajiv Chowk', 'phone': '011-23323333', 'latitude': 28.6304, 'longitude': 77.2177, 'office_type': 'meeseva'},
            {'name': 'Vasant Vihar Sub-Registrar', 'state': dl, 'district': 'South West', 'city': 'New Delhi', 'address': 'Vasant Vihar', 'phone': '011-26143434', 'latitude': 28.5604, 'longitude': 77.1611, 'office_type': 'registration'},

            # Chennai (Tamil Nadu)
            {'name': 'Anna Salai Law & Order PS', 'state': tn, 'district': 'Chennai', 'city': 'Chennai', 'address': 'Anna Salai, Mount Road', 'phone': '044-28522306', 'latitude': 13.0604, 'longitude': 80.2646},
            {'name': 'T. Nagar Police Station', 'state': tn, 'district': 'Chennai', 'city': 'Chennai', 'address': 'Venkatnarayana Road, T. Nagar', 'phone': '044-24342371', 'latitude': 13.0405, 'longitude': 80.2337},

            # Kolkata
            {'name': 'Park Street Police Station', 'state': wb, 'district': 'Kolkata', 'city': 'Kolkata', 'address': 'Park Street area', 'phone': '033-22262963', 'latitude': 22.5522, 'longitude': 88.3526},
            {'name': 'Cyber Crime PS, Lalbazar', 'state': wb, 'district': 'Kolkata', 'city': 'Kolkata', 'address': '18, Lalbazar Street', 'phone': '033-22143000', 'latitude': 22.5732, 'longitude': 88.3499},

            # Uttar Pradesh
            {'name': 'Hazratganj Police Station', 'state': up, 'district': 'Lucknow', 'city': 'Lucknow', 'address': 'Hazratganj Circle', 'phone': '0522-2629654', 'latitude': 26.8500, 'longitude': 80.9499},
            {'name': 'Sector 20 Police Station', 'state': up, 'district': 'Gautam Buddha Nagar', 'city': 'Noida', 'address': 'Sector 20, Noida', 'phone': '0120-2521199', 'latitude': 28.5833, 'longitude': 77.3167},
        ]
        for s in stations:
            PoliceStation.objects.get_or_create(name=s['name'], defaults=s)

    def create_government_documents_and_services(self):
        """Massive generation of 9 govt documents with complete structures"""
        docs_data = [
            {
                'name': 'Aadhaar Card',
                'document_type': 'identity',
                'description': 'Aadhaar is like your unique digital identity card. It uses a 12-digit number that marks your presence in India. It is one of the most important documents you can have because it stores your fingerprints and eye-scan data securely to prove you are really you!',
                'purpose': 'Aadhaar helps you get many benefits! You need it to open a bank account, get a SIM card for your phone, and receive money directly from the government for things like gas subsidies or school scholarships.',
                'eligibility': 'Any person living in India can get one. Even tiny babies and senior citizens are eligible! As long as you have proof that you live here, you can apply.',
                'required_documents': '1. Proof of who you are (like a Birth Certificate or School ID)\n2. Proof of where you live (like your parent\'s electricity bill or ration card)\n3. A mobile number to get secret codes (OTPs).',
                'step_by_step_guide': '1. Find the Nearest Center: Go to a nearby Aadhaar Seva Kendra or a bank/post office that does Aadhaar work.\n2. Fill the Form: Get a simple application form and fill in your name, address, and age.\n3. Biometric Check: The officer will take a photo of you, scan your fingerprints, and take a picture of your eyes. It doesn\'t hurt at all!\n4. Get Your Receipt: They will give you a paper with an "Enrolment ID". Keep this very safe!\n5. Wait for the Post: Your physical card will be printed and sent to your house in about 2 to 4 weeks.',
                'fees': 'Free of cost for your first card! If you lose it and need a plastic reprint later, it might cost ₹50.',
                'processing_time': 'Usually 10 to 30 days. You can also download a digital copy (e-Aadhaar) online once it\'s ready.',
                'official_website': 'https://uidai.gov.in/',
                'common_mistakes': '1. Name Mismatch: Make sure your name is spelled exactly as it appears on your birth certificate.\n2. Blurry Photo: Stay still when they take your picture!\n3. Wrong Address: Double-check your pin code, otherwise the card won\'t reach your home.',
                'document_checklist': 'Birth Certificate\nSchool Identity Card\nParent\'s Address Proof\nValid Mobile Number',
                'direct_apply_available': False,
                'offline_centers': 'Aadhaar Seva Kendra, Post Offices, Selected Banks',
            },
            {
                'name': 'PAN Card',
                'document_type': 'identity',
                'description': 'PAN stands for Permanent Account Number. It\'s a special 10-character code given by the Income Tax Department. Think of it as your "financial nickname" that the government uses to track money and taxes.',
                'purpose': 'You need a PAN card if you want to earn a salary, open a bank account, or buy expensive things like a car or a house. It proves you are a responsible citizen who plays a part in the country\'s economy.',
                'eligibility': 'Anyone can get a PAN card, even students who don\'t have a job yet! You just need to be an Indian citizen or someone living and working here.',
                'required_documents': '1. Aadhaar Card (the easiest way!)\n2. Two recent passport-sized photos with a white background\n3. Proof of age like a school certificate.',
                'step_by_step_guide': '1. Apply Online: Go to the NSDL website. It\'s much faster than going to an office!\n2. Fill Form 49A: Use this form for Indian citizens. Enter your details carefully.\n3. Digital e-KYC: If you use your Aadhaar, you don\'t even need to send physical papers. You can sign with an OTP!\n4. Pay the Fee: Use your parent\'s debit card or UPI to pay the small processing fee.\n5. Tracking: You will get a 15-digit number to check where your card is. It usually arrives by post.',
                'fees': 'Approx ₹107 for Indian addresses. It\'s a small price for a lifetime document!',
                'processing_time': 'Digital e-PAN comes in 48 hours. The plastic card arrives in 15-20 days.',
                'official_website': 'https://www.onlineservices.nsdl.com/',
                'common_mistakes': '1. Signature outside the box: When signing, stay inside the white box or it will be rejected!\n2. Old Photos: Use a fresh photo where you look exactly like you do now.\n3. Father\'s Name: Always double check the spelling of your father\'s name as it\'s a key security check.',
                'document_checklist': 'Aadhaar Card (for e-KYC)\nProof of Identity\nProof of Address\n2 Passport size photographs',
                'direct_apply_available': True,
            },
            {
                'name': 'Indian Passport',
                'document_type': 'travel',
                'description': 'A Passport is your "International Identity Card". When you want to travel to other countries like the USA, Dubai, or London, the Passport proves you are an Indian citizen and allows you to cross borders safely.',
                'purpose': 'Its main job is for international travel. But in India, it\'s also considered the absolute strongest proof of your identity and address because the police verify it personally!',
                'eligibility': 'Any Indian citizen can get one! From a new-born baby to an old person. You just need to be a true citizen of India.',
                'required_documents': '1. Proof of Address (like Aadhaar or Bank Passbook)\n2. Proof of Birth Date (Birth Certificate or 10th Class Marksheet)\n3. 10th Class Certificate if you want to skip immigration checks (Non-ECR).',
                'step_by_step_guide': '1. Register Online: Visit the official Passport Seva portal and create an account.\n2. Fill the Form: Click on "Apply for Fresh Passport" and enter all your details accurately.\n3. Pay & Book: You must pay the fee online to get an appointment date and time.\n4. Visit the Office: Go to the Passport Seva Kendra (PSK) on your appointment day. They will check your documents and take your photo.\n5. Police Check: A few days later, a friendly policeman will visit your house to verify you really live there.\n6. Postal Delivery: Once the police give a "Thumbs Up", your passport is printed and sent home!',
                'fees': '₹1,500 for a fresh 36-page booklet. It lasts for 10 years!',
                'processing_time': 'Normal: 30-45 days. Tatkaal (Emergency): 3-7 days.',
                'official_website': 'https://www.passportindia.gov.in/',
                'common_mistakes': '1. Document Mismatch: The names on your Aadhaar and Birth certificate must match exactly.\n2. Not at Home: You must be present at home when the police come to verify!\n3. Wrong Address: Use your current address where you have been living for at least one year.',
                'document_checklist': 'Proof of Present Address\nProof of Date of Birth\n10th Pass Certificate (for Non-ECR status)\nOld Passport (if re-issue)',
                'direct_apply_available': True,
            },
            {
                'name': 'Voter ID Card (EPIC)',
                'document_type': 'identity',
                'description': 'A Voter ID is your "Voice Card". In India, every adult gets a chance to choose who should lead the country. This card proves you are a voter and allows you to enter the polling booth to cast your vote!',
                'purpose': 'Its main purpose is to let you vote during elections. It is also a valid proof of your identity and address that never expires!',
                'eligibility': 'You must be an Indian citizen and at least 18 years old. You can even register when you are 17 so that you are ready as soon as you turn 18!',
                'required_documents': '1. A recent passport-sized photo\n2. Age proof (like your 10th marksheet or Birth certificate)\n3. Address proof (like an electricity bill or your parent\'s Aadhaar).',
                'step_by_step_guide': '1. Go Online: Visit the Voters\' Service Portal (NVSP) or download the Voter Helpline App.\n2. Fill Form 6: Choose "New Voter Registration" and fill in your details.\n3. Upload Photo: Take a clear selfie or upload a photo with a plain background.\n4. Verification: A Booth Level Officer (BLO) might visit your house to check if you really live there.\n5. Get the Card: Once approved, your EPIC card will be sent to your home by speed post for free!',
                'fees': 'Absolutely free of cost! The government wants everyone to vote.',
                'processing_time': 'Usually 1 to 2 months. You get a digital Voter ID (e-EPIC) much faster.',
                'official_website': 'https://voters.eci.gov.in/',
                'common_mistakes': '1. Blurred Photo: If your face isn\'t clear, they won\'t issue the card.\n2. Incomplete Address: Make sure to include your House Number and Street name correctly.\n3. Existing Voter: Don\'t apply again if you already have a card in another city!',
                'document_checklist': 'Passport size photograph\nIdentity proof (Aadhaar/PAN)\nAddress proof (Utility Bills/Rent Agreement)\nAge proof (Birth certificate/10th mark sheet)',
                'direct_apply_available': True,
            },
            {
                'name': 'Driving License',
                'document_type': 'permit',
                'description': 'A Driving License is your "Permission to Drive". It proves that you have learned how to handle a vehicle safely and that you know all the traffic rules to keep everyone on the road safe.',
                'purpose': 'It allows you to legally drive a scooty, bike, or car on public roads. It\'s also a great ID proof!',
                'eligibility': 'You can apply for a gearless scooty (50cc) at age 16 with parents\' permission. For cars and bikes with gears, you must be 18 years old.',
                'required_documents': '1. Age proof (Birth certificate)\n2. Address proof (Aadhaar card)\n3. Learner\'s License (you need this for 30 days before getting the real license).',
                'step_by_step_guide': '1. Learner\'s License First: Apply online on the Parivahan website. You\'ll need to pass a simple computer test about road signs.\n2. Practice: After getting your Learner\'s License, practice driving for at least 30 days.\n3. Book a Slot: Go back to the website and book a date for your physical driving test at the RTO.\n4. Give the Test: Go to the RTO on your bike or car and show the officer you can drive properly (like making an "8" shape or reversing).\n5. License by Post: If you pass, your smart card license will arrive home in 2-3 weeks.',
                'fees': 'Approx ₹200-₹500 for tests + ₹200 for the smart card. Worth it for your safety!',
                'processing_time': '30 days of waiting after the Learner\'s License, then about 15 days after the final test.',
                'official_website': 'https://parivahan.gov.in/',
                'document_checklist': 'Valid Learner\'s License\nAddress Proof (Aadhaar/Passport)\nAge Proof\nFitness Certificate (for older applicants)',
                'direct_apply_available': True,
            },
            {
                'name': 'Income Certificate',
                'document_type': 'certificate',
                'description': 'An Income Certificate is a paper that proves how much money your family earns in a year. It\'s like a "Financial Report Card" issued by the local government officer (Tehsildar).',
                'purpose': 'You need this to get school scholarships, free uniforms, or help with college fees. It helps the government know who needs financial support the most.',
                'eligibility': 'Any family living in the state can apply. The certificate usually shows the combined income of all adult members in the house.',
                'required_documents': '1. Salary slips or a letter from your parent\'s boss\n2. Aadhaar card of the head of the family\n3. Ration card or a self-declaration form.',
                'step_by_step_guide': '1. Go to your state\'s e-District portal.\n2. Register and login to the portal.\n3. Select "Income Certificate" from Revenue Services.\n4. Fill the online application and upload the scanned requisite documents.\n5. Submit and pay the minimal service charge.\n6. The Patwari or local revenue officer verifies the claim offline.\n7. Download the digitally signed certificate.',
                'fees': '₹15 to ₹50 depending on the state portal.',
                'processing_time': '7 to 15 Days.',
                'official_website': 'https://edistrict.py.gov.in/',  # Generic example portal
                'document_checklist': 'Aadhaar Card\nRation Card\nSalary Slip / IT Returns\nSelf Declaration Form',
                'direct_apply_available': True,
            },
            {
                'name': 'Caste Certificate',
                'document_type': 'certificate',
                'description': 'A Caste Certificate is your "Community Membership Card". It shows that you belong to a specific group like SC, ST, or OBC. This helps the government make sure everyone gets a fair chance in life.',
                'purpose': 'Its main job is to help you get special seats in colleges, jobs, or scholarships that are reserved for your community. It ensures that everyone can grow together!',
                'eligibility': 'You must belong to a group that is listed by the government in your state. Usually, if your father has one, you are eligible too!',
                'required_documents': '1. Your father\'s or grandfather\'s Caste Certificate\n2. Your Aadhaar card\n3. An affidavit (a signed promise) stating your caste for the record.',
                'step_by_step_guide': '1. Find the Portal: Visit your state\'s Revenue or e-District website.\n2. Apply: Choose "Caste Certificate" and fill in your family tree details.\n3. Link to Family: You must show proof that your relatives belong to the same caste.\n4. Verification: An officer will check your records and might visit your neighborhood to confirm.\n5. Print it out: Once they are sure, the certificate is issued online for you to print.',
                'fees': 'Nominal charge (₹10 to ₹50).',
                'processing_time': 'Usually 15 to 30 days because it needs careful verification.',
                'official_website': 'https://edistrict.py.gov.in/',
                'common_mistakes': '1. No Family Proof: It\'s very hard to get a caste certificate if no one else in your family has one.\n2. Spelling Errors: Ensure your caste sub-group is spelled exactly as it is in the official list.\n3. Old Format: Some states require a new digital format, so check if you need to upgrade an old one.',
                'document_checklist': 'Aadhaar Card\nOld Caste Cert of Father/Relatives\nAffidavit of Caste\nAddress Proof',
                'direct_apply_available': True,
            },
            {
                'name': 'Birth / Death Certificate',
                'document_type': 'registry',
                'description': 'A Birth Certificate is your "Official Entry into the World". It\'s the very first ID a person gets! A Death Certificate is the official record of a person\'s journey ending.',
                'purpose': 'You need a Birth Certificate for everything—getting school admission, making a Passport, and proving your age. It is the foundation for all other documents!',
                'eligibility': 'Any baby born in India is eligible for a Birth Certificate. It must be registered within 21 days of birth to make it easy and free.',
                'required_documents': '1. Hospital "Discharge Slip" (this is the most important!)\n2. Aadhaar cards of both parents\n3. A small form filled by the parents.',
                'step_by_step_guide': '1. Hospital Report: Most modern hospitals automatically send the details to the government office for you.\n2. Check Online: Visit the CRS (Civil Registration System) portal for your area.\n3. Search: Look for the record using the date of birth and parents\' names.\n4. Download: If the hospital did their job, it will be there! You can just download the digital version.\n5. Late Registration: If it wasn\'t done in 21 days, you might have to visit the Municipal office in person.',
                'fees': 'Free if you do it within 21 days! If you wait longer, you have to pay a small late fee.',
                'processing_time': 'Usually issued within 7 days once the data is in the system.',
                'official_website': 'https://crsorgi.gov.in/',
                'common_mistakes': '1. Wrong Name Spelling: Check the spelling of the baby\'s name carefully before the hospital submits it!\n2. Delay: Don\'t wait more than 21 days or you will have to deal with more paperwork.\n3. Parents\' ID: Ensure the parents\' names on the hospital slip match their Aadhaar cards.',
                'document_checklist': 'Hospital Discharge Slip\nParents\' Aadhaar Cards\nMarriage Certificate (optional)\nDeclaration by Family Head',
                'direct_apply_available': True,
            },
            {
                'name': 'Ration Card',
                'document_type': 'permit',
                'description': 'A Ration Card is your family\'s "Food Security Pass". It ensures that every family in India can get essential food items like rice, wheat, and sugar at very low prices from special government shops.',
                'purpose': 'It helps families get affordable food. It is also a very powerful document to prove who all are in your family and where you live.',
                'eligibility': 'Any family can apply! The type of card you get (like BPL for support or APL) depends on how much the family earns.',
                'required_documents': '1. Aadhaar cards of every single family member\n2. Current address proof (like a light bill)\n3. A group photo of the whole family or just the head of the family.',
                'step_by_step_guide': '1. State Food Portal: Visit your state\'s Food and Civil Supplies website.\n2. Add Members: Enter the details of everyone living in your house.\n3. Choose Card Type: Select the category based on your income.\n4. Local Verification: A food inspector will visit your house to see your kitchen and verify your members.\n5. Collect Card: Once they approve, your new card is issued and you can start buying from your local "Fair Price Shop".',
                'fees': 'Very cheap (₹5 to ₹45) for the printing of the booklet or smart card.',
                'processing_time': 'Usually takes about 15 to 45 days.',
                'official_website': 'https://nfsa.gov.in/',
                'common_mistakes': '1. Missing Members: Make sure everyone\'s Aadhaar is linked, or they won\'t get their food share.\n2. Wrong Shop: You must choose the Ration shop closest to your house.\n3. Mobile Link: Your Ration card should be linked to the mobile number of the head of the family.',
                'document_checklist': 'Aadhaar cards of all family members\nElectricity bill\nIncome certificate\nPassport size photo of HOF',
                'direct_apply_available': True,
            },
        ]

        for d in docs_data:
            GovernmentDocument.objects.get_or_create(name=d['name'], defaults=d)
        
        # Link 8 of them to ApplicationService (the mock portal system)
        service_map = {
            'Aadhaar Card': 'aadhaar_card',
            'PAN Card': 'pan_card',
            'Indian Passport': 'passport',
            'Driving License': 'driving_license',
            'Voter ID Card (EPIC)': 'voter_id',
            'Income Certificate': 'income_certificate',
            'Caste Certificate': 'caste_certificate',
            'Ration Card': 'ration_card'
        }

        # Define realistic application form fields for each service
        fields_map = {
            'Aadhaar Card': 'full_name, date_of_birth, gender, mobile_number, email_id, residential_address, pincode',
            'PAN Card': 'full_name, fathers_name, date_of_birth, gender, aadhaar_number, mobile_number, email_id, residential_address',
            'Indian Passport': 'full_name, date_of_birth, place_of_birth, gender, marital_status, aadhaar_number, mobile_number, residential_address, nearest_police_station',
            'Driving License': 'full_name, date_of_birth, blood_group, educational_qualification, aadhaar_number, mobile_number, residential_address',
            'Voter ID Card (EPIC)': 'full_name, date_of_birth, gender, relatives_name, relationship_type, mobile_number, residential_address',
            'Income Certificate': 'applicant_name, fathers_name, date_of_birth, gender, annual_income, aadhaar_number, mobile_number, residential_address, purpose_of_certificate',
            'Caste Certificate': 'applicant_name, fathers_name, date_of_birth, caste_category, sub_caste, aadhaar_number, mobile_number, residential_address',
            'Ration Card': 'head_of_family_name, fathers_name, date_of_birth, gender, total_family_members, annual_income, aadhaar_number, residential_address'
        }

        for doc in GovernmentDocument.objects.all():
            if doc.name in service_map:
                ApplicationService.objects.get_or_create(
                    name=service_map[doc.name],
                    defaults={
                        'description': doc.description,
                        'eligibility': doc.eligibility,
                        'required_fields': fields_map.get(doc.name, 'full_name, date_of_birth, mobile_number, residential_address'),
                        'fees': doc.fees,
                        'processing_days': 15,
                        'direct_apply': doc.direct_apply_available,
                        'official_website': doc.official_website,
                        'application_format_url': f"{doc.official_website}forms/application_format.pdf" if doc.official_website else ""
                    }
                )

        self.stdout.write('[SUCCESS] Government Documents and Application Services created')

    def create_workplace_laws(self):
        """Seed 5 major corporate and office laws"""
        laws = [
            {
                'title': 'Sexual Harassment of Women at Workplace (PoSH) Act, 2013',
                'short_name': 'PoSH Act',
                'applies_to': 'Every workplace setting in India (Private, Public, Organized, Unorganized). Mandates an Internal Complaints Committee (ICC) if there are 10 or more employees.',
                'description': 'A landmark law protecting women from sexual harassment at their place of work. It defines what constitutes harassment and mandates employers to build a safe environment.',
                'employee_rights': '- Right to a safe working environment.\n- Right to file a complaint within 3 months of the incident.\n- Right to request transfer or 3 months leave during the inquiry.\n- Identity protection of the complainant during the proceedings.',
                'employer_duties': '- Must establish an Internal Complaints Committee (ICC) with an external member.\n- Display penal consequences of workplace harassments openly.\n- Organize awareness programs at regular intervals.\n- File an annual report of complaints to the district officer.',
                'violation_consequences': '- Penalty up to ₹50,000 for non-compliance on the first offence.\n- Cancellation of business license or registration for repeated offences by the employer.\n- Compensation awarded to the victim based on mental trauma, loss in career, and medical expenses.',
                'where_to_complain': 'Internal Complaints Committee (ICC) of the company.\nIf no ICC exists or the complaint is against the employer, contact the Local Complaints Committee (LCC) at the District Officer level.'
            },
            {
                'title': 'Maternity Benefit (Amendment) Act, 2017',
                'short_name': 'Maternity Act',
                'applies_to': 'Any establishment (factory, mine, plantation, shop, or commercial establishment) employing 10 or more people.',
                'description': 'Regulates the employment of women in certain establishments for certain periods before and after child-birth and provides for maternity benefit.',
                'employee_rights': '- Maximum of 26 weeks paid maternity leave (for the first 2 children).\n- 12 weeks of leave for commissioning and adopting mothers.\n- Right to work from home, if the nature of work allows it, after 26 weeks.\n- Protection against dismissal or discharge during the maternity leave period.',
                'employer_duties': '- Mandatory to provide crèche (daycare) facilities if the establishment has 50 or more employees.\n- Allow women 4 visits a day to the crèche.\n- Must inform women of these benefits in writing upon joining the firm.',
                'violation_consequences': '- Imprisonment of 3 months to 1 year for the employer.\n- Fine ranging from ₹10,000 to ₹50,000.\n- Court order forcing the company to pay the withheld maternity benefits.',
                'where_to_complain': 'State Labour Commissioner or the designated Inspector under the Maternity Benefit Act.'
            },
            {
                'title': 'Minimum Wages Act, 1948',
                'short_name': 'Minimum Wages Act',
                'applies_to': 'All scheduled employments (factories, agriculture, shops, commercial establishments) across India.',
                'description': 'An Act to provide for fixing minimum rates of wages in certain employments. Ensures that employees cannot be exploited by being paid unlivable wages.',
                'employee_rights': '- Right to receive the state-mandated minimum wage for their skill category (Unskilled, Semi-skilled, Skilled).\n- Payment must be made in cash (or legally authorized transfers) and on time.\n- Overtime pay at twice the ordinary rate of wages if working more than standard shifting hours.',
                'employer_duties': '- Must pay wages without unauthorized deductions.\n- Maintain proper registers and records of wages, hours, and receipts.\n- Issue authentic wage slips to every employee.',
                'violation_consequences': '- Imprisonment of up to 6 months.\n- Fine spanning up to ₹10,000 or greater depending on state amendments.\n- Order to pay the difference plus compensation up to 10 times the unpaid amount.',
                'where_to_complain': 'Assistant Labour Commissioner (Central/State) or Labor Courts.'
            },
            {
                'title': 'Payment of Gratuity Act, 1972',
                'short_name': 'Gratuity Act',
                'applies_to': 'Every factory, mine, oilfield, plantation, port, railway company, and shop/establishment employing 10 or more persons.',
                'description': 'A statutory benefit paid by an employer to an employee in appreciation of long and continuous service to the company.',
                'employee_rights': '- Guaranteed gratuity payment upon resignation, retirement, death, or disablement IF continuous service of 5 years is completed.\n- (No 5-year requirement in case of death or disablement).\n- Calculated as 15 days of last drawn salary for every completed year of service.',
                'employer_duties': '- Must calculate and pay the gratuity amount within 30 days from when it becomes payable.\n- Obtain an insurance policy to cover gratuity liabilities or establish an approved gratuity fund.',
                'violation_consequences': '- To avoid payment, false statements can lead to 6 months imprisonment.\n- Default in payment can lead to 6 months to 2 years imprisonment.\n- Ordered to pay the gratuity with compound interest.',
                'where_to_complain': 'Controlling Authority designated under the Payment of Gratuity Act (usually the Assistant Labour Commissioner).'
            },
            {
                'title': 'Shops and Establishments Act (State-wise)',
                'short_name': 'Shops Act',
                'applies_to': 'All shops, commercial establishments, hotels, theaters, and IT parks (depending on state exemptions).',
                'description': 'A state-level legislation that regulates the conditions of work and employment in shops and commercial establishments.',
                'employee_rights': '- Mandated maximum working hours (usually 8-9 hours a day, 48 a week).\n- Fixed number of privileged, casual, and sick leaves.\n- Guaranteed minimum notice period before termination.\n- Special protections for women working in night shifts (e.g. mandated drop facilities).',
                'employer_duties': '- Mandatory registration of the business under the Act within 30 days of commencement.\n- Prevent discrimination.\n- Provide a clean, ventilated, and well-lit working environment.',
                'violation_consequences': '- Financial penalties for non-registration or record-keeping failures.\n- Suspension of establishment license for severe recurring health and safety violations.',
                'where_to_complain': 'State Labour Department or local Municipal Inspector designated under the Act.'
            },
            {
                'title': 'Employees\' Provident Funds and Miscellaneous Provisions Act, 1952',
                'short_name': 'EPF Act',
                'applies_to': 'Any establishment employing 20 or more persons (or fewer if voluntarily opted in).',
                'description': 'A mandatory social security and retirement savings scheme for employees in India.',
                'employee_rights': '- Right to have 12% of basic salary matched by the employer for retirement savings.\n- Right to withdraw partial funds for emergencies (medical, marriage, house purchase).\n- Right to transfer PF account digitally when switching jobs.',
                'employer_duties': '- Must register with the EPFO within 1 month of reaching 20 employees.\n- Must deposit both employee and employer contributions by the 15th of every month.\n- Keep accurate records of all contributing employees.',
                'violation_consequences': '- Non-payment or delayed payment attracts heavy penal damages (up to 25% per annum) and interest.\n- Imprisonment up to 3 years and fines up to ₹10,000 for failing to deposit the deducted amount.',
                'where_to_complain': 'Employees\' Provident Fund Organisation (EPFO) portal (EPFiGMS) or the Regional PF Commissioner.'
            },
            {
                'title': 'Equal Remuneration Act, 1976',
                'short_name': 'Equal Pay Act',
                'applies_to': 'All employers and establishments across India, regardless of sector or size.',
                'description': 'An act to provide for the payment of equal remuneration to men and women workers and for the prevention of discrimination.',
                'employee_rights': '- Right to receive equal pay for equal work or work of a similar nature, irrespective of gender.\n- Protection against discrimination in recruitment, training, or promotion processes.',
                'employer_duties': '- Ensure wages are not lowered for one gender to equalize pay.\n- Maintain proper registers detailing the workforce gender ratio and pay scales.\n- Prevent any biases during the hiring pipeline.',
                'violation_consequences': '- Fines ranging from ₹10,000 to ₹20,000 or imprisonment ranging from 3 months to 1 year.\n- Repeated offences multiply the severity of the penalties.',
                'where_to_complain': 'State Labour Commissioner or appointed inspectors under the Equal Remuneration Act.'
            },
            {
                'title': 'Employees\' State Insurance Act, 1948',
                'short_name': 'ESI Act',
                'applies_to': 'Factories and certain establishments employing 10 or more persons (20 in some states) with employees earning ₹21,000 or less per month.',
                'description': 'A massive social security system designed to provide socio-economic protection to workers in organized sectors against events like sickness, maternity, and disability.',
                'employee_rights': '- Free comprehensive medical care for the employee and their immediate family.\n- Cash benefits during sick leave (up to 91 days at 70% of wages).\n- Maternity benefits and disability/death compensation for dependents.',
                'employer_duties': '- Mandatory registration on the ESIC portal.\n- Deduct 0.75% of employee wages and contribute 3.25% from the employer side.\n- File ESI returns every 6 months.',
                'violation_consequences': '- Prosecutable offence with imprisonment up to 3 years for withholding contributions.\n- Damages up to 100% of the arrears can be claimed by the ESIC corporation.',
                'where_to_complain': 'Employees State Insurance Corporation (ESIC) portal (Samadhan) or local ESI branch offices.'
            },
            {
                'title': 'Industrial Disputes Act, 1947',
                'short_name': 'ID Act',
                'applies_to': 'All industrial establishments in India. Protects "workmen" (excludes managerial/administrative staff).',
                'description': 'Secures industrial peace and harmony by providing machinery and procedure for the investigation and settlement of industrial disputes.',
                'employee_rights': '- Protection against unfair, illegal termination or sudden mass layoffs.\n- Right to a minimum 30 days formatted notice period before retrenchment (or pay in lieu).\n- Right to severance pay (15 days average pay per year of continuous service).',
                'employer_duties': '- Establish a Grievance Redressal Committee if employing more than 20 workmen.\n- Gain government permission before closing down an establishment employing more than 100 people.\n- Follow the "Last in, First out" principle during legitimate layoffs.',
                'violation_consequences': '- Imprisonment of up to 6 months or fines if employers illegally shut down operations or ignore tribunal awards.',
                'where_to_complain': 'Labor Conciliation Officer, Labour Court, or the Industrial Tribunal.'
            }
        ]

        from rights.models import WorkplaceLaw
        
        for data in laws:
            WorkplaceLaw.objects.get_or_create(
                title=data['title'],
                defaults=data
            )
            
        self.stdout.write('[SUCCESS] Corporate Workplace Laws created')
