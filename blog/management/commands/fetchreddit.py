from django.core.management.base import BaseCommand
from news.models import News
from feed.models import Feed


class Command(BaseCommand):
    help = 'Fetch News from reddit'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        News.fetch_reddit_news('worldnews')
        News.fetch_reddit_news('news')
        News.fetch_reddit_news('RefugeeCrisis')
        News.fetch_reddit_news('migrantsituation')
        Feed.fetch_rss_news()
