from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse
from core.models import Post # pyright: ignore[reportMissingImports]
from .models import Comment
from django.core.paginator import Paginator
from .forms import CommentForm
from django.contrib import messages
from django.db.models import F
# Create your views here.


def bloghome(request,**kwargs):
    posts = Post.objects.filter(
    status=1
    ).select_related(
        'author'
    ).prefetch_related(
        'category',
        'tags'
    )
        
    if kwargs.get('cat_name') is not None:
        posts=posts.filter(category__name=kwargs['cat_name'])
        
    if kwargs.get('author_name') is not None:
        posts=posts.filter(author__username=kwargs['author_name'])

    if kwargs.get('tag_name') is not None:
        posts=posts.filter(tags__name__in=[kwargs['tag_name']])   
    
    paginator = Paginator(posts,3) 

    page_number = request.GET.get("page")
    posts = paginator.get_page(page_number)
    
    return render(request,'Blog/blog-home.html',context={'posts':posts})



def blogsingle(request, pk):

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'you sent a comment.')
        else:
            messages.error(request, "the comment didn't send.")

    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pk)

    if post.login_require and not request.user.is_authenticated:
        return redirect(reverse('accounts:login'))

    Post.objects.filter(pk=post.pk).update(
        counted_views=F('counted_views') + 1
    )

    post.refresh_from_db()

    prv_post = Post.objects.filter(
        created_date__lt=post.created_date,
        status=1
    ).order_by("-created_date").first()

    nxt_post = Post.objects.filter(
        created_date__gt=post.created_date,
        status=1
    ).order_by("created_date").first()

    comments = Comment.objects.filter(
        post=post.pk,
        approved=True
    )

    form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
        'prv_post': prv_post,
        'nxt_post': nxt_post,
    }

    return render(
        request,
        'Blog/blog-single.html',
        context=context
    )


def search_box(request):
    posts=Post.objects.filter(status=1)
    if request.method =='GET':
        if s:= request.GET.get('s'):
           posts= posts.filter(title__contains=s)
    context={'posts':posts}
    
    return render(request,'Blog/blog-home.html',context)