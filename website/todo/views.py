from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# function index
def index(request):
    return HttpResponse("Hello Django")