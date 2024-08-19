from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('' , views.url_shortner, name = 'url_shortener'),
    path('show/' , views.show_all, name = 'show_all'),
]
