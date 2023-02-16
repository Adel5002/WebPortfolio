from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ListProjects, ProjectDetail, RegisterUser, LoginUser

urlpatterns = [
    path('', ListProjects.as_view(), name='home'),
    path('project/<slug:proj_slug>/', ProjectDetail.as_view(), name='project'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
]


urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

