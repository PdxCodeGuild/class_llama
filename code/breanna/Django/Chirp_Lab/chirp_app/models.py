from django.db import models
from django.urls import reverse

class PostChirp(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __str__(self):
        return self.title