from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/article/id
    path('<int:article_pk>', views.article_detail, name='article_detail'),
    path('cate/<int:article_cate_pk>', views.articles_by_cate, name='articles_by_cate'),
]