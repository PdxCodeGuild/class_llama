from django.urls import path
from . import views

app_name = 'chirp'
urlpatterns = [
    path('', views.ChirpListView.as_view(), name='homepage'),
    path('post/<int:pk>/', views.ChirpDetailView.as_view(), name='detail'),
    # path('post/new/', views.BlogCreateView.as_view(), name='new'),
    # path('post/<int:pk>/edit/', views.BlogEditView.as_view(), name='edit'),
    # path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='delete'),
]