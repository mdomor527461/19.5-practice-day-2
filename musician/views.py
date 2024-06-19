from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from . import models,forms
from .models import MusicianModel
from django.urls import reverse_lazy
# Create your views here.
class AddMusician(CreateView):
    model = models.MusicianModel
    template_name = 'add_musician.html'
    form_class = forms.MusicianForm
    success_url = '/'

class EditMusician(UpdateView):
    model = MusicianModel
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
    form_class = forms.MusicianForm