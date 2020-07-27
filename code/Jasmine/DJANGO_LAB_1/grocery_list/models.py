from django.db import models


class GroceryItem(models.Model): 
    item = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    complete_date = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)

    def __str__(self): 
        return self.item