from django.contrib import admin
from .models import Product,Category,CartItem,Cart
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(CartItem)
admin.site.register(Cart)