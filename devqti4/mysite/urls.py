from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('mysite1/', views.mysite , name ="mysite")
]