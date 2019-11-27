import markdown
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CharField, TextField
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags


class Category(models.Model):
    """
    文章类别
    """
    name = CharField('类别名称', max_length=100)

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签类别
    """
    tag_name = CharField('标签名', max_length=100)

    class Meta:
        verbose_name = '博客标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    """
    文章
    """
    title = CharField('标题', max_length=100)
    content = TextField('内容')
    excerpt = models.CharField('文章摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章所属分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='文章所属标签')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='文章作者')
    created_time = models.DateTimeField('创建时间', default=timezone.now())
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('myblog:detail', kwargs={'pk': self.pk})

    def save(self,*args, **kwargs):
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])

        self.excerpt = strip_tags(md.convert(self.content))[:50]
        super().save(*args, **kwargs)
