from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    username = models.CharField(max_length=50)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    date_modified = models.DateTimeField(default=timezone.now) # doesn't call timezone.now() function but uses the meta data to store current dt field
    
    def __str__(self):
        return self.username