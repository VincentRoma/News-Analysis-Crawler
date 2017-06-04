from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from news.views import NewsViewSet as news_viesset
from explore.views import ExploreViewSet as explore_viesset

router = routers.DefaultRouter()
router.register(r'news', news_viesset)
router.register(r'explore', explore_viesset, 'Explore')

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    # url(r'^$', home_views, name='home'),
)
