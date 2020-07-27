from django.urls import path
from . import views


app_name = "grocerlist"



urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add' ),
    path('completed/<int:item_id>', views.completed, name= 'completed'),
    path('delete/<int:item_id>', views.delete, name= 'delete'),
]
