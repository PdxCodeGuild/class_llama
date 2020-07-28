from django.db import models

# Create your models here.

class ShortUrl(models.Model):
    long_url = models.URLField('URL')
    short_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return str(self.long_url)