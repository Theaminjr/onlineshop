from django.contrib import admin
from .models import Product,Category,Image


class CustomCategoryAdmin(admin.ModelAdmin):
    model = Category
    ordering = ['name']
    list_display = ['name','parent']
    list_filter = ("parent", )

class CustomProductAdmin(admin.ModelAdmin):
    model = Product
    ordering = ['name']
    list_display = ['thumbnail_img','name','price','available']
    list_filter = ("available","recommended" )

class CustomImageAdmin(admin.ModelAdmin):
    model = Image()
    ordering = ['name']
    list_display = ['img','name']


admin.site.register(Product,CustomProductAdmin)
admin.site.register(Category,CustomCategoryAdmin)
admin.site.register(Image,CustomImageAdmin)