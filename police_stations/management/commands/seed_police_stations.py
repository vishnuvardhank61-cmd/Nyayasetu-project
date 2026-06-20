from django.core.management.base import BaseCommand
from police_stations.models import PoliceStation
from regions.models import State

class Command(BaseCommand):
    help = 'Seeds realistic Police and Traffic Station data for major Indian cities'

    def handle(self, *args, **options):
        self.stdout.write("Seeding comprehensive police and traffic station data...")
        
        # Get states
        states = {s.code: s for s in State.objects.all()}
        
        stations_data = [
            # DELHI (DL)
            {'name': 'Parliament Street Police Station', 'state_code': 'DL', 'district': 'New Delhi', 'city': 'New Delhi', 'address': 'Parliament Street, Connaught Place', 'phone': '011-23361100', 'latitude': 28.6255, 'longitude': 77.2139, 'office_type': 'police'},
            {'name': 'Delhi Traffic Police HQ', 'state_code': 'DL', 'district': 'Central Delhi', 'city': 'New Delhi', 'address': 'Dev Prakash Shastri Marg, Pusa', 'phone': '011-25844444', 'latitude': 28.6365, 'longitude': 77.1687, 'office_type': 'traffic'},
            {'name': 'Hauz Khas Police Station', 'state_code': 'DL', 'district': 'South Delhi', 'city': 'New Delhi', 'address': 'Aurobindo Marg, Hauz Khas', 'phone': '011-26852400', 'latitude': 28.5487, 'longitude': 77.2045, 'office_type': 'police'},
            {'name': 'Connaught Place Traffic Circle', 'state_code': 'DL', 'district': 'New Delhi', 'city': 'New Delhi', 'address': 'Outer Circle, Connaught Place', 'phone': '011-23412300', 'latitude': 28.6328, 'longitude': 77.2197, 'office_type': 'traffic'},
            
            # MAHARASHTRA (MH) - Mumbai & Pune
            {'name': 'Bandra Police Station', 'state_code': 'MH', 'district': 'Mumbai Suburban', 'city': 'Mumbai', 'address': 'Hill Road, Bandra West', 'phone': '022-26423042', 'latitude': 19.0566, 'longitude': 72.8306, 'office_type': 'police'},
            {'name': 'Colaba Police Station', 'state_code': 'MH', 'district': 'Mumbai City', 'city': 'Mumbai', 'address': 'Cusrow Baug, Colaba', 'phone': '022-22852323', 'latitude': 18.9151, 'longitude': 72.8277, 'office_type': 'police'},
            {'name': 'Worli Traffic Police HQ', 'state_code': 'MH', 'district': 'Mumbai City', 'city': 'Mumbai', 'address': 'Sir Pochkhanwala Road, Worli', 'phone': '022-24937747', 'latitude': 19.0016, 'longitude': 72.8149, 'office_type': 'traffic'},
            {'name': 'Shivajinagar Police Station', 'state_code': 'MH', 'district': 'Pune', 'city': 'Pune', 'address': 'Ganeshkhind Road, Shivajinagar', 'phone': '020-25536263', 'latitude': 18.5312, 'longitude': 73.8445, 'office_type': 'police'},
            {'name': 'Pune Traffic Police HQ', 'state_code': 'MH', 'district': 'Pune', 'city': 'Pune', 'address': 'Yerawada, PMPML Depot', 'phone': '020-26208225', 'latitude': 18.5529, 'longitude': 73.8796, 'office_type': 'traffic'},

            # KARNATAKA (KA) - Bangalore
            {'name': 'Cubbon Park Police Station', 'state_code': 'KA', 'district': 'Bangalore Urban', 'city': 'Bangalore', 'address': 'Kasturba Road, Cubbon Park', 'phone': '080-22942517', 'latitude': 12.9733, 'longitude': 77.5947, 'office_type': 'police'},
            {'name': 'Indiranagar Police Station', 'state_code': 'KA', 'district': 'Bangalore Urban', 'city': 'Bangalore', 'address': '100 Feet Road, Indiranagar', 'phone': '080-22942521', 'latitude': 12.9719, 'longitude': 77.6412, 'office_type': 'police'},
            {'name': 'Bangalore Traffic Management Centre', 'state_code': 'KA', 'district': 'Bangalore Urban', 'city': 'Bangalore', 'address': 'Infantry Road', 'phone': '080-22943030', 'latitude': 12.9830, 'longitude': 77.5950, 'office_type': 'traffic'},
            {'name': 'Koramangala Traffic Police Station', 'state_code': 'KA', 'district': 'Bangalore Urban', 'city': 'Bangalore', 'address': '80 Feet Road, Koramangala', 'phone': '080-22943035', 'latitude': 12.9352, 'longitude': 77.6191, 'office_type': 'traffic'},

            # TAMIL NADU (TN) - Chennai
            {'name': 'Anna Salai Police Station', 'state_code': 'TN', 'district': 'Chennai', 'city': 'Chennai', 'address': 'Mount Road, Anna Salai', 'phone': '044-23452500', 'latitude': 13.0638, 'longitude': 80.2520, 'office_type': 'police'},
            {'name': 'Adyar Police Station', 'state_code': 'TN', 'district': 'Chennai', 'city': 'Chennai', 'address': 'Sardar Patel Road, Adyar', 'phone': '044-23452505', 'latitude': 13.0067, 'longitude': 80.2545, 'office_type': 'police'},
            {'name': 'Chennai Traffic Police Control Room', 'state_code': 'TN', 'district': 'Chennai', 'city': 'Chennai', 'address': 'Vepery, Commissioner Office', 'phone': '044-23452336', 'latitude': 13.0888, 'longitude': 80.2647, 'office_type': 'traffic'},

            # TELANGANA (TS) - Hyderabad
            {'name': 'Banjara Hills Police Station', 'state_code': 'TS', 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'Road No 12, Banjara Hills', 'phone': '040-27853503', 'latitude': 17.4126, 'longitude': 78.4358, 'office_type': 'police'},
            {'name': 'Jubilee Hills Police Station', 'state_code': 'TS', 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'Road No 36, Jubilee Hills', 'phone': '040-27853505', 'latitude': 17.4301, 'longitude': 78.4067, 'office_type': 'police'},
            {'name': 'Hyderabad Traffic Police HQ', 'state_code': 'TS', 'district': 'Hyderabad', 'city': 'Hyderabad', 'address': 'Nampally', 'phone': '040-27852482', 'latitude': 17.3888, 'longitude': 78.4682, 'office_type': 'traffic'},
            {'name': 'Cyberabad Traffic Police', 'state_code': 'TS', 'district': 'Rangareddy', 'city': 'Gachibowli', 'address': 'Gachibowli X Roads', 'phone': '040-27854000', 'latitude': 17.4447, 'longitude': 78.3653, 'office_type': 'traffic'},

            # WEST BENGAL (WB) - Kolkata (Wait, check if WB is in states list... no it wasn't. Let's add it if needed, or skip)
            # AP, DL, KA, KL, MH, TN, TS, UP are available.
            
            # UTTAR PRADESH (UP) - Lucknow/Noida
            {'name': 'Hazratganj Police Station', 'state_code': 'UP', 'district': 'Lucknow', 'city': 'Lucknow', 'address': 'Hazratganj Main Market', 'phone': '0522-2214344', 'latitude': 26.8467, 'longitude': 80.9462, 'office_type': 'police'},
            {'name': 'Sector 20 Police Station Noida', 'state_code': 'UP', 'district': 'Gautam Buddh Nagar', 'city': 'Noida', 'address': 'Sector 20, Near Harola', 'phone': '0120-2525111', 'latitude': 28.5847, 'longitude': 77.3159, 'office_type': 'police'},
            {'name': 'Noida Traffic Police HQ', 'state_code': 'UP', 'district': 'Gautam Buddh Nagar', 'city': 'Noida', 'address': 'Sector 14A', 'phone': '0120-2442444', 'latitude': 28.5866, 'longitude': 77.3015, 'office_type': 'traffic'},
            
            # KERALA (KL) - Kochi
            {'name': 'Central Police Station Kochi', 'state_code': 'KL', 'district': 'Ernakulam', 'city': 'Kochi', 'address': 'Broadway, Marine Drive', 'phone': '0484-2351433', 'latitude': 9.9796, 'longitude': 76.2811, 'office_type': 'police'},
            {'name': 'Kochi Traffic Police East', 'state_code': 'KL', 'district': 'Ernakulam', 'city': 'Kochi', 'address': 'High Bridge, Ernakulam', 'phone': '0484-2394100', 'latitude': 9.9888, 'longitude': 76.2858, 'office_type': 'traffic'},
            
            # ANDHRA PRADESH (AP) - Vijayawada
            {'name': 'Governorpet Police Station', 'state_code': 'AP', 'district': 'Krishna', 'city': 'Vijayawada', 'address': 'Governorpet', 'phone': '0866-2575444', 'latitude': 16.5126, 'longitude': 80.6267, 'office_type': 'police'},
            {'name': 'Vijayawada Traffic Control', 'state_code': 'AP', 'district': 'Krishna', 'city': 'Vijayawada', 'address': 'MG Road', 'phone': '0866-2571212', 'latitude': 16.5062, 'longitude': 80.6480, 'office_type': 'traffic'},
        ]

        count = 0
        for data in stations_data:
            state_code = data.pop('state_code')
            state = states.get(state_code)
            if state:
                PoliceStation.objects.update_or_create(
                    name=data['name'],
                    state=state,
                    defaults=data
                )
                count += 1
        
        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {count} stations!"))
