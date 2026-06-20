import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nyayasetu.settings')
django.setup()

import json
from applications.models import ApplicationService

service = ApplicationService.objects.get(name='caste_certificate')
fields = []
if service.required_fields:
    try:
        fields_data = json.loads(service.required_fields)
        fields = fields_data.get('fields', [])
    except Exception as e:
        fields = [f.strip() for f in service.required_fields.split(',')]
print('FIELDS =', fields)
