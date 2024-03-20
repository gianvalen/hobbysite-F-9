from django.urls import path
from .views import MerchListView, MerchDetailView

urlpatterns = [
    path('items/', MerchListView.as_view(), name='items'),
    path('item/<int:pk>/', MerchDetailView.as_view(), name='item'),
]

app_name = 'merchstore'