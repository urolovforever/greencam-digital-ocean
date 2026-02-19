from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Contact form for user submissions"""

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'contact-input',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+998 90 123-45-67',
                'class': 'contact-input',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'What is this about?',
                'class': 'contact-input',
            }),
            'message': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Your message...',
                'class': 'contact-input',
            }),
        }
        labels = {
            'name': 'Name',
            'phone': 'Phone Number',
            'subject': 'Subject',
            'message': 'Message',
        }
