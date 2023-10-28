from django.contrib import admin
from .models import Product, Customer, Order, OrderItem, ShippingAddress

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
