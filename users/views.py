from django.forms import forms
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
# Create your views here.

class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
