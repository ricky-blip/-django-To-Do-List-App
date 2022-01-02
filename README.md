# Project Website Using Django

DOCS :

========== Setup Project & App ==========
1. Make sure install Python
2. Install PIP
3. Create Virtual Environment
4. install Package Django ```pip install django```
5. Create Project ( **WEBSITE** ) ```django-admin startproject website```
6. Check Django server 
7. Running database migration
8. Running Django Server ```./manage.py runserver```
9. Create App ( TODO LIST ) ```./manage.py startapp todo```

========== Setting Urls & Views ==========

Connect Todo List Application to server 
1. in views.py Create function index for request Response Http
2. Create file urls.py
3. in urls.py Create "urlpatterns" and import file views.py
4. views.py and urls.py in (Todo List Application) supposed to be conected
5. Connect to (Project Website)urls.py
6. in urls.py(Project Website), Import urls.py(Todo List Application)
7. Running Django Server ```./manage.py runserver```
8. urls/(Todo List Application)

========== Setting Templates & Static Files ==========

Templates (file .html)
static    (file .css .js)
1. You need template and static file, you can download from internet or you can build you're own.
2. File templates you can put inside folder ```templates/todo/(yourfileTemplate)``` in you're (Todo List Application)
3. in views.py(Todo List Application), you need change to request render with you're templates file
4. in setting.py(Project Website) you need register you're template file in ```INSTALLED_APPS```  
5. File static you can put inside folder ```static/todo/css/(yourfileTemplate)``` in you're (Todo List Application)
6. in setting.py(Project Website) you will find ```STATIC_URL = 'static/' ```
7. We need call static file in templates file with (Template static --> ```{% load static %}```) for setting static file in templates files
8. in views.py(Todo List Application)
    1. Register function done
    2. Register function pending
    3. Register function delete all
    4. Register function update
    5. Register function create
    6. Register function delete
9. in urls.py(Todo List Application)
    1. Register pathURLS to done
    2. Register pathURLS to pending
    3. Register pathURLS to delete all
    4. Register pathURLS to update and add id
    5. Register pathURLS to create
    6. Register pathURLS to delete and add id
10. in Templates(file .html),change url with 
    ```
    {% url '(name from urls)' %}
    ```

========== Django MODELS ==========

" Table Database == Model Databases. "

We need Field and Columns.
1. Title (Text)
2. Status (Boolean)

Declare Models.
1. in models.py(Todo List Application), we only need saving data TodoApps.
2. Create Models in the form of ```class Todo```
3. Models is ready

We need create Database.
- In Django have concept ```Database Migration``` as noted(like update version) 

1. Create file Migration ```./manage.py makemigrations``` Output : folder migrations(Todo List Application) > ```0001.initial.py```
2. Access models in terminal
3. Activate shell django ```./manage.py shell```
4. Import models ```from todo.models import Todo```
5. Check All Table Database todo ```Todo.objects.all()``` 
6. Create todo content ```id = nameClassinModels(field = 'value')```
7. Save data content to database ```id.save()```
8. Check All Table Database todo ```Todo.objects.all()``` Output : ```<QuerySet [ <Todo: Todo object (1)> , <Todo: Todo object (2)> ]>```
9. Convert Ouput from type >>> id to string
   - in models.py(Todo List Application), create function with method string ```def ___str___(self)```
   - Output will be : ```<QuerySet [ <Todo: id: (string)> , <Todo: id: (string)> ] >```
10. id = PK (Primary Key)
11. Check per-ID or PK ``` Todo.objects.get(id=numberid) ```
12. Update todo content ```id = Todo.objects.get(id=numberid)``` and ```id.namefield = 'updatehere!'``` then save
13. Update todo content ```Todo(namefield='updatehere!').save()```
14. Delete todo content ```id.delete```
15. If you wanna search spesific word use >> Filter data content ```Todo.objects.filter(namefield__startswith='typespesificword')``` 
16. Sort by id ```Todo.objects.order_by('-id')``` symbol - mean from large to small (OPERATION MODELS we can see at Docs Django)

We need Call from Views.py(Todo List Application).
1. in views.py (Todo List Application) ```from .models import Todo```
2. in views.py (Todo List Application) call all items ```items = Todo.objects.all()```
3. in views.py (Todo List Application) added value for bring in templates ```{'items': items}```
4. in templates create looping for items in the form of <li>
5. setting items with descending with ```order by -id```
6. setting in templates ```selected``` so as every request link can match in Templates(selected) and views.py(path) "INDICATOR"

========== FORM and POST request ==========

---DELETE items
1. in views.py (Todo List Application) 
    - Button delete require id items
    - we change delete link in Templates with ```item.id```
2. We don't need to visit link delete, just only still in ALL link
3. in views.py (Todo List Application) 
    - Get ```todo = Todo.objects.get(id=id)```
    - Delete ```todo.delete()```
4. We need "Error Handling", if```id```getting nothing is mean = nothing data in database then will be an ERROR
    - Import django exceptions object does not exist in views.py (Todo List Application)
    - If Error ```ObjectDoesNotExist```, we must direct to (index/ALL) ```from django.http import HttpResponse``` with return ```return HttpResponseRedirect('/todo/')```
    - Use```reverse```in views.py(Todo List Application) with path urls.py(Todo List Application) so that keep direct to (index/ALL) ```return HttpResponseRedirect(reverse('index'))```

---CREATE items
1. in Templates(Todo List Application) 
    - Setting Templates under header, create FORM for Create Items(new-todo)
    - Protect FORM with ```{% csrf_token %}``` 
2. in views.py(Todo List Application) 
    - Redirect to index(/todo) ```return HttpResponseRedirect(reverse('index'))```
    - GET DATA INPUT(Handle data input) ```title = request.POST['title']```
    - Error Handling ```Try Except```
    - SAVE DATA INPUT ```todo = Todo(title=title)``` ```todo.save()```

---DELETE ALL items 
1. in views.py(Todo List Application)
    - GET ALL database and DELETE ```Todo.objects.all().delete()```
    - Redirect to index(/todo)

---Update items (Status Items)
1. in Templates(Todo List Application) 
    - Create Form
    - Protect FORM with ```{% csrf_token %}```
2. Need Submit with javascript ``` onclick="this.form.submit()" ```
    - Mean submit for just This Form, not another FORM
3. Check Output: must be to url /update
4. Redirect to index(/todo) ```return HttpResponseRedirect(reverse('index'))```
5. Error Handling ```Try Except```
    - Status Uncheck(Pending) <-> Status Check(Not Pending) ``` todo.status = not todo.status ```
    - save ``` todo.save() ```