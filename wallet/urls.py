from django.urls import path
from .views import *
urlpatterns = [
    path('',bankhome.as_view(),name='home'),
    path('info',info,name='info'),
    path('news/', shownews.as_view(), name='news'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('register/',RegisterUser.as_view(),name='register'),
    path('post/<slug:post_slug>/',showpost.as_view(),name='post'),
    path('top_up_balance/',my_view,name='up'),
    path('currency_change/',currency.as_view(),name='change'),
    path('login/',LoginUser.as_view() , name='login'),
    path('logout/', logout_user, name='logout'),
   # path('lo/',my_view,name='test')
]