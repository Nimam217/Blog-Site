from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
# Create your views here.

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            contact=form.save(commit=False)
            contact.name='Unknown'
            contact.save()
            messages.success(request,'you sent a contact form.')
        else:
            messages.error(request,"the contact form didn't send.")
    else:
        
        form=ContactForm()
    return render(request,'Contact/contact.html')