from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Car(models.Model):
    owner = models.ForeignKey(User, default="",on_delete=models.CASCADE, null=True)
    car_model = models.CharField('Car Name', max_length=120)
    car_manufacturer = models.CharField('Car Manufacturer', max_length=120)
    car_color = models.CharField('Car Color', max_length=120)
    plate_num = models.CharField('Plate Number', max_length=20)

    def __str__(self):
        return self.car_model

