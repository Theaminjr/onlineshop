from django.db import models
from products.models import Product
from core.models import User
# Create your models here.

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    count = models.IntegerField()

    @property
    def price(self):
        return self.product.price * self.count

    @property
    def discount(self):
        return self.count * self.product.discount





class Order(models.Model):
    status_choices = [("PENDING", "pending"),("CANCELED", "canceled"),("DELIVERED","delivered")]
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=status_choices,default="PENDING")
    items = models.ManyToManyField(OrderItem)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    
    @property
    def price(self):
        total = 0
        for item in self.items.all():
            total += item.price
        return total
    
    @property
    def discount(self):
        total = 0
        for item in self.items.all():
            total += item.discount
        return int(total)



    def __str__(self):
        return f"{self.date} {self.price} {self.discount}"
