"""Posts Urls"""

#Django
from django.urls import path

# Views
from posts import views

urlpatterns = [

    path(
        route='post/new/',
        view=views.CreatePostView.as_view(),
        name='create'
    ),

    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='profile'
    ),

]