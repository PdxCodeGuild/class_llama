# Generated by Django 3.0.8 on 2020-07-28 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0002_auto_20200728_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='long_url',
            field=models.URLField(verbose_name='URL'),
        ),
    ]
