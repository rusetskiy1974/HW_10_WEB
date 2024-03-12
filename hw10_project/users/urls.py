from django.urls import path
from django.contrib.auth.views import LoginView

from . import views
from .forms import LoginForm

app_name = "users"

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('signin/',
         LoginView.as_view(template_name="users/login.html", form_class=LoginForm, redirect_authenticated_user=True),
         name='signin'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
