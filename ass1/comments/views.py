from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def comm_home(request):
    return HttpResponse('<h1 style="color:blue">This is the comments view</h1>')
