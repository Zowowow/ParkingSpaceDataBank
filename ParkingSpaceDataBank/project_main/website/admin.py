from django.contrib import admin
from .models import Car, TimeStamps

# Register your models here.

admin.site.register(Car)
admin.site.register(TimeStamps)