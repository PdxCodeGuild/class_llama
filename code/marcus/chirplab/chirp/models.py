from django.db import models
from django.urls import reverse

class Chirping(models.Model):
    chirpauthor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    chirpdate = models.DateTimeField(auto_now_add=True)
    chirp_char = models.CharField(max_length=280)


    def __str__(self):
        return self.chirp_char
