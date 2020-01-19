from django.db import models

# Create your models here.
class User(models.Model):   
    SEXE = [
        ("Men", "Male"), 
        ("Women", "Female")
    ]
    SEASONS = [
        ("Summer", "Summer"),
        ("Fall", "Fall"),
        ("Spring", "Spring"),
        ("Winter", "Winter")
    ]
    name = models.CharField(max_length = 30, default = "Please enter your name")
    gender = models.CharField(max_length = 20, choices = SEXE)
    height = models.DecimalField(max_digits = 5, decimal_places = 2)
    season = models.CharField(max_length = 20, choices = SEASONS)
    usage = models.CharField(max_length = 20, default = "Casual")