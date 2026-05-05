from django.db import models 
from core.models import Post 
# Create your models here.

class Comment(models.Model):
    post =models.ForeignKey(Post,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    email=models.EmailField()
    message=models.TextField()
    created_date=models.DateTimeField(auto_now=True)
    updated_date=models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta: 
        ordering =['-created_date']
        
    def __str__(self):
        return self .name