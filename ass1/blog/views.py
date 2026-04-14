from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def blog_home(request):
    return HttpResponse('<h1 style="color:blue">This is the blog view</h1>')