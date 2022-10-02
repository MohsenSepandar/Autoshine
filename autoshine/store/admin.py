from django.contrib import admin
from .models import ProductAndService, Category, Cart, Customer, Reception


@admin.register(ProductAndService)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'unit_price', 'category']
    ordering = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'service_type']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'first_name', 'last_name', 'user']


@admin.register(Reception)
class ReceptionAdmin(admin.ModelAdmin):
    list_display = ['customer', 'entry_date', 'total_price', 'cart', 'payment_status']
    list_editable = ['payment_status']
