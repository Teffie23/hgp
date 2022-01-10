from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import F
from django.contrib import admin
from django.contrib.auth.models import User
import random
from .utils import *
from .forms import *
class bankhome(DataMixin,ListView):
    model=users
    template_name = 'wallet/home.html'
    context_object_name='posts'
    def get_context_data(self,*,object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Личный кабинет')
        context=dict(list(context.items())+list(c_def.items()))
        return context
class showbalance(DataMixin,DetailView):
    model= users
    template_name = 'wallet/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    def get_context_data(self,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title=context['post'])
        return dict(list(context.items())+list(c_def.items()))
class shownews(DataMixin,ListView):
    model=Apdata
    template_name = 'wallet/posts.html'
    context_object_name = 'posts'
    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Новость')
        return dict(list(context.items())+list(c_def.items()))
    def get_queryset(self):
        return Apdata.objects.all()
class ContactFormView(DataMixin,FormView):
    form_class= ContactForm
    template_name = 'wallet/contact.html'
    success_url = reverse_lazy('home')
    def get_context_data(self,*,object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Обратная связь')
        return dict(list(context.items())+list(c_def.items()))
    def form_valid(self, form):
        print(form.cleaned.data)
        return redirect('home')

class RegisterUser(DataMixin,CreateView):
    form_class = RegisterFormUser
    template_name = 'wallet/register.html'
    success_url = reverse_lazy('home')
    def get_context_data(self,*,object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Регистрация')
        return dict(list(context.items())+list(c_def.items()))
    def form_valid(self, form):
        user=form.save()
        global j
        j=user.username
        print(j)
        j1=j.upper()
        print(j1)
        users.objects.create(title=j,slug=j1,balance=0,currency_id=1)
        login(self.request,user)
        return redirect('home')
class LoginUser(DataMixin,LoginView):
    form_class = LoginUserForm
    template_name = 'wallet/login.html'
    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Авторизация')
        return dict(list(context.items())+list(c_def.items()))
    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')
def info(request):
    return HttpResponse('О банке')
def showpost1(request):
    return HttpResponse(f'статья={post_id}')
class showpost(DataMixin,DetailView):
    model=Apdata
    template_name = 'wallet/post.html'
    slug_url_kwarg='post_slug'
    context_object_name = 'post'
    def get_context_data(self,*,object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Новость')
        return dict(list(context.items())+list(c_def.items()))
    def get_queryset(self):
        return Apdata.objects.all()
class currency(DataMixin, CreateView):
    form_class = currency_change
    template_name = 'wallet/currency_change.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Смена валюты')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        x = {'EUR': {'USD': 1.13,
                     'RUB': 83.1},
             'USD': {'EUR': 0.88,
                     'RUB': 73.2},
             'RUB': {'USD': 0.014,
                     'EUR': 0.012}}
        user = form.save()
        v = user.currency.id
        p=user.currency.buy
        l=user.currency.names
        low=users.objects.get(slug=user.title).currency.names
        das = user.slug
        print(v)
        print(l)
        users.objects.filter(slug=user.title).update(currency=v)
        users.objects.filter(slug=user.title).update(balance=F('balance')*x[low][l])
        users.objects.filter(slug=das).delete()
        return redirect('home')

def my_view(request):
        username = None
        if request.method == 'POST':
            form=Top_up_balance(request.POST)
            if form.is_valid():
                user=form.save()
                if request.user.is_authenticated:
                    username = request.user.username
                    v=user.balance
                    d=user.slug
                    users.objects.filter(title=username).update(balance=F('balance') - v)
                    users.objects.filter(slug=user.title).update(balance=F('balance') + v)
                    users.objects.filter(slug=d).delete()
                    return redirect('/')

        else:
            form=Top_up_balance()
        return render(request,'wallet/up_balance.html',{'form':form})
# Create your views here.
