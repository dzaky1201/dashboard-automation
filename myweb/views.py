from .forms import ConfigForms
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())