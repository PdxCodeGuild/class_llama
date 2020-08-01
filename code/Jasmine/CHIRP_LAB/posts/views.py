from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post

class ChirpListView(ListView): 
    model = Post
    template_name = 'home.html'

class ChirpDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class ChirpCreateView(CreateView): 
    model = Post
    template_name = 'post_new.html'
    fields = ['body']

class ChirpEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['body']

class ChirpDeleteView(DeleteView): 
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:home')
