from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import LoginView, RegistrationView

app_name = 'appauth'

urlpatterns = [
    path("login/", LoginView.as_view(), name="auth"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
