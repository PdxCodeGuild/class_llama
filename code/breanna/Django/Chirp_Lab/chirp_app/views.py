from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import PostChirp

class ChirpListView(ListView):
    model = PostChirp
    template_name = 'homepage.html'

class ChirpDetailView(DetailView):
    model = PostChirp
    # template_name = detail.html