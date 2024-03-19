from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article, ArticleCategory

class ArticleList(ListView):
    model = ArticleCategory
    context_object_name = "articles"
    template_name = "onlinewiki/wiki_list.html"


class ArticleDetail(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "onlinewiki/wiki_detail.html"