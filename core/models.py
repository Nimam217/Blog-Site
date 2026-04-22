from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    image=models.ImageField(upload_to='img/upload',default='img/o3.jpg')
    title=models.CharField(max_length=50)
    published_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    #tag
    category=models.ManyToManyField(Category)
    #comments
    content=models.TextField(null=True)
    status=models.BooleanField(default=False)
    counted_views=models.IntegerField(default=0)
    
    
    
    class Meta:
      ordering=['published_date']
    
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        try:
            old_instance = Post.objects.get(pk=self.pk)
        except ObjectDoesNotExist:
            old_instance = None

        if (old_instance is None or not old_instance.status) and self.status:
            if not self.published_date: 
                self.published_date = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:blog-single", kwargs={"pk": self.pk})
    
    
    
class NewsLetter(models.Model):
    email=models.EmailField()
    
    def __str__(self):
        return self.email