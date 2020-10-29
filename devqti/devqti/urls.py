"""devqti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mmmm import views as mv
from bi import views as bv

micorse = [

    path('bibi/', bv.bi_django),
    path('bibimi/', bv.bi_django_bi),

]

bicorse = [
    path('mimi/', mv.mi_django),
    path('mimibi/', mv.mi_flask),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi/', include(bicorse)),
    path('bi/', include(micorse)),
]
