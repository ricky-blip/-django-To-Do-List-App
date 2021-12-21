from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# function index
def index(request):
    # return HttpResponse("Hello Django")
    return render(request, 'todo/index.html')

# function button Done
def done(request):
    return render(request, 'todo/index.html')

# function button Pending
def pending(request):
    return render(request, 'todo/index.html')

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