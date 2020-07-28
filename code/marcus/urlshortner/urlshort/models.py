from django.conf import settings
from django.db import models
from django.utils import timezone



class Url_shortner(models.Model):
    urlentry = models.CharField(max_length=200)
    



