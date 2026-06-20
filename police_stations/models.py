from django.db import models
from regions.models import State


class PoliceStation(models.Model):
    """Police stations, Registration offices, and Traffic offices"""
    
    OFFICE_TYPE_CHOICES = [
        ('police', 'General Police Station'),
        ('traffic', 'Traffic Police Station'),
        ('registration', 'Registration & Sub-Registrar Office'),
        ('meeseva', 'MeeSeva Center'),
        ('mandal', 'Mandal Revenue Office (MRO)'),
    ]

    name = models.CharField(max_length=200, db_index=True)
    office_type = models.CharField(max_length=20, choices=OFFICE_TYPE_CHOICES, default='police')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='police_stations')
    district = models.CharField(max_length=100, db_index=True)
    city = models.CharField(max_length=100, db_index=True)
    
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    
    # Google Maps coordinates
    latitude = models.FloatField(help_text="GPS latitude")
    longitude = models.FloatField(help_text="GPS longitude")
    
    jurisdiction = models.TextField(blank=True, help_text="Area of jurisdiction")
    
    # Operation hours
    opening_hours = models.CharField(max_length=200, default="24/7")
    
    keywords = models.CharField(max_length=300, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Police Station'
        verbose_name_plural = 'Police Stations'
        ordering = ['state', 'district', 'name']
        indexes = [
            models.Index(fields=['state', 'city']),
            models.Index(fields=['district']),
        ]
    
    def __str__(self):
        return f"{self.name}, {self.city} ({self.state.name})"
