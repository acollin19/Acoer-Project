from django.contrib import admin
from . import models

# Register your models here.
class Admin(admin.ModelAdmin):
    display = ("title", "created", "due_date")
    
admin.site.register(models.Items, Admin)
