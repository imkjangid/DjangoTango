from django.shortcuts import render, redirect
from signals.forms import UserForm
from signals.models import Users

# Create your views here.
def index(request):
    print('index of signals called')
    users = Users.objects.using('signals').all()
    form = UserForm()
    
    return render(request, "home.html", {"form": form, "users": users})

def user_add(request):
    print('user add called')
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "home.html", {"form": form})

def edit(request, user_id):
    user = Users.objects.get(id=user_id)
    form = UserForm(instance=user)
    return render(request, "edit.html", {"form": form, "user": user})

def user_update(request, user_id):
    user = Users.objects.get(id=user_id)
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    return redirect("index")

def user_delete(request, user_id):
    user = Users.objects.get(id=user_id)
    if request.method == "GET":
        user.delete()
    return redirect("index")
