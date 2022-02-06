from django.contrib import admin

from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','title','status')

# register link        
admin.site.register(Todo,TodoAdmin)
admin.site.site_url = '..' # meaning URL from page admin(view site) direct to apps(todo)