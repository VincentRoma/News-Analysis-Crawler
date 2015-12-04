from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from post.models import Post

def HomeViews(request):
    slider_posts = Post.objects.filter(slider=True)
    posts = Post.objects.filter(slider=False)
    return render(request, 'blog/home.html', {'posts': posts, 'slider_posts': slider_posts, 'state': 'home'})
