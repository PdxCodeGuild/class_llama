from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

class ChirpListView(ListView):
    model = Post
    template_name = 'home.html'

# class ChirpCreateView(CreateView):
#     model = Post
#     template_name = post_chirp.html
#     fields = ['chirp']
