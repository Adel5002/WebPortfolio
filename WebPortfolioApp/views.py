from django.shortcuts import render
from django.views.generic import ListView

from .models import PortfolioStructure


class ListProjects(ListView):
    paginate_by = 3
    model = PortfolioStructure
    template_name = 'WebPortfolioApp/index.html'
    context_object_name = 'projects'


