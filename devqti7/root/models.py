from django.db import models

# # Create your models here.
# class user(models.Model):
#     name = models.CharField(max_length=70)
#     email = models.EmailField(max_length=254)
#     password = models.CharField(max_length=100)

class user(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
