from django.contrib import admin

from .models import ProductType, Product


class ProductInline(admin.TabularInline):
    model = Product


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    inline = [ProductInline]

    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    model = Product
    
    search_fields = ['name']
    list_display = ['name', 'product_type', 'price']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)