from django.urls import path
from .views import ProfileUpdate

urlpatterns = [
    path('', ProfileUpdate.as_view(), name = 'profile-update')
]

app_name = 'profile'