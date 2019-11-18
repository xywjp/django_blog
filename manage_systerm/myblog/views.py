import re

import markdown
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension

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
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        TocExtension(slugify=slugify),
        'markdown.extensions.toc',
        ])

    article.content = md.convert(article.content)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    article.toc = m.group(1) if m is not None else ''
    return render(request, 'myblog/detail.html', context={'article': article})
