from django.urls import path
from . import views
urlpatterns = [
    path("dashboard/", views.dashboard, name='dashboard'),
    path("profile/", views.profile, name='profile'),
    path("settings/", views.settings, name='settings'),
    path("help/", views.helps, name='help'),
]