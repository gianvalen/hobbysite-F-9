"""
URL configuration for hobbysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import HomePageView
from user_management.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('merchstore/', include('merchstore.urls', namespace='merchstore')),
    path('wiki/', include('wiki.urls', namespace = "wiki")),
    path('blog/',include('blog.urls', namespace='blog')),
    path('commissions/', include('commissions.urls', namespace='commissions')),
    path('profile/', include('user_management.urls', namespace = "user_management")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('home', HomePageView.as_view(), name='home'),
    path('dashboard', dashboard, name = "dashboard"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)