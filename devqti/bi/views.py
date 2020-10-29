from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bi_django(request):
    return HttpResponse('hhhhllo')

def bi_django_bi(request):
    return HttpResponse('bi')