from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.TextField(max_length=50) #title is field
    status = models.BooleanField(default=False) #status is field
    
    def __str__(self):
        return '%s: %s' % (self.id, self.title)
        
        