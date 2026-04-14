from django.shortcuts import render
from django.http import HttpResponse

def store_view(request):
    return HttpResponse("This is th storre view")
