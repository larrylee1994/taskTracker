from django.shortcuts import render
from .models import Worksheet
from django.utils import timezone
from django.http import HttpResponseRedirect



def home(response):

    if response.method == "POST":
        first_name = response.user.first_name
        worksheet = Worksheet(name=first_name)
        worksheet.save()
        response.user.worksheet.add(worksheet)

        return HttpResponseRedirect("tracker/%i" % worksheet.id)
    else:
        pass

    return render(response, 'home.html')


def dashboard(response):
    ws = Worksheet.objects.all()

    return render(response, 'dashboard.html', {"ws": ws})

# TODO: abstract tracker function into its own view
# TODO: global variables or object for variables

def user_tracker(response, id):

    # TODO: properly catch this specific expeption
    try:
        ws = Worksheet.objects.get(id=id)
    except:
        return HttpResponseRedirect('/')
    
    
    view_flag = False

    # Only continue if worksheet belongs to user
    if ws in response.user.worksheet.all():
        view_flag = True
    
    # Or continue if user is superuser
    if response.user.is_superuser:
        view_flag = True
    
    if (view_flag):

        response.session['ws'] = id

        last_entry = len(ws.entry_set.all())
        if response.method == "POST":
            if response.POST.get("start_new"):
                if (last_entry == 0):
                    # Create first entry
                    entry = ws.entry_set.create()
                    entry.start_time = timezone.now()
                    entry.store = response.POST.get("store_list")
                    entry.operation = response.POST.get("operation_list")
                    entry.save()
                else:
                    # Update lastest end time to now
                    # DEMO
                    entry = ws.entry_set.last()
                    if (entry.end_time == None):
                        entry.end_time = timezone.now()
                    entry.save()

                    # Create next entry
                    new_entry = ws.entry_set.create()
                    new_entry.start_time = timezone.now()
                    new_entry.store = response.POST.get("store_list")
                    new_entry.operation = response.POST.get("operation_list")
                    new_entry.save()

            elif response.POST.get("delete"):

                if (last_entry > 0):
                    entry = ws.entry_set.last()
                    entry.delete()

            elif response.POST.get("complete"):
                # Update lastest end time to now
                entry = ws.entry_set.last()
                if (entry.end_time == None):
                    entry.end_time = timezone.now()
                    entry.save()

        return render(response, 'tracker.html', {"ws": ws})
    return render(response, "worksheets.html", {"ws": ws})


def worksheets(response):
    return render(response, "worksheets.html", {})
