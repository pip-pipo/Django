from django.shortcuts import render

# Create your views here.
def myroot(request):
    return render(request, "myroot.html")