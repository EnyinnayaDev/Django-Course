from django.urls import path
from .views import *

urlpatterns = [
    path("", student_list, name="student_list"),
    path("create/", student_create, name="student_create"),
    path("students/<int:student_id>/update/", student_update, name="student_update"),
]