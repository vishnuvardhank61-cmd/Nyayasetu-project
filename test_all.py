import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nyayasetu.settings')
django.setup()

import json
from applications.models import ApplicationService

for s in ApplicationService.objects.all():
    fields = []
    if s.required_fields:
        try:
            fd = json.loads(s.required_fields)
            fields = fd.get('fields', [])
        except Exception as e:
            fields = [f.strip() for f in s.required_fields.split(',')]
    print(f'{s.name}: {len(fields)} fields')
