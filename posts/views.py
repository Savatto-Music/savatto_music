"""Posts views."""
#Django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

#Forms
from posts.forms import PostForm

#Models
from posts.models import Post

class PostDetailView(DetailView):
    """Return Detail posts"""

    template_name = 'profile.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(CreateView):
    """Create a new post."""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context