from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.





class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    sub = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(MyModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description =  RichTextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(MyModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_images')
    Product = models.ForeignKey(Product, null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.title