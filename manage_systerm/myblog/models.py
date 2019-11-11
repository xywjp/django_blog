from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CharField, TextField


class Category(models.Model):
    """
    文章类别
    """
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签类别
    """
    tag_name = CharField(max_length=100)

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    """
    文章
    """
    title = CharField(max_length=100)
    content = TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.title