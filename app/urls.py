from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('save-process/', views.save_process),
    path('gamelist/', views.gamelist)
]
