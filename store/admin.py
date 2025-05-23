from django.contrib import admin
from .models import Product, Order, OrderItem

#@admin.register (Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity_in_stock', 'description']
    list_filter = ['price']
    search_fields = ['name', 'description']
    fields = ['name', 'price', 'quantity_in_stock', 'description', 'image']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'guest_name', 'guest_email', 'ordered_at', 'status')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'customization')

admin.site.register(Product, ProductAdmin)
