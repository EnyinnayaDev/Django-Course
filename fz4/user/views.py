from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "theme": "Project template",
        "name": "Enyinnaya",
        "age": 18
    }
    return render(request, 'base.html', context)

def home2(request):
    context = {
        "theme": "App template",
        "name": "Paschal"
    }
    return render(request, 'user/index.html', context)
