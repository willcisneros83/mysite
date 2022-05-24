from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    price = models.FloatField()
    profile_picture = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True) 

class Order(models.Model):    
    total = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    products = models.ManyToManyField(Product, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)



