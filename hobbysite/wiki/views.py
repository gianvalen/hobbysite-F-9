from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Article, ArticleCategory
from .forms import ArticleForm, CommentForm

class ArticleList(ListView):
    model = ArticleCategory
    context_object_name = "articles"
    template_name = "onlinewiki/wiki_list.html"


class ArticleDetail(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "onlinewiki/wiki_detail.html"

class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    form_class = 
    template_name = ""

    def get_success_url(self):
        return reverse_lazy("wiki:articles")

class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = 
    template_name = ""

    def get_success_url(self):
        return reverse_lazy("wiki:articles")