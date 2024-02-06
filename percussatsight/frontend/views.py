from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
# Create your views here.

def index(request):
    return HttpResponse("Hello world")

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def sheetspage(request):
    template = loader.get_template('sheetspage.html')
    return HttpResponse(template.render())
