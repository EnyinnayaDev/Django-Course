from django.db import models
from django.core.validators import EmailValidator, validate_slug

# Create your models here.
class Student(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    UserName = models.CharField(max_length=20)
    email = models.CharField(max_length=100, validators=[EmailValidator(message='Enter a valid email')])
    Password1 = models.SlugField(validators=[validate_slug])
    Password2 = models.SlugField(validators=[validate_slug])
    
    def __str__(self):
        return str(self.UserName)