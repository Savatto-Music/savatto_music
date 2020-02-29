"""Users views"""

# Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView, ListView
from django.shortcuts import render



# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

# Forms
from users.forms import SignupForm

class UserGarageView(ListView):
    template_name = 'garage.html'
    model = User
    paginate_by = 8
    context_object_name = 'user'


class UserHomeView(ListView):
    template_name = 'home.html'
    model = User
    paginate_by = 5
    context_object_name = 'user'


class UserDetailView(DetailView):
    """User Detail view."""

    template_name = 'detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class SignupView(FormView):
    """Users signup."""

    template_name = 'sign.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Sava form data."""
        form.save()
        return super().form_valid(form)

class Band_signupView(FormView):
    """Users signup."""

    template_name = 'band_register.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Sava form data."""
        form.save()
        return super().form_valid(form)



class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'profile.html'
    model = Profile
    fields = [
        'name',
        'genre',
        'biography',
        'phone_number',
        'email',
        'namesong1',
        'namesong2',
        'namesong3',
        'urlsong1',
        'urlsong2',
        'urlsong3',
        'price']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class LoginView(auth_views.LoginView):
    """ Login View """

    template_name = 'sign.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout View."""
    template_name = 'logged_out.html'
