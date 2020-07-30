from django.urls import path

from . import views

appname = 'posts'

urlpatterns = [
    path('', views.home, name='home'),
]