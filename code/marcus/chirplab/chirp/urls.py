
from django.urls import path
from . import views
app_name = 'chirp'

urlpatterns = [
    path('', views.ChirpListView.as_view(), name='home' ),
    path('chirping_page/newpost', views.ChirpCreateView.as_view(), name='newpost' ),
    # path()


]