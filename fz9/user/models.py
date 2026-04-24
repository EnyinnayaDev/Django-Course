from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=10, unique=True, help_text="Enter a unique article title", verbose_name="Article title")
    slug = models.SlugField(max_length=100, unique=True, editable=True)
    content = models.TextField(blank=True, null=True, default="No content provided")
    category = models.CharField(max_length=20, choices=[('health', 'Health'),('tech', 'Tech'), ('life', 'Lifestyle'), ('news', 'news')], default='tech')
    published_date = models.DateField()
    reference_code = models.CharField(max_length=20, unique_for_date='published_date')
    id = models.AutoField(primary_key=True)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    
    def __str__(self):
        return str(self.user)
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"'{self.title}'` written by {self.author}"
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    student = models.ManyToManyField(Student)
    
    def __str__(self):
        return str(self.title)