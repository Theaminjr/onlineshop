from django import forms
from django.forms import ModelForm
from .models import Product

class CreateProduct(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
