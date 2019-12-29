from django.db import models
from django.db.models import Model

class ToDoItem(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        get_latest_by = 'created_at'
        
class ToDoHistory(models.Model):
    content = models.TextField()
