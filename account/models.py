from django.db import models
from django.contrib.auth.models import User
from secrets import token_urlsafe

class PasswordResetRequest(models.Model):
    email = models.CharField(max_length=100)
    token = models.CharField(max_length=43, default=token_urlsafe)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Active: {self.active} // {self.token}'