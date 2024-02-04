from django.contrib.auth import views
from django.urls import reverse_lazy

from appauth.forms import LoginForm


class LoginView(views.LoginView):
    template_name = 'pages/login.html'
    form_class = LoginForm
    extra_context = {
        'title': 'Авторизация',
        'breadcrumbs': {
            'Главная': reverse_lazy('home'),
            'Авторизация': ''
        }
    }
