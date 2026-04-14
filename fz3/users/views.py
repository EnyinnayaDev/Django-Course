from django.shortcuts import render
from django.http import HttpResponse
def users_home(request):
    return HttpResponse("<h1>This is the users page.</h1>")

# Create your views here.
