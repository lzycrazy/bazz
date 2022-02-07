from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('contact/',views.contact, name='contact'),
    path('about/' ,views.about, name='about'),
    path('terms/',views.terms , name='terms'),
    path('police/',views.police , name='privacy'),
    path('desclimer/',views.desclimer , name='desc'),

]