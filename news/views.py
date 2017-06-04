from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import list_route
from rest_framework.response import Response
from .models import News
import re

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

    @list_route()
    def count(self, request):
        news = {"count": News.objects.count()}
        return Response(news)

    @list_route()
    def sources(self, request):
        domains = []
        results = {}
        news = News.objects.all()
        for n in news:
            se = re.search(ur'^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)', n.description)
            if se:
                domains.append(se.group(1))
        for item in domains:
            if item in results.keys():
                results[item] = results[item] + 1
            else:
                results[item] = 1
        return Response(results)
