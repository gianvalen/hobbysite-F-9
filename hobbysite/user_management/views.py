from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Profile

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = "registration/profile_update.html"

    def get_success_url (self):
        return reverse_lazy("wiki:articles") # MAKE SURE TO CHANGE SUCCESS URL