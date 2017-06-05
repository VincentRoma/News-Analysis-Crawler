from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
import re

class News( models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    domain = models.CharField(max_length=100, null=False, default="unkown")
    news_type = models.CharField(max_length=500, default="worldnews")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    has_been_fetched = models.BooleanField(default=False)
    source = models.CharField(max_length=500, null=True)
    region = models.CharField(max_length=4, null=False, default="EN")

    def __unicode__(self):
       return 'News: ' + self.title

    @staticmethod
    def fetch_reddit_news(channel, region):
        import praw
        r = praw.Reddit(user_agent='homeAPI')
        submissions = r.get_subreddit(channel).get_hot(limit=100)
        for x in submissions:
            news, created = News.objects.get_or_create(description=x.url, region=region)
            if created:
                news.title = x.title
                news.news_type = channel
                news.save()

    @staticmethod
    def delete_duplicated_news():
        count = 0
        # for x in submissions:
        # News.objects.get_or_create(description=x.url)
        for news in News.objects.all():
            if news.description in News.objects.exclude(id=news.id).values_list('description', flat=True):
                news.delete()
                count = count + 1
        print "{} duplicated news deleted".format(count)

    @staticmethod
    def time_aggregation(format_date):
        results = {}
        news = News.objects.all()
        for item in news:
            date = item.created_at.strftime(format_date)
            if date in results.keys():
                results[date] = results[date] + 1
            else:
                results[date] = 1
        return results

    @staticmethod
    def domain_aggregation():
        import re
        domains = []
        results = {}
        news = News.objects.all()
        for n in news:
            se = re.search(ur'^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)', n.description)
            if se:
                domains.append(se.group(1))
        for item in domains:
            if item in results.keys():
                results[item] = results[item] + 1
            else:
                results[item] = 1
        return results


    @receiver(pre_save)
    def my_callback(sender, instance, *args, **kwargs):
        se = re.search(ur'^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)', instance.description)
        if se:
            instance.domain = se.group(1)

    # def domain_time_aggregation():
    #     by_dates = {}
    #     results = {}
    #     news = News.objects.all()
    #     for n in news:
    #         se = re.search(ur'^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n]+)', n.description)
    #         if se:
    #             if se.group(1) in by_dates.keys():
    #                  by_dates[se.group(1)] = by_dates[se.group(1)]
    #             domains.append(se.group(1))
    #     for item in domains:
    #         if item in results.keys():
    #             results[item] = results[item] + 1
    #         else:
    #             results[item] = 1

class CoreNews(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=10000)

    def __unicode__(self):
       return 'Core: ' + self.title
