# Ex02 Django ORM Web Application
## Date: 18-09-2025

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

<img width="1539" height="1027" alt="Screenshot 2025-09-17 135617" src="https://github.com/user-attachments/assets/469bbc74-4b90-4ebf-8db9-2c1c4e33fbcc" />


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
Models.py
```
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
```
Admin.py
```
from django.contrib import admin
from . models import Car, CarAdmin

# Register your models here.
admin.site.register(Car, CarAdmin)
```

## OUTPUT

<img width="1919" height="938" alt="Screenshot 2025-09-17 133112" src="https://github.com/user-attachments/assets/798f55a8-4a2e-4187-8509-1ec4b311bc6b" />



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
