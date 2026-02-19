from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):
    """Form for event registration"""

    class Meta:
        model = Registration
        fields = ['full_name', 'email', 'phone', 'note']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your full name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your email',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your phone number',
                'required': True
            }),
            'note': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Any additional notes (optional)',
                'rows': 4
            }),
        }
        labels = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'note': 'Additional Note',
        }

    def clean_phone(self):
        """Validate phone number"""
        phone = self.cleaned_data.get('phone')
        if phone and len(phone) < 9:
            raise forms.ValidationError("Please enter a valid phone number")
        return phone

    def clean_email(self):
        """Validate email format"""
        email = self.cleaned_data.get('email')
        if email:
            email = email.lower()
        return email
