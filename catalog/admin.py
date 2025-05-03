from django.contrib import admin
from .models import Product, Category, Contact


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')
    search_fields = ('name', 'description')
    list_filter = ('category__name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('name',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'message')
    search_fields = ('name',)
    list_filter = ('name',)
