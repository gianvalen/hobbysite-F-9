from django.urls import path, include
from .views import ProfileUpdateView

urlpatterns = [
    path('', ProfileUpdateView.as_view(), name = 'profile-update'),
    path('accounts/', include("django.contrib.auth.urls"), name = 'profile-accounts'),
]

app_name = 'user_management'    