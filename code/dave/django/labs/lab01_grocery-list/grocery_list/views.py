from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import GroceryItem
from .forms import GroceryItemForm

# Create your views here.

def index(request):
    items = GroceryItem.objects.all()

    form = GroceryItemForm()

    if request.method == 'POST':
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'items':items, 'form':form}
    return  render(request, 'grocery_list/list.html', context)

def updateItem(request, pk):
    item = GroceryItem.objects.get(id=pk)

    form = GroceryItemForm(instance=item)

    if request.method == 'POST':
        form = GroceryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}

    return render(request, 'grocery_list/update_item.html', context)

def deleteItem(request, pk):
    item = GroceryItem.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'grocery_list/delete.html', context)