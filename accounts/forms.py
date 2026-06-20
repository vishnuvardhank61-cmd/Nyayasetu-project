from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import CustomUser


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(
        required=True,
        help_text='Required. Enter a valid email address.',
        error_messages={'invalid': 'Invalid email.'}
    )
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        help_text='Format: +91XXXXXXXXXX or 10 digits'
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter your address', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+91XXXXXXXXXX', 'class': 'form-control'}),
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'citizen'
        
        # Explicitly save the custom fields
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        user.email = self.cleaned_data.get('email', '')
        user.phone_number = self.cleaned_data.get('phone_number', '')
        user.address = self.cleaned_data.get('address', '')
        
        if commit:
            user.save()
        return user
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError('Username must be at least 3 characters long.')
        return username

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            # Strip non-digit characters to check length
            import re
            digits = re.sub(r'\D', '', phone_number)
            if len(digits) != 10:
                raise forms.ValidationError('Phone number must be exactly 10 digits long.')
        return phone_number


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username or Email')
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if not username or not password:
            raise forms.ValidationError("Username and password are required.")

        # Try authenticate with username first, then email
        user = authenticate(username=username, password=password)
        if not user:
            # Try with email
            try:
                user_obj = CustomUser.objects.get(email=username)
                user = authenticate(username=user_obj.username, password=password)
            except CustomUser.DoesNotExist:
                pass

        if not user:
            raise forms.ValidationError("Invalid username/email or password.")

        self.user = user
        return cleaned_data


class ProfileForm(forms.ModelForm):
    """Form for updating user profile information"""
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+91 XXXXXXXXXX', 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Address', 'class': 'form-control'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('This email is already in use.')
        return email