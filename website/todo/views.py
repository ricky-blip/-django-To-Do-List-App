from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

# Create your views here.

# function index
def index(request):
    items = Todo.objects.order_by('-id')
    # return HttpResponse("Hello Django")
    return render(request, 'todo/index.html', {'items': items})

# function button Done
def done(request):
    items = Todo.objects.filter(status=True).order_by('-id')
    return render(request, 'todo/index.html', {'items': items})

# function button Pending
def pending(request):
    items = Todo.objects.filter(status=False).order_by('-id')
    return render(request, 'todo/index.html', {'items': items})

# function button Delete All
def delete_all(request):
    return render(request, 'todo/index.html')

# ===========================================
# function button create
def create(request):
    return render(request, 'todo/index.html')

# function button update
def update(request, id):
    return render(request, 'todo/index.html')

# function button delete
def delete(request, id):
    return render(request, 'todo/index.html')