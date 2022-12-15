from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import johnlist


# Create your views here.

def index(request):
    namelist = johnlist.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'johnlist': namelist,
    }
    return HttpResponse(template.render(context, request))

