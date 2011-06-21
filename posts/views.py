# Create your views here.
from django.http import HttpResponse
from posts.models import Post
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from posts import settings

def blog_info_processor(request):
    ctx = {
           'BLOG_TITLE': settings.BLOG_TITLE,
           'BLOG_SLOGAN': settings.BLOG_SLOGAN,
    }
    return ctx

def post_list(request):
    posts = get_list_or_404(Post)
    for post in posts:
        post.digest = post.content[:200]
    ctx = RequestContext(request, {
        'posts': posts,
    }, [blog_info_processor])
    return render_to_response('index.html', ctx)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    ctx = RequestContext(request, {
        'post': post
    }, [blog_info_processor])
    return render_to_response('index.html', ctx)