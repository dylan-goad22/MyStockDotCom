from django.contrib import admin

from app.models import Investment, Stock

# Register your models here.

admin.site.register(Stock)
admin.site.register(Investment)