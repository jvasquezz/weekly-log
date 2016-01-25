from django import forms
from log_ap.models import *
from django.forms import ModelForm, Form
from django.contrib.admin import widgets
from django.forms.extras.widgets import *

class hoursForm(forms.Form):
    hours = forms.TimeField()

