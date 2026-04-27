from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    stds = Student.objects.get(id=1)
    f_name = stds.full_name()
    context = {
        'f_name':f_name
    }
    return render(request, "user/index.html", context)