from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def url_submit(request, *args, **kwargs):
    return HttpResponse('hi')

def redirect_user(request, *args, **kwargs):
    return HttpResponseRedirect('hi, again')