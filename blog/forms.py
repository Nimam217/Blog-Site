from django import forms
from django.forms import ModelForm
from .models import Comment
from captcha.fields import CaptchaField

        
class CommentForm(ModelForm):
     captcha = CaptchaField()
     class Meta:
         model=Comment
         fields=['post','name','subject','email','message']