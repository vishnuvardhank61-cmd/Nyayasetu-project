from django.core.management.base import BaseCommand
from police_stations.models import PoliceStation
from regions.models import State

class Command(BaseCommand):
    help = 'Seeds Police Stations for the Bachupally/Nizampet cluster specifically'

    def handle(self, *args, **options):
        ts = State.objects.filter(code='TS').first()
        if not ts:
            self.stdout.write("Run seed_data first.")
            return

        stations = [
            # User Cluster: Bachupally / Nizampet / Miyapur
            {'name': 'Bachupally PS', 'state': ts, 'district': 'Medchal-Malkajgiri', 'city': 'Hyderabad', 'address': 'Bachupally Main Road', 'phone': '040-27854817', 'latitude': 17.5350, 'longitude': 78.3680, 'office_type': 'police'},
            {'name': 'Nizampet Police Outpost', 'state': ts, 'district': 'Medchal-Malkajgiri', 'city': 'Hyderabad', 'address': 'Nizampet Village Road', 'phone': '040-27854820', 'latitude': 17.5185, 'longitude': 78.3845, 'office_type': 'police'},
            {'name': 'Miyapur PS', 'state': ts, 'district': 'Cyberabad', 'city': 'Hyderabad', 'address': 'Miyapur Main Road', 'phone': '040-27854032', 'latitude': 17.4950, 'longitude': 78.3490, 'office_type': 'police'},
            {'name': 'KPHB PS', 'state': ts, 'district': 'Cyberabad', 'city': 'Hyderabad', 'address': 'KPHB Colony', 'phone': '040-27854025', 'latitude': 17.4855, 'longitude': 78.3888, 'office_type': 'police'},
            {'name': 'Pragathi Nagar PS', 'state': ts, 'district': 'Medchal-Malkajgiri', 'city': 'Hyderabad', 'address': 'Pragathi Nagar, Kukatpally', 'phone': '040-27854830', 'latitude': 17.5135, 'longitude': 78.3995, 'office_type': 'police'},
            {'name': 'Kukatpally PS', 'state': ts, 'district': 'Cyberabad', 'city': 'Hyderabad', 'address': 'Kukatpally Housing Board', 'phone': '040-27854022', 'latitude': 17.4845, 'longitude': 78.4010, 'office_type': 'police'},
            {'name': 'Bollaram PS', 'state': ts, 'district': 'Sangareddy', 'city': 'Hyderabad', 'address': 'Industrial Area, Bollaram', 'phone': '040-27854850', 'latitude': 17.5580, 'longitude': 78.3585, 'office_type': 'police'},
            
            # Traffic Stations nearby
            {'name': 'Kukatpally Traffic PS', 'state': ts, 'district': 'Cyberabad', 'city': 'Hyderabad', 'address': 'Kukatpally Main Road', 'phone': '040-27854045', 'latitude': 17.4840, 'longitude': 78.3990, 'office_type': 'traffic'},
            {'name': 'Miyapur Traffic PS', 'state': ts, 'district': 'Cyberabad', 'city': 'Hyderabad', 'address': 'Miyapur Junction', 'phone': '040-27854048', 'latitude': 17.4960, 'longitude': 78.3510, 'office_type': 'traffic'},
        ]

        count = 0
        for data in stations:
            if not PoliceStation.objects.filter(name=data['name'], city=data['city']).exists():
                PoliceStation.objects.create(**data)
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f"Successfully added {count} stations in the Bachupally/Nizampet area!"))
