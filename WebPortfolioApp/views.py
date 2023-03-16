from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse

from .forms import RegisterUserForm, LoginUserForm, CommentForm
from .models import PortfolioStructure, Comment


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

    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data()


        stuff = get_object_or_404(PortfolioStructure, slug=self.kwargs['proj_slug'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True


        context['total_likes'] = total_likes
        context['liked'] = liked
        return context



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'WebPortfolioApp/register_popup.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'WebPortfolioApp/login_popup.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def like_view(request, proj_slug):
    project = get_object_or_404(PortfolioStructure, id=request.POST.get('project_id'))
    liked = False
    if project.likes.filter(id=request.user.id).exists():
        project.likes.remove(request.user)
        liked = False
    else:
        project.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('project', args=[str(proj_slug)]))


class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'WebPortfolioApp/add_comment.html'

    def form_valid(self, form):
        form.instance.project = PortfolioStructure.objects.get(slug=self.kwargs['proj_slug'])
        comments = form.save(commit=False)
        comments.commentator = self.request.user
        comments.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project', kwargs={'proj_slug': self.object.project.slug})


class EditComment(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'WebPortfolioApp/edit_comment.html'



    def get_success_url(self):
        return reverse('project', kwargs={'proj_slug': self.object.project.slug})


class DeleteComment(DeleteView):
    model = Comment
    template_name = 'WebPortfolioApp/delete_comment.html'



    def get_success_url(self):
        return reverse('project', kwargs={'proj_slug': self.object.project.slug})

