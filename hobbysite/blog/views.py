from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, CommentForm
from user_management.models import Profile


class BlogListView(ListView):
    model = Article
    template_name = "blog/blog_list.html"


class BlogDetailView(DetailView):
    model = Article
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        article = self.get_object()
        ctx['author_articles'] = Article.objects.filter(author=article.author).exclude(pk=article.pk)
        ctx['comment_form'] = CommentForm()
        ctx['comments'] = Comment.objects.filter(article=self.object).order_by('-created_on')
        return ctx
   
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = Profile.objects.get(user_id=self.request.user)
            comment.article = self.get_object() 
            comment.entry = form.cleaned_data.get('entry')
            comment.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context["form"] = form
            return self.render_to_response(context)
        
        
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:blog-list")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = ArticleCategory.objects.all()
        return ctx
    
    def form_valid(self, form):
        form.instance.author = self.request.user.profile 
        return super().form_valid(form)

    
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:blog-list")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = ArticleCategory.objects.all()
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user.profile 
        return super().form_valid(form)