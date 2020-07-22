from django.shortcuts import render
from django.utils import timezone

from .models import GroceryItem

def Index(request): 
    return render(request, 'grocery_list/index.html')

def createitem(request):
    post_item = request.POST['grocery']
    GroceryItem.objects.create(item=post_item, created_date=timezone.now())

