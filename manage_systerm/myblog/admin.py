from django.contrib import admin

# Register your models here.
from .models import Article, Category, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'update_time', 'category', 'author']
    fields = ['title', 'content', 'excerpt', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)