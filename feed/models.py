from django.db import models
from news.models import News
import feedparser
import re

class Feed(models.Model):
    title = models.CharField(max_length=500)
    url = models.CharField(max_length=1000)
    region = models.CharField(max_length=4, null=False, default="EN")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
       return 'RSS: ' + self.title

    @staticmethod
    def fetch_rss_news():
        publications = []
        feeds = Feed.objects.all()
        for feed in feeds:
            rss = feedparser.parse(feed.url)
            for entry in rss.entries:
                se = re.search(ur'^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)', entry.link)
                if se:
                    entry.domain = se.group(1)
                news, created = News.objects.get_or_create(title=entry.title,
                    description=entry.link,
                    news_type="rss",
                    region=feed.region,
                    domain=entry.domain)
