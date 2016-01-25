from django.conf import settings
from django import forms

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.i

def log_call(request):
    return HttpResponse("form log")
