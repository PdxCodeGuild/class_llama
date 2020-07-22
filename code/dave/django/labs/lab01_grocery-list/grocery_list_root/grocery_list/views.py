from django.shortcuts import render

def index(request):
    return render(request, 'grocery_list/index.html')
