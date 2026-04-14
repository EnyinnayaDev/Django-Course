from django.shortcuts import render
from django.http import HttpResponse
def product_home(request):
    return HttpResponse("<h1>This is the product home page.</h1>")
# Create your views here.
