from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, "dashboard.html", {"page_name":"Dasboard",})
def profile(request):
    return render(request, "profile.html", {"page_name":"Profile"})
def settings(request):
    return render(request, "settings.html", {"page_name":"Settings"})
def helps(request):
    return render(request, "help.html", {"page_name":"Help"})