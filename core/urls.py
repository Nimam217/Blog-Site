from django.urls import path
from .views import index,elements,about,newsletter
app_name='core'
urlpatterns = [
    path('',index,name='index'),
    
    path('elements/',elements,name='elements'),

    path('about/',about,name='about'),
    
    path('newsletter/',newsletter,name='newsletter')
    
   

]