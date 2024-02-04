from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView

from shop.models import Product, Category, Material, Brand


class CatalogView(ListView):
    model = Product
    template_name = 'pages/catalog.html'
    paginate_by = 20
    extra_context = {
        'title': 'Каталог',
        'breadcrumbs': {
            'Главная': reverse_lazy('home'),
            'Каталог': reverse_lazy('shop:catalog'),
        },
        'categories': Category.objects.all(),
        'materials': Material.objects.all(),
        'brands': Brand.objects.all(),
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        query_dict = self.request.GET.copy()

        if 'page' in query_dict:
            query_dict.pop('page')

        context['queries'] = query_dict.urlencode()

        context['min_price'] = self.request.GET.getlist('material', [])
        context['max_price'] = self.request.GET.get('max_price', 0)

        context['apply_materials'] = self.request.GET.getlist('material', [])
        context['apply_categories'] = self.request.GET.getlist('category', [])
        context['apply_brands'] = self.request.GET.getlist('brand', [])

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        min_price_query = self.request.GET.get('min_price', 0)
        min_price = 0 if min_price_query == '' else int(min_price_query)

        max_price_query = self.request.GET.get('max_price', 0)
        max_price = 0 if max_price_query == '' else int(max_price_query)

        if max_price != 0:
            queryset = queryset.filter(Q(price__gte=min_price) & Q(price__lte=max_price))

        apply_categories = self.request.GET.getlist('category')

        if len(apply_categories) != 0:
            queryset = queryset.filter(category__in=apply_categories)

        apply_materials = self.request.GET.getlist('material', [])

        if len(apply_materials) != 0:
            queryset = queryset.filter(materials__in=apply_materials)

        apply_brands = self.request.GET.getlist('brand', [])

        if len(apply_brands) != 0:
            queryset = queryset.filter(brand__in=apply_brands)

        search_query = self.request.GET.get('search', '')
        if search_query != '':
            queryset = queryset.filter(name__iregex=search_query)

        return queryset.distinct()
