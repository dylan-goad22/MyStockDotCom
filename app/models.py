from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib import admin
from django.conf import settings
from django.db.models.fields import DecimalField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    abb_name = models.TextField(null=True)
    full_name = models.TextField(null=True)
    current_price = models.DecimalField(max_digits=9, decimal_places=2, null=True)

class Investment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=CASCADE, null=True)
    stock = models.OneToOneField(Stock, on_delete=CASCADE, null=True)
    amount = models.PositiveIntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)