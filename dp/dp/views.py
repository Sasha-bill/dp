from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse
from .models import UserModel


def index(request):
    if request.method == "POST":

        #data = request.POST.get("data")
        UserModel.objects.create(data=request.POST.get("data"))
        userdata = UserModel.objects.all()

        return HttpResponse("<h3>  JSON OUTPUT:  {0}   </h3>".format(userdata))
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})
