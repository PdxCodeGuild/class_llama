from django.shortcuts import render, get_object_or_404
from .models import GroceryItem
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    grocery_items = GroceryItem.objects.all()
    context = {
        'grocery_items':grocery_items,
    }
    return render(request, 'groceries_app/index.html', context)

def add(request):
    description = request.POST['description']
    created_date = timezone.now()
    GroceryItem.objects.create(description = description,created_date=created_date)
    return HttpResponseRedirect(reverse('groceries_app:index'))

def update(request, item_id):
    item_got = get_object_or_404(GroceryItem, pk=item_id)
    item_got.completed = True
    item_got.completed_date = timezone.now()
    item_got.save()
    return HttpResponseRedirect(reverse('groceries_app:index'))

def delete(request, item_id):
    item_got = get_object_or_404(GroceryItem, pk=item_id)
    item_got.delete()
    return HttpResponseRedirect(reverse('groceries_app:index'))