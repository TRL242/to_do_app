from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)
