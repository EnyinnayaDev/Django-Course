from django.urls import path
from .views import *

urlpatterns = [
    path("", student_list, name="student_list"),
    path("create/", student_create, name="student_create"),
    path("students/<int:student_id>/update/", student_update, name="student_update"),
    path("students/<int:student_id>/delete/", student_delete, name="student_delete"),
    path("students/<int:student_id>/model-form/update/", student_update_model_form, name="student_update_model_form"),
    path("students/model-form/create/", student_create_model_form, name="student_create_model_form")
]