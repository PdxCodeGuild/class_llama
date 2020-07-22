from django.db import models


class GroceryItem(models.Model): 
    item = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    completed_date = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self): 
        return self.item