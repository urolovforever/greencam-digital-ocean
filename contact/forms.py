from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': _('Your Name'),
                'class': 'contact-input',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your.email@example.com',
                'class': 'contact-input',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': _('What is this about?'),
                'class': 'contact-input',
            }),
            'message': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': _('Your message...'),
                'class': 'contact-input',
            }),
        }
        labels = {
            'name': _('Name'),
            'email': _('Email'),
            'subject': _('Subject'),
            'message': _('Message'),
        }
