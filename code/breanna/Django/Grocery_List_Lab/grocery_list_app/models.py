from django.db import models


# model called GroceryItem
# contains a text description, a created date, a completed date, and a boolean representing whether it was completed

class GroceryItem(models.Model):
    grocery_item = models.CharField(max_length=100)
    created_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.grocery_item, self.created_date

        
