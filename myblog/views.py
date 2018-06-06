# coding:utf8

from django.shortcuts import render
from . import models

# 显示已存在的文章标题
def index(request):
    arts = models.Article.objects.all()
    return render(request, 'blog/index.html',{'articles':arts})

# 修改文章内容呈现
def showed(request):
    arts = models.Article.objects.all()
    return render(request, 'blog/showed.html', {'articles':arts})


# 添加和修改文章
def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/add_page.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'blog/change_page.html', {'article': article})

# 添加和修改动作的实现
def edit_action(requset):
    title=requset.POST.get('title', 'TITLE')
    content=requset.POST.get('content', 'CONTENT')
    article_id=requset.POST.get('article_id', '0')
    if article_id=='0':
        models.Article.objects.create(title=title, content=content)
        arts = models.Article.objects.all()
        return render(requset,'blog/index.html', {'articles':arts})
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title=title
        article.content=content
        article.save()
        return render(requset, 'blog/showed.html', {'article': article})





