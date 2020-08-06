from django.urls import path
from . import views

appname = 'users'

urlpatterns = [
    path('signup/', views.signup, name='users-signup'),
]