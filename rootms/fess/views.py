from django.shortcuts import render

# Create your views here.
def fess(request):
    return render(request, 'fess.html')