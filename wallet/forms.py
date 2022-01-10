from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from django.contrib import admin
from .models import *
from django.core.exceptions import ValidationError
class addnews(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['cat'].empty_label='Категория не выбрана'
    class Meta:
        model=users
        fields='__all__'
        widgets={
            'title':forms.TextInput(attrs={'class':'form-input'}),
        }
class RegisterFormUser(UserCreationForm):
    username=forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='Повтор пароля',widget=forms.PasswordInput(attrs={'class':'form-input'}))
    class Meta:
        model=User
        fields=('username','password1','password2')
class LoginUserForm(AuthenticationForm):
    username=forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class':'form-input'}))
    password=forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class':'form-input'}))
class ContactForm(forms.Form):
    name=forms.CharField(label='Имя',max_length=255)
    content=forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}))
    captcha=CaptchaField()
#class Top_up_balance(forms.Form):
 #   content = forms.FloatField(label='Сумма',widget=forms.NumberInput())
class Top_up_balance(forms.ModelForm):
    #title=forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class':'form-input'}))
   # balance = forms.FloatField(label='Пароль',widget=forms.NumberInput(attrs={'class':'form-input'}))
    prepopulated_fields = {'slug': ('title', 'balance')}
    class Meta:
        model=users
        fields='__all__'
class currency_change(forms.ModelForm):
    class Meta:
        model = users
        fields = '__all__'

