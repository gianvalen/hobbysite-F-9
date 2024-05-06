from django.urls import path
from .views import BlogListView, BlogDetailView,  ArticleCreateView, ArticleUpdateView

app_name = "blog"

urlpatterns = [
    path('articles/', BlogListView.as_view(), name='blog-list'),
    path('article/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('article/add', ArticleCreateView.as_view(), name = 'blog-create'),
    path('article/<int:pk>/edit', ArticleUpdateView.as_view(), name = 'blog-edit'),
]