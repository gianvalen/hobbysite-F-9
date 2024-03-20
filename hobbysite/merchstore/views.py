from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import ProductType, Product


class MerchListView(ListView):
    model = Product
    template_name = 'merch-store/merchstore_list.html'
    context_object_name = 'items'


class MerchDetailView(DetailView):
    model = Product
    template_name = 'merch-store/merchstore_detail.html'
    context_object_name = 'item'