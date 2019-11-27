from django import template
from ..models import Article, Category, Tag

register = template.Library()


@register.inclusion_tag('myblog/inclusions/_recent_articles.html', takes_context=True)
def show_recent_articles(context, num=5):
    return {'recent_article_list': Article.objects.all().order_by('-update_time')[:num]}


@register.inclusion_tag('myblog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Article.objects.dates('created_time', 'month', order='DESC'),
    }


@register.inclusion_tag('myblog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    category_list = Category.objects.all()
    return {
        'category_list': category_list,
        'length': len(category_list)
    }


@register.inclusion_tag('myblog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }