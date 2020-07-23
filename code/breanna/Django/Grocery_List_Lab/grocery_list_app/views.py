from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse

from .models import GroceryItem

def index(request):
    grocery_list_incomplete = GroceryItem.objects.filter(completed=False).order_by('created_date')
    grocery_list_completed = GroceryItem.objects.filter(completed=True).order_by('created_date')

    context = {
        'incomplete': grocery_list_incomplete,
        'completed': grocery_list_completed
    }
    return render(request, 'grocery_list/index.html', context)

def add(request):
    GroceryItem.objects.create(grocery_item=request.POST['grocery_item'], created_date=timezone.now())
    return HttpResponseRedirect(reverse('grocery_list:index'))

def completed(request, grocery_item_id):
    grocery_item = get_object_or_404(GroceryItem, pk=grocery_item_id)
    grocery_item.completed = True
    grocery_item.completed_date = timezone.now()
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))
