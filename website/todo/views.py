from django.shortcuts import render, reverse
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

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
    Todo.objects.all().delete()
    return HttpResponseRedirect(reverse('index'))

# ===========================================
# function button create
def create(request):
    # return render(request, 'todo/index.html')
    try:
        title = request.POST['title']
        
        todo = Todo(title=title)
        todo.save()
        return HttpResponseRedirect(reverse('index'))
    except:
        return HttpResponseRedirect(reverse('index'))

# function button update
def update(request, id):
    try:
        todo = Todo.objects.get(id=id)
        todo.status = not todo.status
        todo.save()
        return HttpResponseRedirect(reverse('index'))
    
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('index'))

# function button delete
def delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
        todo.delete()
        return HttpResponseRedirect(reverse('index'))
    
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('index'))