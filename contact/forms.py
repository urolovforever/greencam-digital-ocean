from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Contact form for user submissions"""

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'contact-input',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your.email@example.com',
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
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
        }
