from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Addmaterial(models.Model):
    material_type =  models.CharField(max_length=10)
    author = models.CharField(max_length=150, blank=True)
    title = models.CharField(max_length=250)
    language = models.CharField(max_length=100)
    year = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(2020),])
    pages = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    quantity_available = models.IntegerField()
    quantity_loaned = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'