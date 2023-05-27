from django.contrib import admin
from .models import Category, Products
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display= ['auto_id', 'name', 'description']

class ProductsAdmin(admin.ModelAdmin):
    model = Products
    list_display = ['auto_id', 'name' ,'category', 'description', 'mrp', 'image' ,'is_active']


admin.site.register(Category, CategoryAdmin)   
admin.site.register(Products, ProductsAdmin)
