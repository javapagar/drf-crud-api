from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
