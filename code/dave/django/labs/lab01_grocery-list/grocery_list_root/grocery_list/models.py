import datetime
from django.db import models

   
class GroceryItem(models.Model):
    item_description = models.CharField(max_length=50)
    created_date = models.DateTimeField('Date Created')
    completed_date = models.DateTimeField('Date Completed')
    is_complete = models.BooleanField()