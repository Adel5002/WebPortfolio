from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ListProjects, ProjectDetail, RegisterUser, LoginUser, logout_user, like_view, AddComment, \
    EditComment, DeleteComment

urlpatterns = [
    path('', ListProjects.as_view(), name='home'),
    path('project/<slug:proj_slug>/', ProjectDetail.as_view(), name='project'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('project/<slug:proj_slug>/like', like_view, name='like_project'),
    path('project/<slug:proj_slug>/add_comment/', AddComment.as_view(), name='add_comment'),
    path('project/comment/<int:pk>/delete', DeleteComment.as_view(), name='delete_comment'),
    path('project/comment/<int:pk>/edit', EditComment.as_view(), name='edit_comment'),
]


urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

