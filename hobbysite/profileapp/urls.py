from django.urls import path, include
from .views import ProfileUpdate

urlpatterns = [
    path('', ProfileUpdate.as_view(), name = 'profile-update'),
    path('accounts/', include("django.contrib.auth.urls"), name = 'profile-accounts')
]

app_name = 'profileapp'