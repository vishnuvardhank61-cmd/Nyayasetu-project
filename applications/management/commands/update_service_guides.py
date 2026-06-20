from django.core.management.base import BaseCommand
from applications.models import ApplicationService
from documents.models import GovernmentDocument

class Command(BaseCommand):
    help = 'Populates the updated educational fields for government services and documents'

    def handle(self, *args, **options):
        self.stdout.write("Improving Government Service Data...")

        # --- Aadhaar Card ---
        aadhaar_data = {
            'eligibility': 'Any resident of India (including infants and foreigners living here for >182 days).',
            'description': 'The most essential biometric identity document in India, used as proof of residence and for direct benefit transfers (DBT).',
            'fees': 'Free for first-time enrollment. Rs. 50-100 for biometric/demographic updates.',
            'processing_days': 15,
            'direct_apply': False,
            'offline_instructions': 'Aadhaar requires biometric verification (fingerprints/retina). You MUST visit a permanent Aadhaar Enrollment Center or an authorized Post Office/Bank. Use the official Uidai.gov.in portal only to BOOK an appointment or update address.',
        }
        
        # --- PAN Card ---
        pan_data = {
            'eligibility': 'Any citizen, company, or foreign national earning income in India.',
            'description': 'Permanent Account Number used mainly for tax purposes and opening bank accounts.',
            'fees': 'Rs. 101-107 for physical delivery within India.',
            'processing_days': 7,
            'direct_apply': True,
            'offline_instructions': 'While you can apply online through NSDL or UTIITSL, you can also visit authorized PAN Service Centers (Protean) in your city.',
        }

        # --- Voter ID (EPIC) ---
        voter_data = {
            'eligibility': 'Indian citizen aged 18+ on the qualifying date.',
            'description': 'The official ID issued by the Election Commission of India allowing you to exercise your right to vote.',
            'fees': 'Free of cost.',
            'processing_days': 20,
            'direct_apply': True,
            'offline_instructions': 'Download the Voter Helpline App or visit your local BLO (Booth Level Officer).',
        }

        # Mapping names to data
        service_map = {
            'aadhaar_card': aadhaar_data,
            'pan_card': pan_data,
            'voter_id': voter_data,
        }

        for name, data in service_map.items():
            ApplicationService.objects.update_or_create(
                name=name,
                defaults=data
            )

        self.stdout.write(self.style.SUCCESS("Government Service Action Guides Updated!"))
