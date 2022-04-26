from django.db import models

# Create your models here.
class Todo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    todo = models.CharField(max_length=50, blank=False, default='')
    done = models.BooleanField(default=False)