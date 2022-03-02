from django.db import models
from django.utils import timezone

# Create your models here.
# represents each item on the to do list

class Items(models.Model): 
    title = models.CharField(max_length=250, default="Create Task")    
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    
    class Meta:
        ordering = ["-created"] 
    
    def __str__(self):
        return self.title