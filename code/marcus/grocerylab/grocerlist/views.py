from django.shortcuts import render, get_object_or_404
from .models import Grocery_List
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


def index(request):
    grocerydb = Grocery_List.objects.filter(completed=False)

    completeddb = Grocery_List.objects.filter(completed=True)

    context = {
        'grocerydb':grocerydb, 
        'completeddb':completeddb
    }
    
    
    return render(request, 'grocerlist/index.html', context)

def add(request):
    addgrocery = request.POST['adder']
    Grocery_List.objects.create(groceryitem=addgrocery)

    return HttpResponseRedirect(reverse('grocerlist:index'))

def completed(request,item_id):
    completegrocery = get_object_or_404(Grocery_List, pk=item_id)
    completegrocery.completed_date = timezone.now()
    completegrocery.completed = True
    completegrocery.save()

    return HttpResponseRedirect(reverse('grocerlist:index'))

def delete(request,item_id):
    item = get_object_or_404(Grocery_List, pk=item_id)
    item.delete()
    
    return HttpResponseRedirect(reverse('grocerlist:index'))

# Create your views here.
