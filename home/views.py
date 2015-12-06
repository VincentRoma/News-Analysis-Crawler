from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from post.models import Post
from news.models import News

def HomeViews(request):
    slider_posts = Post.objects.filter(slider=True)
    posts = Post.objects.all()[:20]

    ## Get Statistics ##
    nb_news = News.objects.all().count()
    nb_posts = Post.objects.all().count()
    nb_refugee = News.objects.filter(title__contains="refugee").count()
    nb_terror = News.objects.filter(Q(title__contains="ISIS") | Q(title__contains="Daesh") | Q(title__contains="terror")).count()

    return render(request, 'blog/home.html', {
        'posts': posts,
        'slider_posts': slider_posts,
        'state': 'home',
        'nb_refugee': nb_refugee,
        'nb_terror': nb_terror,
        'nb_posts': nb_posts,
        'nb_news': nb_news
    })
