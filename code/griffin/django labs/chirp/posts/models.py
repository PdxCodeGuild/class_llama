from django.db import models
from django.urls import reverse

class Post(models.Model):
    chirp = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)


    def __str__(self):
        return self.chirp

    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.id,))
