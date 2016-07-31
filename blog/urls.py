from django.conf.urls import patterns, include, url
from django.contrib import admin
from post.views import PostViews as post_views
from home.views import HomeViews as home_views
from news.views import NewsViews as news_views
from explore.views import ExploreViews as explore_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^posts/', post_views, name='post'),
    url(r'^news/', news_views, name='news'),
    url(r'^explore/', explore_views, name='explore'),
    url(r'^$', home_views, name='home'),
)
