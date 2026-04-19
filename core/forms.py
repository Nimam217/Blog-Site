from django import forms
from django.forms import ModelForm
from .models import NewsLetter

        
class NewsLetterForm(ModelForm):
     class Meta:
         model=NewsLetter
         fields='__all__'
         