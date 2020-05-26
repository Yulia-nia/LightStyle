from django.http import Http404
from django.shortcuts import render
from users.models import User
from users.forms import RegistrationForm


def register(request):
    if request.method == 'GET':
        form = RegistrationForm()
        return render(request, 'register.html', context={
            "form": form
        })

    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'register_succes.html', context={"form": form})
        else:
            return render(request, 'register.html', context={"form": form})


def login(request):
    return render(request, 'login.html')
