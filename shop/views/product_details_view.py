from django.urls import reverse_lazy
from django.views.generic import DetailView

from shop.models import Product


class ProductDetail(DetailView):
    template_name = 'pages/product-details.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object_name = self.object.name
        context['title'] = object_name
        context['breadcrumbs'] = {
            'Главная': reverse_lazy('home'),
            f'{object_name}': ''
        }
        return context
