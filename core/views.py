from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import NewsLetterForm
from django.contrib import messages
# Create your views here.

def index (request):
    return render(request,'Mysite/index.html')  
      
      
def about(request):
    return render(request,'Mysite/about.html')

        


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

   
