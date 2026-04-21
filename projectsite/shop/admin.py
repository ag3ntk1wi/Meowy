from django.contrib import admin
from .models import Product, ProductVariant, Cart, CartItem, Order, OrderItem

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)