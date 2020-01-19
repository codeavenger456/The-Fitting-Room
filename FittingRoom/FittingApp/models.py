from django.db import models

# Create your models here.
class User(models.Model):   
    SEXE = [
        ("M", "Male"), 
        ("W", "Female")
    ]
    name = models.CharField(max_length = 30, default = "Please enter your name")
    gender = models.CharField(max_length = 20, choices = SEXE)
    height = models.DecimalField(max_digits = 5, decimal_places = 2)