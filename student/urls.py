from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='home'),
    path('upload', views.upload, name='upload'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('report', views.report, name='report'),
    path('search', views.search, name='search'), 

]
