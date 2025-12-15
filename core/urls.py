from django.urls import path
from .views import index,contact,elements,bloghome,blogsingle,about,search_box
app_name='core'
urlpatterns = [
    path('',index,name='index'),
    
    path('contact/',contact,name='contact'),
    
    path('elements/',elements,name='elements'),
    
    path('blog-home/',bloghome,name='blog-home'),
    
    path('blog-single/<int:pk>',blogsingle,name='blog-single'),
    
    path('about/',about,name='about'),
    
    path('blog-home/category/<str:cat_name>',bloghome,name='blog-category'),
    
    path('blog-home/author/<str:author_name>',bloghome,name='blog-author'),
    
    path('blog-home/search/',search_box,name='blog-search')
    
    


]