from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    url_picture = models.CharField(max_length=200, null=True, blank=True)
    url_link = models.CharField(max_length=200, null=True, blank=True)
    slider = models.BooleanField(default=False)
    picture = models.ImageField(null=True, blank=True)

    def __unicode__(self):
       return 'Post: ' + self.title
