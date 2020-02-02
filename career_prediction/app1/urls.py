from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$',views.home,name='home'),
    url(r'home/$',views.home,name='home'),
    url(r'form/$',views.form,name='form'),
    url(r'signup/$',views.signup,name='signup'),
    url(r'final/',views.final,name='final'),
    url(r'model/',views.mod,name='mod'),
    url(r'login/', views.login, name='login'),
    url(r'login2/',views.login2,name='login2'),

]