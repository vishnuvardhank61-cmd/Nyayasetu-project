from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError

class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('user_type', 'admin')
        return super().create_superuser(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    
    PHONE_REGEX = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message='Phone number must be 9-15 digits and may start with +.',
        code='invalid_phone'
    )
    
    phone_number = models.CharField(
        max_length=15,
        validators=[PHONE_REGEX],
        blank=True,
        help_text="Format: +91XXXXXXXXXX or 10 digits"
    )
    address = models.TextField(blank=True)
    
    USER_TYPE_CHOICES = (
        ('citizen', 'Citizen'),
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
    )

    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='citizen'
    )
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
        ordering = ['-date_joined']
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
            models.Index(fields=['user_type']),
        ]

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
    
    def clean(self):
        super().clean()
        if self.email:
            # Check email uniqueness
            if CustomUser.objects.filter(email=self.email).exclude(pk=self.pk).exists():
                raise ValidationError({'email': 'This email is already registered.'})