from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, ListView
from django.urls import reverse_lazy
from .models import Profile

from commissions.models import Commission
from merchstore.models import Product
from wiki.models import Article as WikiArticle
from blog.models import Article as BlogArticle


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['display_name', 'email_address']
    template_name = "registration/profile_update.html"

    def get_success_url (self):
        return reverse_lazy("home")
    
    def get_object(self, queryset=None):
        return self.request.user.profile
    

@login_required
def dashboard(request):
    user = request.user
    ctx = {
        "commissions_created": Commission.objects.filter(author=user.profile),
        "commissions_applied_to": Commission.objects.filter(jobs__job_application__applicant=user.profile),
        # "products_bought": , 
        # "products_sold": ,
        # "wiki_articles_created": WikiArticle.objects.filter(author=user.profile), 
        # "blog_articles_created": BlogArticle.objects.filter(author=user.profile),
    }
    return render(request, "dashboard.html", ctx)