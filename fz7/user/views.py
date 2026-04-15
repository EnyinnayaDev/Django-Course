from django.shortcuts import render
from django.http import HttpResponse
from .models import Students

# Create your views here.
students = Students.objects.all()
def home(request):
    return HttpResponse("""<h1>Hello, World! This is the home page.</h1>
                        <p>Here are the students:</p>
                        <ul>
                        """ + "".join([f"<li>{student.name} - Age: {student.age} - Level: {student.level}</li>" for student in students]) + """</ul>""")