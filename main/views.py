from django.shortcuts import render

def home(response):
    if response.method == "POST":
        pass
    return render(response, 'home.html')

def register(response):
    return render(response, 'register.html')

def sign_in(response):
    return render(response, 'sign_in.html')

def dashboard(response):
    return render(response, 'dashboard.html')

def user_tracker(response):
    return render(response, 'tracker.html')

