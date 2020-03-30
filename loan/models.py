from django.contrib.auth.models import User
from django.db import models
from addmaterial.models import Publishmaterial
from datetime import datetime

class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Publishmaterial, on_delete=models.CASCADE)
    loan_datetime = models.DateTimeField(default=datetime.now())
    loan_return_datetime = models.DateTimeField(blank=True, null=True)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.user}: {self.book_id}'

    @property
    def date_diff(self):
        return (self.loan_datetime - self.loan_return_datetime).days