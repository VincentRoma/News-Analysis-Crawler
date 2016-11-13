from django.core.management.base import BaseCommand
from news.models import News
from feed.models import Feed


class Command(BaseCommand):
    help = 'Crawl news articles from the registered sources'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        News.fetch_reddit_news('worldnews', 'EN')
        News.fetch_reddit_news('news', 'EN')
        News.fetch_reddit_news('RefugeeCrisis', 'EN')
        News.fetch_reddit_news('migrantsituation', 'EN')
        Feed.fetch_rss_news()
