from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1==password2:
            if Student.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif Student.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = Student.objects.create_student(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('Username created')
                return redirect('register')
                
        else:
            messages.info(request,('password not matching'))
            return redirect('register')
        
    else:
        return render(request, 'user/index.html')
    