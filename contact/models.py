from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField()
    email=models.EmailField()
    subject=models.CharField(blank=True)
    message=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    upadate_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name