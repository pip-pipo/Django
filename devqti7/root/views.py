from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .forms import studentReg
from .models import user


def update(request):
    return render(request, "update.html")


def addandshow(request):
    if request.method == 'POST':
        fm = studentReg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = user(name=nm, email=em, password=pw)
            reg.save()
        fm = studentReg()

    else:
        fm = studentReg()

    stud = user.objects.all()

    return render(request, "addandshow.html", {'form': fm, 'stu': stud})


def delete_data(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
