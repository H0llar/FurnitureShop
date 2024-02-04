from django.views.generic import TemplateView

from shop.models import Product, Category


class HomeView(TemplateView):
    template_name = 'pages/home.html'
    extra_context = {
        'title': 'Главная',
        'top_banner_products': Product.objects.order_by('?').all()[:3],
        'bottom_banner_products': Product.objects.order_by('?').all()[:3],
        'categories': {category: Product.objects.order_by('?').filter(category=category)[:10]
                       for category in Category.objects.all()}
    }
