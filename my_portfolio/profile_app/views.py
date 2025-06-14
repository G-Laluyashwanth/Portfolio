from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello, You're at index page.")

def about(request):
    return HttpResponse("Hello, You're at about page.👏")