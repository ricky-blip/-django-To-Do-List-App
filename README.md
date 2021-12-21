# Project Website Using Django

DOCS :

========== Setup Project & App ==========
1. Make sure install Python
2. Install PIP
3. Create Virtual Environment
4. install Package Django "PIP install django"
5. Create Project ( **WEBSITE** ) "django-admin startproject website"
6. Check Django server 
7. Running database migration
8. Running Django Server "./manage.py runserver"
9. Create App ( TODO LIST ) "./manage.py startapp todo"

========== Setting Urls & Views ==========

Connect Todo List Application to server 
1. in views.py Create function index for request Response Http
2. Create file urls.py
3. in urls.py Create "urlpatterns" and import file views.py
4. views.py and urls.py in (Todo List Application) supposed to be conected
5. Connect to (Project Website)urls.py
6. in urls.py(Project Website), Import urls.py(Todo List Application)
7. Running Django Server "./manage.py runserver" 
8. urls/(Todo List Application)

========== Setting Templates & Static Files ==========

Templates (file .html)
static    (file .css .js)
1. You need template and static file, you can download from internet or you can build you're own.
2. File templates you can put inside folder "templates/todo/(yourfileTemplate)" in you're (Todo List Application)
3. in views.py(Todo List Application), you need change to request render with you're templates file
4. in setting.py(Project Website) you need register you're template file in |INSTALLED_APPS|    
5. File static you can put inside folder "static/todo/css/(yourfileTemplate)" in you're (Todo List Application)
6. in setting.py(Project Website) you will find |STATIC_URL = 'static/'|
7. We need call static file in templates file with (Template static --> {% load static %}) for setting static file in templates files
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
