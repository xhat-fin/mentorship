from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def registration(request):
    return render(request, "auth_jwt/registration.html")


def sign_in(request):
    return render(request, "auth_jwt/sign-in.html")


def redirect_index(request):
    return redirect('http://127.0.0.1:8000/')
