from django.shortcuts import render, redirect
from .models import Items



# Create your views here.
def index(request):
    all_items = Items.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] 
            date = str(request.POST["date"]) 
            content = title + " -- " + date
            s = Items(title=title, content=content, due_date=date)
            s.save() 
            return redirect("/") #reloading page
        
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] 
            y = Items.objects.get(id=checkedlist)
            y.delete()
        else:
            return redirect("/")
        
            
    return render(request, "index.html", {"all_items": all_items})
