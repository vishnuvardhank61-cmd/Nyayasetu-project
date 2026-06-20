from django.core.management.base import BaseCommand
from documents.models import GovernmentDocument
from applications.models import ApplicationService

class Command(BaseCommand):
    help = 'Seeds high-impact Government Documents and Services with Real-Form mirroring'

    def handle(self, *args, **options):
        # 1. Seed Government Documents (Learning-First Guides)
        documents = [
            {
                'name': 'Aadhaar Card (UIDAI)',
                'document_type': 'identity',
                'description': 'Aadhaar is a 12-digit unique identity number that can be obtained by residents of India, based on their biometric and demographic data.',
                'purpose': 'Proof of identity and address across India; essential for availing government subsidies and financial services.',
                'eligibility': 'Any resident of India (including infants and foreigners staying for >182 days).',
                'required_documents': 'Proof of Identity (e.g. Voter ID), Proof of Address (e.g. Electricity Bill), Proof of DOB (e.g. Birth Certificate).',
                'step_by_step_guide': '1. Locate an Enrolment Center. 2. Fill the enrolment form. 3. Get biometrics (photo, iris scan, fingerprints) done. 4. Collect acknowledgement slip.',
                'fees': 'First enrolment is FREE. Mandatory Biometric Update (Age 5 and 15) is FREE.',
                'processing_time': 'up to 90 days',
                'official_website': 'https://uidai.gov.in/',
                'common_mistakes': 'Mismatch between spelling on different documents; blurry photocopies; outdated address proofs.',
                'document_checklist': 'Aadhaar Enrolment Form\nOriginal Proof of Identity (POI)\nOriginal Proof of Address (POA)\nOriginal Proof of DOB',
                'direct_apply_available': True,
                'offline_centers': 'Aadhaar Seva Kendras, Designated Post Offices, and Banks.',
            },
            {
                'name': 'Permanent Account Number (PAN) Card',
                'document_type': 'identity',
                'description': 'PAN is a unique 10-character alphanumeric identifier issued by the Income Tax Department.',
                'purpose': 'Essential for financial transactions like opening a bank account, receiving taxable salary, or buying/selling assets.',
                'eligibility': 'Any individual, company, or entity requiring a financial footprint in India.',
                'required_documents': 'Identity Proof, Address Proof, and Date of Birth proof.',
                'step_by_step_guide': '1. Apply online via NSDL/UTIITSL. 2. Select Form 49A. 3. Pay fee. 4. Send physical documents if e-KYC is not used.',
                'fees': '₹107 (within India), ₹1017 (outside India)',
                'processing_time': '15-20 business days',
                'official_website': 'https://www.onlineservices.nsdl.com/paam/endUserRegisterContact.html',
                'common_mistakes': 'Card name mismatch with Aadhaar; incorrect father\'s name; unclear signature.',
                'document_checklist': 'Copy of Aadhaar Card\n2 Passport Size Photos (if not using e-KYC)\nSelf-attested identity proof',
                'direct_apply_available': True,
                'offline_centers': 'PAN Service Centers, NSDL Tin-Facilitation Centers.',
            },
            {
                'name': 'Ration Card (NFSA)',
                'document_type': 'registry',
                'description': 'Official document issued by State Governments to households that are eligible to purchase subsidized food grains.',
                'purpose': 'Provides food security to low-income families and serves as a verified residency proof.',
                'eligibility': 'Based on annual income and household criteria defined by the State (AP/Telangana).',
                'required_documents': 'Aadhaar copies of all family members, Income certificate, Electricity bill, Bank passbook.',
                'step_by_step_guide': '1. Visit MeeSeva or Grama Sachivalayam. 2. Submit physical application with family photo. 3. Field inspection by VRO.',
                'fees': 'Nominal processing fee (₹15-₹35)',
                'processing_time': '30 days',
                'official_website': 'https://epdsap.ap.gov.in/',
                'common_mistakes': 'Multiple family members in different cards; incorrect income details; missing Aadhaar seeding.',
                'document_checklist': 'Family Photograph\nMember Aadhaar Cards\nOld Ration Card (if any)\nIncome Certificate',
                'direct_apply_available': False,
                'offline_centers': 'MeeSeva Centers, Tahsildar Office, Civil Supplies Dept.',
            },
        ]

        for doc in documents:
            GovernmentDocument.objects.update_or_create(name=doc['name'], defaults=doc)

        # 2. Seed Application Services (Real-Form Mirroring)
        services = [
            {
                'name': 'aadhaar_card',
                'description': 'Apply for New Aadhaar Enrolment or Update existing details.',
                'eligibility': 'All residents of India.',
                'required_fields': '{"fields": ["full_name", "gender", "age", "mobile", "email", "address", "parent_name", "biometric_consent"]}',
                'fees': '₹0 (New) / ₹50 (Update)',
                'processing_days': 90,
                'direct_apply': True,
                'official_website': 'https://uidai.gov.in/',
            },
            {
                'name': 'pan_card',
                'description': 'Official application for New PAN (Form 49A).',
                'eligibility': 'Individuals and Businesses.',
                'required_fields': '{"fields": ["full_name", "fathers_name", "date_of_birth", "aadhaar_number", "source_of_income", "address_type", "mobile_number"]}',
                'fees': '₹107',
                'processing_days': 15,
                'direct_apply': True,
                'official_website': 'https://www.onlineservices.nsdl.com/',
            },
            {
                'name': 'income_certificate',
                'description': 'Income Certificate required for educational scholarship and subsidies.',
                'eligibility': 'Residents of AP/Telangana with verified income sources.',
                'required_fields': '{"fields": ["applicant_name", "ration_card_number", "aadhaar_number", "annual_income", "purpose_of_certificate", "residential_address"]}',
                'fees': '₹35',
                'processing_days': 7,
                'direct_apply': False,
                'offline_instructions': 'Visit nearest MeeSeva or Grama Sachivalayam with Ration Card and Aadhaar. Biometric authentication required.',
            },
        ]

        for svc in services:
            ApplicationService.objects.update_or_create(name=svc['name'], defaults=svc)

        self.stdout.write(self.style.SUCCESS('Successfully seeded Official Service Portal data!'))
