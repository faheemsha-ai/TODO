from django.shortcuts import render, redirect
from . models import Todo
from . forms import TodoForm

def index(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            form = TodoForm()
            return redirect("/")
    pro = Todo.objects.all()
    return render(request,"index.html",{"form": form , "pro":pro})
def update(request,id):
    data=Todo.objects.get(id=id)
    form=TodoForm(instance=data)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,"update.html",{"form":form})
def delete(request,id):
    data=Todo.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect("/")
    return redirect("/")