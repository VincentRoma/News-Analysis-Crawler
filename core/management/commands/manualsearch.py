from django.core.management.base import BaseCommand
from news.models import News
from feed.models import Feed


class Command(BaseCommand):
    help = 'Explore ES'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        import pdb; pdb.set_trace()
