from django.db import models


class News(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
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


class CoreNews(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=10000)

    def __unicode__(self):
       return 'Core: ' + self.title
