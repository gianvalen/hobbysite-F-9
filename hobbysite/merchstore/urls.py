from django.urls import path
from .views import MerchListView, MerchDetailView, MerchCreateView, MerchUpdateView, MerchCartView, MerchTransactionView

urlpatterns = [
    path('cart/', MerchCartView.as_view(), name='cart'),
    path('transactions', MerchTransactionView.as_view(), name='transaction'),
    path('items/', MerchListView.as_view(), name='items'),
    path('item/<int:pk>/', MerchDetailView.as_view(), name='item'),
    path('item/<int:pk>/edit', MerchUpdateView.as_view(), name='update'),
    path('item/add', MerchCreateView.as_view(), name='add'),
]

app_name = 'merchstore'