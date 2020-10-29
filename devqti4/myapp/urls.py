from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('myapp1/', views.myapp , name='myapp')
]