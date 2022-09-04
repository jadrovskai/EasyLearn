from django.shortcuts import render

from django.http import HttpResponse
from .models import Subject, Video

# Create your views here.

def homepage(request):
    return render(request, "homepage.html")

def contactus(request):
    return render(request, "contactus.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def subjects(request):
    context = {"subjects": Subject.objects.all()}
    return render(request, "subjects.html", context=context)

def videos(request):
    context = {"videos": Video.objects.all()}
    return render(request, "videos.html", context=context)

