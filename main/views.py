from django.shortcuts import render
from .models import Worksheet
from django.http import HttpResponseRedirect



def home(response):

    if response.method == "POST":
        first = response.user.first_name
        last = response.user.last_name

        worksheet = Worksheet(name=f'{first} {last}')
        worksheet.save()
        response.user.worksheet.add(worksheet)

        return HttpResponseRedirect("tracker/%i/" % worksheet.id)
    else:
        pass

    return render(response, 'home.html')


def dashboard(response):
    # ws = Worksheet.objects.all()
    return render(response, 
    'dashboard.html', 
    # {"ws": ws}
    )

def worksheets(response):
    return render(response, "worksheets.html", {})
