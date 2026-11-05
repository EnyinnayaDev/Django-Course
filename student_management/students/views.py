from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib import messages
from .forms import StudentForm

# Create your views here.
@login_required
def student_list(request):
    students = Student.objects.all()

    return render(request, 'students/student_list.html', {'students': students})


#CREATE
@login_required
@permission_required('students.add_student', raise_exception=True)
def student_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        level = request.POST.get('level')
        
        student = Student(
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        age=age,
                        level=level
                    )
        
        # add validation for first_name and last_name
        def is_name_valid(name):
            name = name.strip()
            if name == "":
                return False
            if len(name) > 50:
                return False
            return True
            
        if not is_name_valid(first_name):
            error_message = "First name cannot be empty or longer than 50 characters."
            return render(request, 'students/student_form.html', {'error_message': error_message, 'student': student})
        student.first_name = first_name.strip()
        if not is_name_valid(last_name):
            error_message = "Last name cannot be empty or longer than 50 characters."
            return render(request, 'students/student_form.html', {'error_message': error_message, 'student': student})
        student.last_name = last_name.strip()
        # add validation for age
        try:
            age = int(age)
        except ValueError:
            error_message = "Age must be a number."
            return render(request, 'students/student_form.html', {'error_message': error_message, 'student': student})
        
        if age < 1 or age > 120:
            error_message = "Age must be between 1 and 120."
            return render(request, 'students/student_form.html', {'error_message': error_message, 'student': student})
        student.age = age
        
        # add validation for level
        try:
            level = int(level)
        except ValueError:
            error_message = "Level must be a number."
            return render(request, 'students/student_form.html', {'error_message': error_message, 'student': student})
        
        levels = [100, 200, 300, 400, 500]
        if level not in levels:
            error_message = "Level must be one of the following: 100, 200, 300, 400, 500."
            return render(request, 'students/student_form.html', {'error_message': error_message, 'student': student})
        student.level = level

        # add validation for email
        try:
            validate_email(email)
        except ValidationError:
            error_message = "Invalid email address."
            return render(request, 'students/student_form.html', {'error_message': error_message, 'student': student})
        student.email = email
        if Student.objects.filter(email=email).exists():
            error_message = "A student with this email already exists."
            return render(request, 'students/student_form.html', {'error_message': error_message, 'student': student})
        else:
            student.save()
            return redirect('student_list')

    return render(request, 'students/student_form.html')

#UPDATE
@login_required
@permission_required('students.change_student', raise_exception=True)
def student_update(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.level = request.POST.get('level')

        student.save()
        return redirect('student_list')

    return render(request, 'students/student_form.html', {'student': student})

#DELETE
@login_required
@permission_required('students.delete_student', raise_exception=True)
def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})



#Model Forms
@login_required
@permission_required('students.add_student', raise_exception=True)
def student_create_model_form(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request, 'students/student_model_form.html', {'form': form})

@login_required
@permission_required('students.change_student', raise_exception=True)
def student_update_model_form(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    return render(request, 'students/student_model_form.html', {'form': form, "student": student})

# Login function
def user_login(request):
    if request.method == 'POST':
        usernames = request.POST.get('username')
        passwords = request.POST.get('password')
          
        user = authenticate(
            username=usernames,
            password=passwords
        )
        print("Authenticated: ", user)
        if user is not None:
            login(request, user)
            page = request.GET.get('next')
            if page and url_has_allowed_host_and_scheme(page, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
                return redirect(page)
            else:
                return redirect('student_list')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'registration/login.html')

# Logout function
@login_required
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'registration/logout.html')

def is_authenticated(request):
    return HttpResponse(request.user.is_authenticated)

# User Reg Function
def user_register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'registration/register.html', {'form': form})