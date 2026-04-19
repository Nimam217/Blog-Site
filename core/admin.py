from django.contrib import admin
from .models import Post,Category,Contact,NewsLetter
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    date_hierarchy = 'created_date'
    fields=['title','author','status','content','category','counted_views']
    list_display=[
        'title','author','created_date','published_date',
        'update_date','status','counted_views','image'
                  ]
    ordering=['-created_date']
    search_fields=['title','author']
    list_filter=['status']

admin.site.register(Category)

admin.site.register(NewsLetter)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')
    ordering=['created_date']