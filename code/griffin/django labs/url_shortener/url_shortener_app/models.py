from django.db import models
import string
import random




class UrlCode(models.Model):
    long_url = models.TextField()
    secret_code = ""

    def __str__(self):
        return self.long_url
    
        