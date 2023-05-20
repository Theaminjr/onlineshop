from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django_cleanup import cleanup
from core.models import Sale
# Create your models here.





class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True,)
    sub = models.ForeignKey('self', null=True,blank=True, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale,null=True, on_delete=models.SET_NULL)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    code = models.IntegerField(unique=True)
    category = models.ForeignKey(Category, null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,null=True,blank=True)
    description =  RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.ForeignKey(Sale,null=True,blank=True, on_delete=models.SET_NULL)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

@cleanup.select
class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_images')
    Product = models.ForeignKey(Product, null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name