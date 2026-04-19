from django import forms
from django.forms import ModelForm
from .models import Contact,NewsLetter


class ContactForm(ModelForm):
     class Meta:
         model=Contact
         fields='__all__'
         


class NewsLetterForm(ModelForm):
     class Meta:
         model=NewsLetter
         fields='__all__'
         