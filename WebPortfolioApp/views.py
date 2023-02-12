from django.shortcuts import render
from django.views.generic import ListView, DetailView

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


