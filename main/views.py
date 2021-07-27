from django.shortcuts import render
from .models import Worksheet, Entry
from .forms import CreateNewWorksheet
from django.utils import timezone
from django.http import HttpResponseRedirect, FileResponse
from django.core import serializers



def home(response):

    if response.method == "POST":
        form = CreateNewWorksheet(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            worksheet = Worksheet(name=n)
            worksheet.save()
            response.user.worksheet.add(worksheet)

        return HttpResponseRedirect("tracker/%i" % worksheet.id)
    else:
        form = CreateNewWorksheet()

    return render(response, 'home.html', {"form": form})


def dashboard(response):
    ws = Worksheet.objects.all()

    return render(response, 'dashboard.html', {"ws": ws})


def user_tracker(response, id):

    try:
        ws = Worksheet.objects.get(id=id)
    except:
        form = CreateNewWorksheet()
        return render(response, 'home.html', {"form": form})
    
    serialized_obj = serializers.serialize('json', [ ws, ])
    response.session['ws'] = serialized_obj

    if ws in response.user.worksheet.all():

        last_entry = len(ws.entry_set.all())
        if response.method == "POST":
            if response.POST.get("start_new"):
                if (last_entry == 0):
                    entry = ws.entry_set.create()
                    entry.store = response.POST.get("store_list")
                    entry.operation = response.POST.get("operation_list")
                    entry.save()
                else:
                    entry = ws.entry_set.order_by('start_time')[last_entry - 1]
                    entry.end_time = timezone.now()
                    entry.save()
                    new_entry = ws.entry_set.create()
                    new_entry.operation = response.POST.get("operation_list")
                    new_entry.store = response.POST.get("store_list")
                    new_entry.save()

            elif response.POST.get("delete"):
                # if delete on no entries, delete worksheet and return to home
                if (last_entry == 0):
                    # ws.delete()
                    # return HttpResponseRedirect("/")
                    pass
                else:
                    entry = ws.entry_set.order_by('start_time')[last_entry - 1]
                    entry.delete()
        return render(response, 'tracker.html', {"ws": ws})
    return render(response, "worksheets.html", {"ws": ws})


def worksheets(response):
    return render(response, "worksheets.html", {})
