from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse

def index(request):
    if request.method == "POST":

        name = request.POST.get("name")     # получение значения поля name
        data = request.POST.get("data")     # получение значения поля data
        return HttpResponse("<h2>Name: {1}        JSON:{0}</h2>".format(data, name))
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})