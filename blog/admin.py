from django.contrib import admin 
from .models import Comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    date_hierarchy = 'created_date'
    fields=['post','name','subject','email'
            ,'message','approved'
        ]
    list_display=[
        'post','name','subject','email'
            ,'created_date','approved'
                  ]
    ordering=['-created_date']
    search_fields=['email','name','post']
    list_filter=['approved']
    
    
    
    




admin.site.register(Comment,CommentAdmin)