from django.contrib import admin
from .models import Category, ShopItem, Brand
# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ShopItem)