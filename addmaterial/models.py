from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Addmaterial(models.Model):
    material_type = models.CharField(max_length=10)
    author = models.CharField(max_length=150, blank=True)
    title = models.CharField(max_length=250)
    language = models.CharField(max_length=100)
    year = models.IntegerField()
    pages = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.title}'

class Publishmaterial(models.Model):
    material_id = models.ForeignKey(Addmaterial, on_delete=models.CASCADE)
    is_loaned = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    published_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.material_id}'