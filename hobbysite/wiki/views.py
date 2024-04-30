from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from profileapp.models import Profile

from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, CommentForm


class ArticleList(ListView):
    model = ArticleCategory
    context_object_name = "articles"
    template_name = "onlinewiki/wiki_list.html"


class ArticleDetail(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "onlinewiki/wiki_detail.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["comments"] = Comment.objects.all()
        ctx["form"] = CommentForm()
        return ctx

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.author = Profile.objects.get(user_id = self.request.user)
            comment.article = self.object
            comment.entry = form.cleaned_data.get('entry')
            comment.save()
            return self.get(request, *args, **kwargs)
        else: 
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context["form"] = form 
            return self.render_to_response(context)


class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "onlinewiki/wiki_form.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = ArticleCategory.objects.all()
        return ctx
    
    def post(self, request, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():

            form.instance.author = Profile.objects.get(user_id = self.request.user)
            return self.form_valid(form)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context["form"] = form 
            return self.render_to_response(context)

    def get_success_url(self):
        return reverse_lazy("wiki:articles")


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = ""

    template_name = "onlinewiki/wiki_form.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = ArticleCategory.objects.all()
        ctx["form"] = ArticleForm()
        return ctx
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article()
            article.title = form.cleaned_data.get('title')
            article.author = Profile.objects.get(user_id = self.request.user)
            article.entry = form.cleaned_data.get('entry')
            article.header_image = form.cleaned_data.get('header_image')
            article.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context["form"] = form 
            return self.render_to_response(context)
    def get_success_url(self):
        return reverse_lazy("wiki:articles")