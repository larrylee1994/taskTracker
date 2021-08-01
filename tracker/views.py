from django.shortcuts import render
from main.models import Worksheet
from django.utils import timezone
from django.http import HttpResponseRedirect

def tracker(response, id):

    try:
        ws = Worksheet.objects.get(id=id)
    except (Worksheet.DoesNotExist, AttributeError) as e:
        print(e)
        # TODO: create page: doesn't exist page or message
        return HttpResponseRedirect('/')
    
    # Check if user can view page
    if (get_view_flag(response, ws)):

        response.session['ws'] = id
        
        if response.method == "POST":
            entry_len = len(ws.entry_set.all())
   
            if response.POST.get("start_new"):
                update_last_entry(response, ws, entry_len)
                create_new_entry(response, ws)

            elif response.POST.get("delete"):
                delete_last_entry(ws, entry_len)

            elif response.POST.get("complete"):
                update_last_entry(response, ws, entry_len)

        # reload page with updated values
        return render(response, 'tracker/tracker.html', {"ws": ws})
    
    # go to worksheet page if user cannot view page
    return render(response, "worksheets.html", {"ws": ws})

def create_new_entry(response, ws):
    entry = ws.entry_set.create(
        start_time=timezone.now(),
        store=response.POST.get("store_list"),
        operation=response.POST.get("operation_list"),
    )
    entry.save()

def update_last_entry(response, ws, entry_len):
    # Set lastest end time to now
    if (entry_len > 0):
        entry = ws.entry_set.last()
        if (entry.end_time == None):
            entry.end_time = timezone.now()
        entry.save()

def delete_last_entry(ws, entry_len):
    if (entry_len > 0):
        entry = ws.entry_set.last()
        entry.delete()
    pass

def get_view_flag(response, ws):

    # Continue if user is superuser
    if response.user.is_superuser:
        return True

    # Continue if worksheet belongs to user
    if ws in response.user.worksheet.all():
        return True
    
    return False