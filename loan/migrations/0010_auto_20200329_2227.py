# Generated by Django 3.0.4 on 2020-03-29 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0009_auto_20200329_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 29, 22, 27, 17, 402374)),
        ),
    ]