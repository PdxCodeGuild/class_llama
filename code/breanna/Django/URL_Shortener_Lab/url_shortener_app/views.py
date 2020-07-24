from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def submit_url(request):
    return HttpResponse('ok')

def redirect(request):
    return HttpResponse('ok')
