from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .models import PostChirp

class ChirpListView(ListView):
    model = PostChirp
    template_name = 'homepage.html'

class ChirpDetailView(DetailView):
    model = PostChirp
    template_name = 'details.html'

class ChirpCreateView(LoginRequiredMixin, CreateView):
    model = PostChirp
    template_name = 'new_post.html'
    fields = ['title', 'body']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ChirpEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostChirp
    template_name = 'edit_post.html'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostChirp
    template_name = 'delete_post.html'
    success_url = reverse_lazy('chirp:homepage')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author