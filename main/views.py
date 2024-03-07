from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    
    if response.method == "POST":
        if response.Post.get("save"):
            for item in ls.item_set.all(): # type: ignore
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False) # type: ignore
            else:
                print("invalid")

    return render(response, "list.html", {"ls":ls})

def home(response):
    return render(response, "home.html", {"name":"Test List"})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            return HttpResponseRedirect('/%i' %t.id) # type: ignore
    else:
            form = CreateNewList()
    return render(response, "create.html", {"form":form})