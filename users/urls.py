"""Users Urls"""

#Django
from django.urls import path


# Views
from users import views

urlpatterns = [
    path(
        route='',
        view=views.UserHomeView.as_view(),
        name='home'
    ),

    path(
        route='garage',
        view=views.UserGarageView.as_view(),
        name='garage'
    ),

    # Management
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),

    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),

    path(
        route='signup/band',
        view=views.Band_signupView.as_view(),
        name='Bandsignup'
    ),

    path(
        route='me/profile',
        view=views.UpdateProfileView.as_view(),
        name='update_profile'
    ),
    
    # Posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail',
    ),

]