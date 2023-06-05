from django.contrib import admin
from .models import Order,OrderItem


class CustomOrderAdmin(admin.ModelAdmin):
    model = Order
    ordering = ['date']
    list_display = ['date','price']
    list_filter = ("status", )

class CusomOrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ['product','count']


# Register your models here.
admin.site.register(OrderItem,CusomOrderItemAdmin)
admin.site.register(Order,CustomOrderAdmin)