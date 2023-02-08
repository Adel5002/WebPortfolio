from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ListProjects

urlpatterns = [
    path('', ListProjects.as_view(), name='home')
]


urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

