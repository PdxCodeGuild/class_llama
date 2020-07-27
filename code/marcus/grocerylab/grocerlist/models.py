from django.conf import settings
from django.db import models
from django.utils import timezone



class Grocery_List(models.Model):
    # title
    groceryitem = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now())
    completed_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.groceryitem