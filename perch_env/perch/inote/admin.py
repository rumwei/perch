from django.contrib import admin
from .models import ArticleCate, Article


@admin.register(ArticleCate)
class ArticleCateAdmin(admin.ModelAdmin):
    list_display = ('id', 'cate_name')
    ordering = ('id', 'cate_name')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'last_update_time')
    ordering = ('id', )

