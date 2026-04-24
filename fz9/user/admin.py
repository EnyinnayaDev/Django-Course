from django.contrib import admin
from .models import Profile, Author, Book, Student, Course
# Register your models here.
admin.site.register(Profile)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Course)