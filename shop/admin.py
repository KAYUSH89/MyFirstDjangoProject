from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    list_filter = ["name"]
    search_fields = ["name", "email"]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductTypeAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)
