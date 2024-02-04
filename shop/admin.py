from django.contrib import admin

from shop.models import Brand, Category, Product, ProductImage, Material

admin.site.register(Brand)
admin.site.register(Material)
admin.site.register(Category)


class ProductImageAdminInline(admin.TabularInline):
    model = ProductImage
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImageAdminInline,)
