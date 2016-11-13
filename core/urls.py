from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from news.views import NewsViews as news_views
from news.views import NewsViewSet as news_viesset
from explore.views import ExploreViews as explore_views

router = routers.DefaultRouter()
router.register(r'news', news_viesset)

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', news_views, name='news'),
    url(r'^explore/', explore_views, name='explore'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    # url(r'^$', home_views, name='home'),
)
