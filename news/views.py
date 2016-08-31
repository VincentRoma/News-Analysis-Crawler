from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import News

def NewsViews(request):
    news_all = News.objects.all().order_by('-created_at')
    paginator = Paginator(news_all, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)

    return render(request, 'news/news.html', {'news': news, 'state': 'news'})

from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'created_at')

# ViewSets define the view behavior.
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
