from django.contrib import admin
from django.urls import path
from student import views
from django.urls import reverse

urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='home'),
    path('upload', views.upload, name='upload'),
    path('uploadei', views.uploadei, name='uploadei'),
    path('uploadic', views.uploadic, name='uploadic'),
    path('about', views.about, name='about'),
    path('report/<int:pk>', views.report, name='report'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('update/<int:pk>', views.update, name='update'),
    path('search', views.search, name='search'), 

]
