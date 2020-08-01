from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Chirps(models.Model):
    chirp = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.chirp