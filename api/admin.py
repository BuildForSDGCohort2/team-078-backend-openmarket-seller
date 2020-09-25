from django.contrib import admin
from .models import Profile, Product, SellerProfile, Category, Order, OrderDetail

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(SellerProfile)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderDetail)