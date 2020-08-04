from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post

class ChirpListView(ListView):
    model = Post
    template_name = 'home.html'

class ChirpCreateView(CreateView):
    model = Post
    template_name = 'post_chirp.html'
    fields = ['chirp']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ChirpDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class ChirpUpdateView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['chirp']

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

class ChirpDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('posts:home')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author