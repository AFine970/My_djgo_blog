from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=32,default='Title')
    content=models.TextField(null=True)
    time=models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title