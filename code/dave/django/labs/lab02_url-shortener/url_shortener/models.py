from django.db import models
import random
import string

# Create your models here.

def code_generator(size=6, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for i in range(size))

def create_short_url(instance, size=6):
    new_code = code_generator(size=size)
    UrlClass = instance.__class__
    qs_exists = UrlClass.objects.filter(short_url=new_code).exists()
    if qs_exists:
        return create_short_url(size=size)
    return new_code

class URLShortener(models.Model):
    long_url = models.CharField(max_length=200, )
    short_url = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if self.short_url is None or self.short_url == "":
            self.short_url = code_generator()
        super(URLShortener, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.long_url)

    