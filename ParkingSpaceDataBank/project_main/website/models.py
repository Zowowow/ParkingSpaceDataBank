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
        return f'{self.owner} / ' + self.car_model + f' / {self.car_manufacturer}' + f' / {self.car_color}' + f' / {self.plate_num}'

class TimeStamps(models.Model):
    Parker = models.ForeignKey(User, default="",on_delete=models.CASCADE, null=True)
    activity = models.CharField('Car Name', max_length=120)
    timestamp = models.TimeField(auto_now_add= True)
    datestamp = models.DateField(auto_now_add= True)
    
    def __str__(self):
        return f'{self.Parker} / ' + self.datestamp.strftime('%d-%m-%Y') + f'/ {self.timestamp}'
