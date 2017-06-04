from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.response import Response
from rest_framework import viewsets
from news.models import News


# ViewSets define the view behavior.
class ExploreViewSet(viewsets.ViewSet):
    def get_queryset(self):
        return self.request.user.accounts.all()
        
    def get(self, request):
        news = {"count": News.objects.count()}
        return Response(news)
