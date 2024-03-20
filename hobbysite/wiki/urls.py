from django.urls import path
from .views import ArticleList, ArticleDetail

urlpatterns = [
    path('articles', ArticleList.as_view(), name = 'articles'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name = 'article'),
]

app_name = 'wiki'