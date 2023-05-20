from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django_cleanup import cleanup
from core.models import Sale
from decimal import Decimal
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(allow_unicode=True,unique=True,blank=True,null=True)
    parent = models.ForeignKey('self', null=True,blank=True,related_name="children", on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale,null=True,blank=True, on_delete=models.SET_NULL)
    


        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name,allow_unicode=True)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

@cleanup.select
class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.IntegerField(unique=True)
    thumbnail = models.OneToOneField(Image,null=True, on_delete=models.SET_NULL,related_name='thumbnail')
    images = models.ManyToManyField(Image)
    category = models.ForeignKey(Category, null=True,on_delete=models.SET_NULL,related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(allow_unicode=True,unique=True,null=True,blank=True)
    description =  RichTextField()
    price = models.IntegerField()
    sale = models.ForeignKey(Sale,null=True,blank=True, on_delete=models.SET_NULL)
    available = models.BooleanField(default=True)
    recommended = models.BooleanField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name,allow_unicode=True)
        super(Product, self).save(*args, **kwargs)

   
   
    @property
    def discount(self):
        if self.sale:
            if self.sale.is_percentage:
                return self.price * self.sale.amount/100
            else:
                return self.sale.amount
        elif self.category.sale:
            if self.category.sale.is_percentage:
                return self.price * self.category.sale.amount/100
        else :
            return 0

    def __str__(self):
        return self.name

