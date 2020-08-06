from django.urls import path
from posts import views

appname = 'posts'

urlpatterns = [
    path('', views.home, name='posts-home')
]