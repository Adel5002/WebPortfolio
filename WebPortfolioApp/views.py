from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import RegisterUserForm
from .models import PortfolioStructure


class ListProjects(ListView):
    paginate_by = 3
    model = PortfolioStructure
    template_name = 'WebPortfolioApp/index.html'
    context_object_name = 'projects'


class ProjectDetail(DetailView):
    model = PortfolioStructure
    template_name = 'WebPortfolioApp/details.html'
    slug_url_kwarg = 'proj_slug'
    context_object_name = 'project'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'WebPortfolioApp/register_popup.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'WebPortfolioApp/login_popup.html'

    def get_success_url(self):
        return reverse_lazy('home')