from django import template
from core.models import Post,Category

register = template.Library()


@register.inclusion_tag('Blog/popular-posts.html')
def popularposts():
    posts=Post.objects.filter(status=1)
    posts=posts.order_by("-counted_views")[:3]
    return {'posts':posts}

@register.inclusion_tag('Blog/post-category.html')
def postcategory():
    posts=Post.objects.filter(status=1)
    category=Category.objects.all()
    cat_dict={}
    
    for name in category:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}

@register.inclusion_tag('Mysite/home-latest-posts.html')
def homelatest():
    posts=Post.objects.filter(status=1)
    posts=posts.order_by("published_date")[:6] 
    return {'posts':posts}