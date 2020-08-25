from django.urls import path

from .views import ListStudent, DetailStudent

urlpatterns = [
    path('students/', ListStudent.as_view()),
    path('students/<int:pk>/', DetailStudent.as_view())
]