from django.contrib import admin
from .models import Post,Category,NewsLetter
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    empty_value_display = '-empty-'
    date_hierarchy = 'created_date'
    fields=['image','title','author','status','login_require','content','category','counted_views','tags']
    list_display=[
        'title','author','created_date','published_date',
        'update_date','status','counted_views','image'
                  ]
    summernote_fields = ('content',)
    ordering=['-created_date']
    search_fields=['title','author']
    list_filter=['status']

    
admin.site.register(Post,PostAdmin)

admin.site.register(Category)

admin.site.register(NewsLetter)


