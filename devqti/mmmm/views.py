from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Create your views here.
def mi_django(request):
    return HttpResponse('hello')

def mi_flask(request):
    return HttpResponse('bi')