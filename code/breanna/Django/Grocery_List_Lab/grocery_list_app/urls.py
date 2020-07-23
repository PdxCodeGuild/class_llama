from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('completed/<int:grocery_item_id>/', views.completed, name='completed'),
    path('deleted/<int:grocery_item_id>/', views.deleted, name='deleted')
]