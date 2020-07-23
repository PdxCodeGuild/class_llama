from django.urls import path

from . import views

app_name = 'groceries_app'


urlpatterns = [
    path('', views.index, name='index'),
    
]
