from django.shortcuts import render_to_response, get_object_or_404
from .models import Article
from .models import ArticleCate


def article_list(request):
    context = dict()
    context['articleList'] = Article.objects.all()
    context['articleCount'] = Article.objects.all().count()
    return render_to_response('article_list.html', context)


def article_detail(request, article_pk):
    context = dict()
    context['articleDetail'] = get_object_or_404(Article, id=article_pk)
    return render_to_response('article_detail.html', context)


def articles_by_cate(request, article_cate_pk):
    context = dict()
    article_type = get_object_or_404(ArticleCate, id=article_cate_pk)
    context['articlesByCate'] = Article.objects.filter(article_cate=article_type)
    context['articleCate'] = article_type
    return render_to_response('articles_by_cate.html', context)

