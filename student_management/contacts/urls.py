from django.urls import path
from .views import contact_view


urlpatterns = [
    path("", name="contact", view=contact_view),
]
