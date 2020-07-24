from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem

def index(request): 
    grocery_item = GroceryItem.objects.all()
    context = {
        'grocery_item': grocery_item
    }
    print(context)
    return render(request, "grocery_list/index.html", context)

 
def itemlist(request):
    post_item = request.POST['grocery']
    GroceryItem.objects.create(item=post_item, create_date=timezone.now())
    return HttpResponseRedirect(reverse('grocery_list:index'))

def update(request, grocery_id): 
    complete = get_object_or_404(GroceryItem, pk= grocery_id)
    complete.complete_date = timezone.now()
    complete.is_done = True
    complete.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete(request, grocery_id):
    deleteitem = get_object_or_404(GroceryItem, pk= grocery_id)
    
