from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

class ToDoItem(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        get_latest_by = 'created_at'
        
class ToDoHistory(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
