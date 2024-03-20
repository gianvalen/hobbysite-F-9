from django.urls import path
from .views import BlogListView, BlogDetailView

app_name = "blog"

urlpatterns = [
    path('articles/', BlogListView.as_view(), name='blog-list'),
    path('article/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
]
