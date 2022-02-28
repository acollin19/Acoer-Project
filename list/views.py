from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Items

# Create your views here.
def todoList(request):
    all_items = Items.objects.all()
    return render(request, 'todolist.html', {'all_items': all_items})

def addItems(request):
    x = request.POST['content']
    new_item = Items(content = x)
    new_item.save()
    return HttpResponseRedirect('/list/')

def deleteItems(request, i):
    y = Items.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/list/')
