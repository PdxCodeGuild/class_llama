from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.ChirpListView.as_view(), name="home"),
    path('post/new_chirp/', views.ChirpCreateView.as_view(), name='new_chirp'),
    path('post/<int:pk>/', views.ChirpDetailView.as_view(), name='detail'),
    path('post/<int:pk>/update/', views.ChirpUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', views.ChirpDeleteView.as_view(), name='delete'),
]