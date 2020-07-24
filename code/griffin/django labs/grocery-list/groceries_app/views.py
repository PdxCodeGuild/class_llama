from django.shortcuts import render
from .models import GroceryItem

def index(request):
    grocery_items = GroceryItem.objects.all()
    context = {
        'grocery_items':grocery_items,
    }
    print(context)
    return render(request, 'groceries_app/index.html', context)

def add():
    pass

def update():
    pass

def delete():
    pass
