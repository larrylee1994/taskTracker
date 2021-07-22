from django.shortcuts import render
from .models import Worksheet, Entry, User
from .forms import CreateNewWorksheet
from django.http import HttpResponseRedirect
from django.utils import timezone

def home(response):

    if response.method == "POST":
        form = CreateNewWorksheet(response.POST)

        if form.is_valid():
            d = form.cleaned_data["date"]
            worksheet = Worksheet(
                # name=form.cleaned_data["name"],
                date=d,
            )
            worksheet.save()
            entry = worksheet.entry_set.create()
            entry.store = 116
            entry.operation = "PROC"
            entry.save()
            

        return HttpResponseRedirect("tracker/%i" %worksheet.id)
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
    last_entry = len(ws.entry_set.all())
    print(last_entry)
    if response.method == "POST":
        if response.POST.get("end_entry"):
            entry = ws.entry_set.order_by('start_time')[last_entry - 1]
            print(entry)
            entry.end_time = timezone.now()
            entry.save()

        elif response.POST.get("start_entry"):
            entry = ws.entry_set.create()
            entry.store = 116
            entry.operation = "PROC"
            entry.save()
            
        elif response.POST.get("complete_worksheet"):
            pass

        pass
    return render(response, 'tracker.html', {"ws": ws})

