from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from FurnitureShop import settings
from FurnitureShop.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("appauth.urls", namespace="appauth")),
    path('shop/', include("shop.urls", namespace="shop")),
    path('cart/', include("cart.urls", namespace="cart")),
    path('', HomeView.as_view(), name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
