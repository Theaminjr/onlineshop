from django.db import models
from products.models import Product
# Create your models here.

class OrderItem(models.Model):
    products = models.ForeignKey(Product, on_delete=models.RESTRICT)
    count = models.IntegerField()

class Order(models.Model):
    status_choices = [("PENDING", "pending"),("CANCELED", "canceled"),("DELIVERED","delivered")]
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=status_choices,default="PENDING")
    items = models.ManyToManyField(OrderItem)