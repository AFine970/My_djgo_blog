# coding:utf8
from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'time')
    list_filter = ('time',) #过滤器

admin.site.register(Article, ArticleAdmin)
