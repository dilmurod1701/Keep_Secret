from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignUp


# Create your views here.
class Login(LoginView):
    template_name = 'users/login.html'
    next_page = 'question'


class Logout(LogoutView):
    next_page = 'login'
