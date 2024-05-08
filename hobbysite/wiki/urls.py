from django.urls import path
from .views import ArticleList, ArticleDetail, ArticleCreate, ArticleUpdate

urlpatterns = [
    path('articles', ArticleList.as_view(), name = 'articles'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name = 'article'),
    path('article/add', ArticleCreate.as_view(), name = 'article-create'),
    path('article/<int:pk>/edit', ArticleUpdate.as_view(), name = 'article-edit'),
]

app_name = 'wiki'