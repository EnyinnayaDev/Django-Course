from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

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
        
        try:
            age = int(age)
        except ValueError:
            error_message = "Age must be a number."
            return render(request, 'students/student_form.html', {'error_message': error_message, 'student': student})
        
        if age < 1 or age > 120:
            error_message = "Age must be between 1 and 120."
            return render(request, 'students/student_form.html', {'error_message': error_message, 'student': student})
        student.age = age
        
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
