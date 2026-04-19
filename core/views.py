from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm,NewsLetterForm
from .models import Contact
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def index (request):
    return render(request,'Mysite/index.html')  
      
      
def about(request):
    return render(request,'Mysite/about.html')


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
        
    
    return render(request,'Mysite/contact.html')

def elements(request):
    return render(request,'Mysite/elements.html')


def newsletter(request):
    
    if request.method=='POST':
        form=NewsLetterForm(request.POST)
        
        if form.is_valid(): 
            form.save()
            messages.success(request,'you sent a newsletter.')
            
            return redirect(reverse('core:index'))
            

    else:
         messages.error(request,"the newsletter didn't send.")
         return redirect(reverse('core:index'))
     
    return render(request,'base.html')

   
