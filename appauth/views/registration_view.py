from django.urls import reverse_lazy
from django.views.generic import CreateView

from appauth.forms import RegistrationForm


class RegistrationView(CreateView):
    template_name = 'pages/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    extra_context = {
        'title': 'Регистрация',
        'breadcrumbs': {
            'Главная': reverse_lazy('home'),
            'Регистрация': ''
        }
    }
