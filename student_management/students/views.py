from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.core.validators import validate_email

# Create your views here.
def student_list(request):
    students = Student.objects.all()

    return render(request, 'students/student_list.html', {'students': students})


#CREATE
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
def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
