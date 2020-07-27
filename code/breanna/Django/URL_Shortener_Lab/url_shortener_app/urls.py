from django.urls import path
from . import views

app_name = 'url_shortener'
urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit_url, name='submit'),
    path('<str:short_url>/', views.redirect, name='redirect')
]