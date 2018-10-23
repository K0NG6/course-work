from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone


def index(request):
    return render(request, 'tamplates/index.html', {})

# Create your views here.
