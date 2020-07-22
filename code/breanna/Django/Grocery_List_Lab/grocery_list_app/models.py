import datetime

from django.db import models
# from django.utils import timezone ?


# model called GroceryItem
# contains a text description, a created date, a completed date, and a boolean representing whether it was completed

class GroceryItem(models.Model):

