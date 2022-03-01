from django.shortcuts import render, redirect
from .models import Items



# Create your views here.
def index(request):
    all_items = Items.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            content = title + " -- " + date #content
            s = Items(title=title, content=content)
            s.save() #saving the todo 
            return redirect("/") #reloading the page
        
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            y = Items.objects.get(id=checkedlist) #getting todo id
            y.delete()
            
            #for i in checkedlist:
            #    toDelete = Items.objects.get(id=int(i)) #getting todo id
            #    toDelete.delete() #deleting todo
        
    return render(request, "index.html", {"all_items": all_items})

'''
def addItems(request):
    x = request.POST['content']
    new_item = Items(content = x)
    new_item.save()
    return HttpResponseRedirect('/list/')

def deleteItems(request, i):
    y = Items.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/list/')
'''