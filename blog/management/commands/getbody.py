from django.core.management.base import BaseCommand
from news.models import News
from news.models import CoreNews
from blog import settings
import requests


class Command(BaseCommand):
    help = 'Fetch body for persisted news'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        crawler_url = settings.CRAWLER_URL
        news = News.objects.filter(has_been_fetched=False)
        for item in news.all():
            r = requests.get(crawler_url + item.description)
            result = r.json()
            if 'text' in result:
                #PERSIST MAGUEULE
                CoreNews.objects.create(
                    title=item.title,
                    description=item.description,
                    text=result['text']
                )
                #HAS BEEN FETCH
                item.has_been_fetched = True
                item.save()
