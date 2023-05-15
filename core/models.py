from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

class Sale(models.Model):
    percentage = models.FloatField(null=True)
    cash = models.DecimalField(null=True,max_digits=10, decimal_places=2)



class CustomUserManager(BaseUserManager):

    def create_user(self, email, password,**extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.phone_number = extra_fields['phone_number']
        user.full_name= extra_fields['full_name']
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.full_name= extra_fields['full_name']
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    full_name = models.CharField(max_length=75)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    is_productmanager = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)
    is_operator = models.BooleanField(default=False)
    sale = models.ForeignKey(Sale,null=True, on_delete=models.SET_NULL)
    REQUIRED_FIELDS=['full_name',]
    USERNAME_FIELD = "email"
    objects = CustomUserManager()


class Address(models.Model):
    location = models.CharField(max_length=600)
    user = models.ForeignKey(User, on_delete=models.CASCADE)