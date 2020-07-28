from django.urls import path
from shorturl import views

appname = 'shorturl'

urlpatterns = [
    path('', views.submit, name='submit'),
    path('<str:token>', views.index, name='index'),
]