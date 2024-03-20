from django.views.generic import DetailView, ListView
from .models import Article

class BlogListView(ListView):
    model = Article
    template_name = "blog_list.html"

class BlogDetailView(DetailView):
    model = Article
    template_name = "blog_detail.html"
