from django.urls import path 

from . import views


app_name = 'grocery_list'
urlpatterns = [
    path('', views.index, name='index'), 
    path('itemlist/', views.itemlist, name='itemlist'),
    path('update/<int:grocery_id>/', views.update, name='update'),
]