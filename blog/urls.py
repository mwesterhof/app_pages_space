from django.urls import path

from .views import ArticleDetail, ArticleList, CreateArticleView


urlpatterns = [
    path('articles/', ArticleList.as_view(), name='article_list'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('articles/new/', CreateArticleView.as_view(), name='article_new'),
]
