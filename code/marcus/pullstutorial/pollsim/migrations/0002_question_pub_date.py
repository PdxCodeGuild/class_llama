# Generated by Django 3.0.8 on 2020-07-17 17:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pollsim', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 17, 25, 22, 702487, tzinfo=utc)),
            preserve_default=False,
        ),
    ]