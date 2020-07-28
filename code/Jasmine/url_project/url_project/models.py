from django.db import models

# Create your models here.

class url(models.Model): 
    long_url = models.URLField(max_length=200)
    short_url = models.URLField(max_length=200)


    def __str__(self): 
        return self.short_url
