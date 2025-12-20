from django.shortcuts import render
# Create your views here.

def index (request):
    return render(request,'Mysite/index.html')  
      
      
def about(request):
    return render(request,'Mysite/about.html')


def contact(request):
    return render(request,'Mysite/contact.html')

def elements(request):
    return render(request,'Mysite/elements.html')



