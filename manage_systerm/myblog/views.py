from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Article


def index(request):
    """
    首页访问
    :return:
    """
    article_list = Article.objects.all().order_by('-created_time')
    return render(request, 'myblog/index.html', context={
       'article_list': article_list
    })


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'myblog/detail.html', context={'article': article})
