from django.contrib import admin
from django.urls import path

from user import views

urlpatterns = [
    path('index/', views.index),
    path('register/', views.register),
    path('login/', views.login),
    # path('logout/', views.logout),
]
