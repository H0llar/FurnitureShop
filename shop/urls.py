from django.urls import path

from shop.views import CatalogView, ProductDetail

app_name = 'shop'

urlpatterns = [
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('details/<int:pk>', ProductDetail.as_view(), name='details'),
]
