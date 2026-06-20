from django.core.management.base import BaseCommand
from police_stations.models import PoliceStation
from regions.models import State

class Command(BaseCommand):
    help = 'Massive seeding of Police Stations for Telangana and Andhra Pradesh'

    def handle(self, *args, **options):
        self.stdout.write("Starting massive expansion for AP and Telangana...")
        
        ts = State.objects.filter(code='TS').first()
        ap = State.objects.filter(code='AP').first()
        
        if not ts or not ap:
            self.stdout.write(self.style.ERROR("States TS or AP not found in DB. Run seed_data first."))
            return

        stations = [
            # --- TELANGANA (TS) ---
            # Hyderabad Core
            {'name': 'Banjara Hills PS', 'state': ts, 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'Road No 12, Hyderabad', 'phone': '040-27853503', 'latitude': 17.4126, 'longitude': 78.4358, 'office_type': 'police'},
            {'name': 'Jubilee Hills PS', 'state': ts, 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'Road No 36, Hyderabad', 'phone': '040-27853505', 'latitude': 17.4301, 'longitude': 78.4067, 'office_type': 'police'},
            {'name': 'Punjagutta PS', 'state': ts, 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'Panjagutta X Roads', 'phone': '040-27853508', 'latitude': 17.4251, 'longitude': 78.4526, 'office_type': 'police'},
            {'name': 'Abids PS', 'state': ts, 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'Abids Main Road', 'phone': '040-27853512', 'latitude': 17.3912, 'longitude': 78.4770, 'office_type': 'police'},
            {'name': 'Secunderabad PS', 'state': ts, 'district': 'Hyderabad', 'city': 'Secunderabad', 'address': 'RP Road', 'phone': '040-27853520', 'latitude': 17.4399, 'longitude': 78.4983, 'office_type': 'police'},
            # Cyberabad / IT Zone
            {'name': 'Gachibowli PS', 'state': ts, 'district': 'Rangareddy', 'city': 'Hyderabad', 'address': 'Gachibowli X Roads', 'phone': '040-27854001', 'latitude': 17.4442, 'longitude': 78.3650, 'office_type': 'police'},
            {'name': 'Madhapur PS', 'state': ts, 'district': 'Rangareddy', 'city': 'Hyderabad', 'address': 'Cyber Towers Road', 'phone': '040-27854005', 'latitude': 17.4483, 'longitude': 78.3915, 'office_type': 'police'},
            {'name': 'Raidurgam PS', 'state': ts, 'district': 'Rangareddy', 'city': 'Hyderabad', 'address': 'Khajaguda X Roads', 'phone': '040-27854010', 'latitude': 17.4285, 'longitude': 78.3780, 'office_type': 'police'},
            # Other Cities TS
            {'name': 'Warangal Central PS', 'state': ts, 'district': 'Warangal', 'city': 'Warangal', 'address': 'Hanamkonda Road', 'phone': '0870-2423333', 'latitude': 17.9689, 'longitude': 79.5941, 'office_type': 'police'},
            {'name': 'Nizamabad Town PS', 'state': ts, 'district': 'Nizamabad', 'city': 'Nizamabad', 'address': 'Main Market Area', 'phone': '08462-221100', 'latitude': 18.6725, 'longitude': 78.0941, 'office_type': 'police'},
            {'name': 'Karimnagar I-Town PS', 'state': ts, 'district': 'Karimnagar', 'city': 'Karimnagar', 'address': 'Bus Stand Road', 'phone': '0878-2241100', 'latitude': 18.4386, 'longitude': 79.1288, 'office_type': 'police'},
            {'name': 'Khammam Town PS', 'state': ts, 'district': 'Khammam', 'city': 'Khammam', 'address': 'Wyra Road', 'phone': '08742-221100', 'latitude': 17.2473, 'longitude': 80.1514, 'office_type': 'police'},
            {'name': 'Nalgonda Town PS', 'state': ts, 'district': 'Nalgonda', 'city': 'Nalgonda', 'address': 'Clock Tower Centre', 'phone': '08682-221100', 'latitude': 17.0575, 'longitude': 79.2684, 'office_type': 'police'},
            {'name': 'Mahbubnagar Town PS', 'state': ts, 'district': 'Mahbubnagar', 'city': 'Mahbubnagar', 'address': 'Main Road', 'phone': '08542-242100', 'latitude': 16.7367, 'longitude': 77.9819, 'office_type': 'police'},
            # Traffic Stations TS
            {'name': 'Traffic Training Institute Begumpet', 'state': ts, 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'Begumpet', 'phone': '040-27852482', 'latitude': 17.4448, 'longitude': 78.4664, 'office_type': 'traffic'},
            {'name': 'Cyberabad Traffic Control', 'state': ts, 'district': 'Rangareddy', 'city': 'Gachibowli', 'address': 'Gachibowli Hub', 'phone': '040-27854040', 'latitude': 17.4470, 'longitude': 78.3670, 'office_type': 'traffic'},
            {'name': 'Warangal Traffic PS', 'state': ts, 'district': 'Warangal', 'city': 'Warangal', 'address': 'Subedari', 'phone': '0870-2423334', 'latitude': 17.9710, 'longitude': 79.5960, 'office_type': 'traffic'},

            # --- ANDHRA PRADESH (AP) ---
            # Visakhapatnam (Vizag)
            {'name': 'RK Beach PS', 'state': ap, 'district': 'Visakhapatnam', 'city': 'Visakhapatnam', 'address': 'Marine Drive, RK Beach', 'phone': '0891-2561100', 'latitude': 17.7145, 'longitude': 83.3236, 'office_type': 'police'},
            {'name': 'Gajuwaka PS', 'state': ap, 'district': 'Visakhapatnam', 'city': 'Visakhapatnam', 'address': 'Old Gajuwaka Junction', 'phone': '0891-2511100', 'latitude': 17.6912, 'longitude': 83.2105, 'office_type': 'police'},
            {'name': 'MVP Colony PS', 'state': ap, 'district': 'Visakhapatnam', 'city': 'Visakhapatnam', 'address': 'MVP Double Road', 'phone': '0891-2551100', 'latitude': 17.7423, 'longitude': 83.3344, 'office_type': 'police'},
            # Vijayawada
            {'name': 'Governorpet PS', 'state': ap, 'district': 'Krishna', 'city': 'Vijayawada', 'address': 'Museum Road', 'phone': '0866-2575444', 'latitude': 16.5126, 'longitude': 80.6267, 'office_type': 'police'},
            {'name': 'Patamata PS', 'state': ap, 'district': 'Krishna', 'city': 'Vijayawada', 'address': 'Benz Circle Area', 'phone': '0866-2541100', 'latitude': 16.4988, 'longitude': 80.6625, 'office_type': 'police'},
            {'name': 'Vijayawada Traffic Control', 'state': ap, 'district': 'Krishna', 'city': 'Vijayawada', 'address': 'Besant Road', 'phone': '0866-2571212', 'latitude': 16.5100, 'longitude': 80.6400, 'office_type': 'traffic'},
            # Guntur
            {'name': 'Lalapet PS Guntur', 'state': ap, 'district': 'Guntur', 'city': 'Guntur', 'address': 'Lalapet Junction', 'phone': '0863-2231100', 'latitude': 16.3067, 'longitude': 80.4365, 'office_type': 'police'},
            {'name': 'Arundelpet PS Guntur', 'state': ap, 'district': 'Guntur', 'city': 'Guntur', 'address': 'Main Road Guntur', 'phone': '0863-2221100', 'latitude': 16.3120, 'longitude': 80.4440, 'office_type': 'police'},
            # Other Cities AP
            {'name': 'Tirupati Town PS-I', 'state': ap, 'district': 'Chittoor', 'city': 'Tirupati', 'address': 'Town Hall Area', 'phone': '0877-2221100', 'latitude': 13.6288, 'longitude': 79.4192, 'office_type': 'police'},
            {'name': 'Kurnool Town PS', 'state': ap, 'district': 'Kurnool', 'city': 'Kurnool', 'address': 'Collectorate Road', 'phone': '08518-221100', 'latitude': 15.8281, 'longitude': 78.0373, 'office_type': 'police'},
            {'name': 'Nellore Town PS', 'state': ap, 'district': 'Nellore', 'city': 'Nellore', 'address': 'GT Road', 'phone': '0861-2321100', 'latitude': 14.4426, 'longitude': 79.9865, 'office_type': 'police'},
            {'name': 'Rajahmundry III-Town PS', 'state': ap, 'district': 'East Godavari', 'city': 'Rajahmundry', 'address': 'Innespet', 'phone': '0883-2421100', 'latitude': 17.0005, 'longitude': 81.8040, 'office_type': 'police'},
            {'name': 'Kakinada Town PS', 'state': ap, 'district': 'East Godavari', 'city': 'Kakinada', 'address': 'Bhanugudi Junction', 'phone': '0884-2321100', 'latitude': 16.9891, 'longitude': 82.2475, 'office_type': 'police'},
            {'name': 'Anantapur Town PS', 'state': ap, 'district': 'Anantapur', 'city': 'Anantapur', 'address': 'Clock Tower Road', 'phone': '08554-221100', 'latitude': 14.6819, 'longitude': 77.6006, 'office_type': 'police'},
        ]

        count = 0
        for data in stations:
            # Avoid duplicates by name + city + state
            state = data['state']
            if not PoliceStation.objects.filter(name=data['name'], city=data['city'], state=state).exists():
                PoliceStation.objects.create(**data)
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f"Successfully added {count} new stations for AP and Telangana!"))
