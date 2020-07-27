from django.urls import path
from . import views

app_name = 'url_shortener'
urlpatterns = [
    path('', views.submit_url, name='submit'),
    path('', views.redirect, name='redirect')
]