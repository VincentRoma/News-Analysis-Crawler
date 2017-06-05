from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import list_route
from rest_framework.response import Response
from .models import News

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
        results = News.domain_aggregation()
        return Response(results)

    @list_route()
    def minutes(self, request):
        results = News.time_aggregation("%Y-%m-%d %H:%M:00")
        return Response(results)

    @list_route()
    def hours(self, request):
        results = News.time_aggregation("%Y-%m-%d %H:00:00")
        return Response(results)

    @list_route()
    def days(self, request):
        results = News.time_aggregation("%Y-%m-%d 00:00:00")
        return Response(results)

    @list_route()
    def sources_time(self, request):
        domains = []
        results = {}
        news = News.objects.raw('SELECT id, domain, created_at, COUNT(*) AS nb_article FROM news_news GROUP BY domain, created_at;')
        import pdb; pdb.set_trace()
        return Response(news)
