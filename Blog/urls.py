
from django.urls import path
from .views import bloghome,blogsingle,search_box
app_name='blog'

urlpatterns = [
     path('',bloghome,name='blog-home'),
    
    path('blog-single/<int:pk>',blogsingle,name='blog-single'),
    
    path('category/<str:cat_name>',bloghome,name='blog-category'),
    path('tag/<str:tag_name>',bloghome,name='blog-tag'),
    path('author/<str:author_name>',bloghome,name='blog-author'),
    
    path('search/',search_box,name='blog-search')
]
