from django.shortcuts import render
from django.http import HttpResponse
def cart_home(request):
    return HttpResponse("<h1>This is the cart home page.</h1>")

# Create your views here.
