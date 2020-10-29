from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('app/', views.myroot, name="myroot"),

]
