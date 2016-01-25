from django.conf import settings
from django import forms

from django.shortcuts import render
from django.http import HttpResponse
from log_ap.forms import *

# Create your views here.i

def log(request):
    return HttpResponse("form log")

def index(request):
    form = hoursForm()
    context = { 'form' : form }
    return render(request, 'log_ap/index.html', context)

