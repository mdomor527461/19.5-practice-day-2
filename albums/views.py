from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from . import models,forms
from django.urls import reverse_lazy
# Create your views here.
class AddAlbum(CreateView):
    model = models.AlbumsModel
    template_name = 'add_album.html'
    form_class = forms.AlbumForm
    success_url = '/'

    
class EditAlbum(UpdateView):
    model = models.AlbumsModel
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
    
    
class DeleteAlbum(DeleteView):
    model = models.AlbumsModel
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
    
