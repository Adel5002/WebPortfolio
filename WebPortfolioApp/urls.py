from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ListProjects, ProjectDetail

urlpatterns = [
    path('', ListProjects.as_view(), name='home'),
    path('project/<slug:proj_slug>/', ProjectDetail.as_view(), name='project'),
]


urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

