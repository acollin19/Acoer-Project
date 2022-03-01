from django.db import models
from django.utils import timezone

# Create your models here.
# represents each item on the to do list

class Items(models.Model): #Todolist able name that inherits models.Model
    title = models.CharField(max_length=250, default="Create Task")    
    content = models.TextField(blank=True) # a text field 
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date

    class Meta:
        ordering = ["-created"] #ordering by the created field
    
    def __str__(self):
        return self.title