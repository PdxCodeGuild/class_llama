from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Chirping

class ChirpListView(ListView):
    # Holds the chirps that have been created
    model = Chirping
    template_name = 'home.html'

class ChirpCreateView(CreateView):
    # Requires User to Login to post (LoginRequiredMixIn)
    model = Chirping
    template_name = 'newchirp.html'
    fields = ['chirp_char']

    def validation(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ChirpEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Chirping
    template_name = 'chirp_edit.html'
    fields = ['chirp_char']

class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chirping
    template_name = 'chirp_delete.html'
    success_url = reverse_lazy('chirp:home')

     











