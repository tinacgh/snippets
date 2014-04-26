from datetime import datetime
from django.db import models

# Create your models here.
class Snippet(models.Model):
    date = models.DateTimeField(default=datetime.now)
    description = models.CharField(max_length=200)
    files = models.CharField(max_length=200, blank=True)
    link = models.CharField(max_length=200, blank=True)
    extra = models.CharField(max_length=200, blank=True)
    code = models.TextField()
    
    def __str__(self):
        return self.description
