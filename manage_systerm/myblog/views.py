from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Article


def index(request):
    """
    首页访问
    :return:
    """
    article_list = Article.objects.all()
    return render(request, 'myblog/index.html', context={
        'title': '我的博客首页',
        'content': 'welcome'
    })