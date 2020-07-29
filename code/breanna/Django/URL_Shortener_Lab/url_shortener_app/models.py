from django.db import models

class UrlShortener(models.Model):

    long_url = models.CharField(max_length=100)
    short_url = models.CharField(max_length=6)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.long_url 
