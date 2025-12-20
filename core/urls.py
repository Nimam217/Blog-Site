from django.urls import path
from .views import index,contact,elements,about
app_name='core'
urlpatterns = [
    path('',index,name='index'),
    
    path('contact/',contact,name='contact'),
    
    path('elements/',elements,name='elements'),

    path('about/',about,name='about'),
    
   

]