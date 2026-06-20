from django.core.management.base import BaseCommand
from police_stations.models import PoliceStation
from regions.models import State

class Command(BaseCommand):
    help = 'Populates the database with help center data for AP and Telangana'

    def handle(self, *args, **options):
        self.stdout.write("Adding Regional Help Centers...")
        
        ap_state = State.objects.get(name="Andhra Pradesh")
        ts_state = State.objects.get(name="Telangana")
        
        centers = [
            # Andhra Pradesh
            {
                "name": "Vijayawada Central Police Station",
                "office_type": "police",
                "state": ap_state,
                "district": "Krishna",
                "city": "Vijayawada",
                "address": "MG Road, Buckinghampet, Vijayawada, AP - 520002",
                "phone": "0866-2579999",
                "latitude": 16.5062,
                "longitude": 80.6480,
            },
            {
                "name": "Visakhapatnam North Traffic Police Station",
                "office_type": "traffic",
                "state": ap_state,
                "district": "Visakhapatnam",
                "city": "Visakhapatnam",
                "address": "Dwaraka Nagar, Visakhapatnam, AP - 530016",
                "phone": "0891-2565454",
                "latitude": 17.7230,
                "longitude": 83.3013,
            },
            {
                "name": "Guntur Sub-Registrar Office",
                "office_type": "registration",
                "state": ap_state,
                "district": "Guntur",
                "city": "Guntur",
                "address": "Collectorate Road, Guntur, AP - 522004",
                "phone": "0863-2234055",
                "latitude": 16.3067,
                "longitude": 80.4365,
            },
            # Telangana
            {
                "name": "Cyberabad Police Commissionerate",
                "office_type": "police",
                "state": ts_state,
                "district": "Rangareddy",
                "city": "Hyderabad",
                "address": "Gachibowli, Hyderabad, TS - 500032",
                "phone": "040-27853400",
                "latitude": 17.4422,
                "longitude": 78.3489,
            },
            {
                "name": "Nampally Sub-Registrar Office",
                "office_type": "registration",
                "state": ts_state,
                "district": "Hyderabad",
                "city": "Hyderabad",
                "address": "Opposite Gandhi Bhavan, Nampally, Hyderabad, TS - 500001",
                "phone": "040-24602234",
                "latitude": 17.3875,
                "longitude": 78.4718,
            },
            {
                "name": "Warangal Traffic PS",
                "office_type": "traffic",
                "state": ts_state,
                "district": "Warangal",
                "city": "Warangal",
                "address": "Hunter Road, Hanamkonda, Warangal, TS - 506001",
                "phone": "0870-2425555",
                "latitude": 18.0116,
                "longitude": 79.5856,
            }
        ]
        
        for center in centers:
            PoliceStation.objects.update_or_create(
                name=center['name'],
                defaults=center
            )
            
        self.stdout.write(self.style.SUCCESS("AP & Telangana Help Centers Successfully Populated!"))
