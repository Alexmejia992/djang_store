from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category_name     

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    description = RichTextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to = 'images/',  null=True, blank=True)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    create_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product_name
