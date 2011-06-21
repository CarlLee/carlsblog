# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from posts.models import Post
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from posts.forms import PostForm
from posts.models import Post
from posts.context import BlogInfoContext
import datetime

def post_list(request):
    posts = get_list_or_404(Post)
    for post in posts:
        post.digest = post.content[:200]
    ctx = BlogInfoContext(request, {
        'posts': posts,
    })
    return render_to_response('post_list.html', ctx)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    ctx = BlogInfoContext(request, {
        'post': post
    })
    return render_to_response('post_detail.html', ctx)

def post_publish(request):
    if(request.method == 'POST'):
        form = PostForm(request.POST)
        if(form.is_valid()):
            ctx = BlogInfoContext(request, {
                   'form': form
                })
            post = Post()
            post.content = form['content'].value()
            post.title = form['title'].value()
            post.published = datetime.datetime.now()
            post.save()
            return HttpResponseRedirect("/")
    else:
        form = PostForm()
    return render_to_response('post_create.html',{
                'form': form
            })

def post_create(request):
    form = PostForm()
    ctx = BlogInfoContext(request, {
           'form': form
        })
    return render_to_response('post_create.html', ctx)
