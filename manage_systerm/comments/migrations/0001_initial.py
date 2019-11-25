# Generated by Django 2.2.3 on 2019-11-25 09:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myblog', '0003_auto_20191125_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名字')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('url', models.URLField(blank=True, verbose_name='网址')),
                ('text', models.TextField(verbose_name='内容')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Article', verbose_name='文章')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
