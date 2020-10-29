from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.addandshow,name ="addandshow"),
    path('update/',views.update, name = "update"),

]
