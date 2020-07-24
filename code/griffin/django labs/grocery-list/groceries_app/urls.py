from django.urls import path

from . import views

app_name = 'groceries_app'


urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.add, name='add'),
    path('update/<int:item_id>',views.update, name='update'),
    path('delete/<int:item_id>',views.delete, name='delete')
]
