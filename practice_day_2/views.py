from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from . import forms
from albums.models import AlbumsModel
from musician.models import MusicianModel
# Create your views here.
class Signup(CreateView):
    form_class = forms.SignupForms
    template_name = 'signup.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        user = form.save()
        messages.success(self.request,'signup successfully')
        return super().form_valid(form)

class LoginView(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        messages.success(self.request,'login successfully')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.warning(self.request,'logged in information is incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']  = 'login'
        return context
        
        
class CustomLogoutView(LogoutView):
    def get_redirect_url(self):
        return reverse_lazy('login')

def home(request):
    data = AlbumsModel.objects.all()
    return render(request,'home.html',{'data':data})

class HomeView(ListView):
    model = AlbumsModel
    template_name = 'home.html'
    context_object_name = 'data'
    

    