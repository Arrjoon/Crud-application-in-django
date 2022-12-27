from argparse import Action
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from .forms import loginForm
# Create your views here.

# this function add and show


def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            rg = User(name=nm, email=em, password=ps)
            rg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()

    stud = User.objects.all()

    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})
# this funtion will delete

# this functon update /edit


def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(id=id)
        print(pi)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(id=id)
        fm = StudentRegistration(request.POST, instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': fm})


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(id=id)
        pi.delete()
        return HttpResponseRedirect('/')


def showLoginForms(request):
    fm = loginForm(auto_id=True)

    return render(request, 'enroll/Demo.html', {'form': fm})
