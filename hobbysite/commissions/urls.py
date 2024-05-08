from django.urls import path

from .views import CommissionDetailView, CommissionUpdateView, CommissionCreateView, commission_list

urlpatterns = [
    path('list', commission_list, name= 'commission-list'), 
    path('detail/<int:pk>', CommissionDetailView.as_view(), name= 'commission-detail'),
    path('add', CommissionCreateView.as_view(), name= 'commission-create'),
    path('<int:pk>/edit', CommissionUpdateView.as_view(), name= 'commission-update'),
]

app_name = 'commissions'