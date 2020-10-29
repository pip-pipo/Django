from django.shortcuts import render

# Create your views here.

def mysite(request):
    return render(request, 'mysite/index.html')