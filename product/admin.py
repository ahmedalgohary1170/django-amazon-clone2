from django.contrib import admin

from .models import Products, Brand , ProductImages



class ProductImageInline(admin.TabularInline):
    model = ProductImages



class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Products,ProductAdmin)
admin.site.register(Brand)
