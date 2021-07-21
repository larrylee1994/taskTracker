from django.shortcuts import render
from .models import Worksheet, Entry, User
from .forms import CreateNewWorksheet
from django.http import HttpResponseRedirect

def home(response):

    if response.method == "POST":
        form = CreateNewWorksheet(response.POST)

        if form.is_valid():
            t = Worksheet(
                # name=form.cleaned_data["name"],
                date=form.cleaned_data["date"],
            )
            t.save()

        return HttpResponseRedirect("tracker/%i" %t.id)
    else:
        form = CreateNewWorksheet()

    return render(response, 'home.html', {"form": form})

def register(response):
    return render(response, 'register.html')

def sign_in(response):
    return render(response, 'sign_in.html')

def dashboard(response):
    return render(response, 'dashboard.html')

def user_tracker(response, id):
    ws = Worksheet.objects.get(id=id)
    return render(response, 'tracker.html', {"ws": ws})

