from django.db import models
from django.contrib import admin

class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=30)
    year = models.DateField()
    price = models.IntegerField()

class CarAdmin(admin.ModelAdmin):
    list_display = ('id','brand','model','year','price')
