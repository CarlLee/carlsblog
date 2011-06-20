# Create your views here.
from django.http import HttpResponse
from posts.models import Post
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404

def index(request):
    posts = get_list_or_404(Post)
    return render_to_response('index.html', {'posts': posts})

def show_post(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render_to_response('show_post.html', {'post': post})

