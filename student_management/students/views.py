from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def student_list(request):
    students = Student.objects.all()

    return render(request, 'students/student_list.html', {'students': students})



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
        student.save()
        return redirect('student_list')
    else:
        pass

    return render(request, 'students/student_form.html')

def student_update(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.level = request.POST.get('level')

        student.save()
        return redirect('student_list')

    return render(request, 'students/student_form.html', {'student': student})