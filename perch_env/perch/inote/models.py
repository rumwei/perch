from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ArticleCate(models.Model):
    cate_name = models.CharField(max_length=15)

    def __str__(self):
        return self.cate_name


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)  # 表示Article删除时，不删除对应的作者
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    article_cate = models.ManyToManyField(ArticleCate)

    def __str__(self):
        return "Article: %s" % self.title




