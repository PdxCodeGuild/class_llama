from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'url_shortener_app'

urlpatterns = [    
    path('',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('<str:short_url>',views.lookup,name='lookup')
]