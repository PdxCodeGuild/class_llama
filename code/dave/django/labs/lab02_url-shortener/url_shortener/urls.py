from django.urls import path

from url_shortener import views

appname = 'url_shortener'

urlpatterns = [
    path('', views.url_submit, name='url submit'),
    path('redirect/', views.redirect_user, name='redirect_user'),
]