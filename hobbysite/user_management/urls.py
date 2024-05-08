from django.urls import path, include
from django.contrib.auth.views import LoginView

from .views import ProfileUpdateView, dashboard

urlpatterns = [
    path('', ProfileUpdateView.as_view(), name = 'profile-update'),
    path('', dashboard, name = 'dashboard'),
]

app_name = 'user_management'    