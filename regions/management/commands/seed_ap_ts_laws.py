from django.core.management.base import BaseCommand
from regions.models import State, RegionalLaw

class Command(BaseCommand):
    help = 'Seeds detailed Regional Laws for AP and Telangana'

    def handle(self, *args, **options):
        ts = State.objects.filter(code='TS').first()
        ap = State.objects.filter(code='AP').first()
        
        if not ts or not ap:
            self.stdout.write("Run seed_data first.")
            return

        laws = [
            # TELANGANA
            {
                'state': ts,
                'title': 'Telangana Rights in Land and Pattadar Pass Books Act, 2020',
                'act_name': 'New ROR Act',
                'description': 'A landmark law to transparency in land records and simplify the process of land registration through the Dharani portal.',
                'key_provisions': '- Digital maintenance of all land records.\n- Instant mutation of land records upon registration.\n- Issuance of E-Pattadar passbooks.',
                'who_it_applies_to': 'Land owners and farmers in Telangana.',
                'how_to_comply': 'Register through the Dharani portal and ensure your Aadhaar is linked to your land records.'
            },
            {
                'state': ts,
                'title': 'Telangana Municipalities Act, 2019',
                'act_name': 'TS Municipal Act',
                'description': 'Reforms in urban local bodies to ensure better civic amenities and faster approvals for building permissions.',
                'key_provisions': '- Self-certification for building permissions (TS-bPASS).\n- Mandatory Greenery (Haritha Haram) in every municipality.',
                'who_it_applies_to': 'Residents of municipalities in Telangana.',
                'how_to_comply': 'Use the TS-bPASS portal for building approvals.'
            },
            # ANDHRA PRADESH
            {
                'state': ap,
                'title': 'Andhra Pradesh Disha Act, 2019',
                'act_name': 'Disha Act',
                'description': 'Specifically designed for the safety of women and children, ensuring swift investigation and trial in sexual offense cases.',
                'key_provisions': '- Completion of investigation in 7 days.\n- Completion of trial in 14 days.\n- Judgment within 21 days from the date of offense.',
                'who_it_applies_to': 'Victims of sexual offenses in Andhra Pradesh.',
                'how_to_comply': 'Report incidents via Disha App or local police immediately.'
            },
            {
                'state': ap,
                'title': 'AP Guarantee of Public Services Act',
                'act_name': 'RTPS Act AP',
                'description': 'Ensures time-bound delivery of various government services to the citizens of Andhra Pradesh through Village/Ward Secretariats.',
                'key_provisions': '- Right to get services within a stipulated time.\n- Compensation to citizens for delays by officials.',
                'who_it_applies_to': 'All citizens of Andhra Pradesh.',
                'how_to_comply': 'Apply via the GSWS (Gram Ward Secretariat) portal.'
            }
        ]

        count = 0
        for law_data in laws:
            if not RegionalLaw.objects.filter(title=law_data['title'], state=law_data['state']).exists():
                RegionalLaw.objects.create(**law_data)
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f"Successfully added {count} regional laws!"))
