from django.db import models

# Create your models here.
# represents each item on the to do list
class Items(models.Model):
    content = models.TextField()
