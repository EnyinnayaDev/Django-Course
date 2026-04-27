from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
    EmailValidator,
    URLValidator,
    validate_slug,
    validate_email,
    FileExtensionValidator
)

# Create your models here.
# Custom
def custom_vald(value):
    if value % 2 != 0:
        raise ValidationError(f"{value} is not an even number.")
   
def validate_alpha(value):
    if not value.isalpha():
        raise ValidationError("Only alphabetic characters are allowed")
    
def starts_with(value):
    if not value.startswith("Paschal"):
        raise ValidationError("Value must start with 'Paschal'.") 
    
def prohibited_words(value):
    banned = ['admin', 'root', 'staff']
    if value.lower() in banned:
        raise ValidationError(f"'{value}' is not alowed as input.")
    
def file_size(value):
    filesize = value.size
    if filesize > 5 * 1024 * 1024:  # 5MB
        raise ValidationError("File size must be under 5MB")
    
class ValidatorDemo(models.Model):
    # 1. Minimum Value(e.g., must be >= 10)
    min_value = models.IntegerField(
        validators=[MinValueValidator(10), custom_vald],
        help_text="Must be an even number and greater than or equal to 10"
    )
    
    # 2. Maximum Value(e.g., must be <= 100)
    max_value = models.IntegerField(
        validators=[MaxValueValidator(100)],
        help_text="Must be less than or equal to 100"
    )
    
    # 3. Regex(e.g., only allow letters, 3-10 characters)
    username = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]{3,10}$',
                message='Username must be 3-10 letters only'
            ),
            starts_with
        ]
    )
    
    # 4. Email Validator
    email = models.CharField(
        max_length=100,
        validators=[EmailValidator(message="Enter a valid email address")]
    )
    
    # 5. URL Validator
    website = models.URLField(
        validators=[URLValidator(message= "Enter a valid URL")]
    )
    
    # 6. Multiple Validators on One Field
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        help_text="Enter a rating between 1 and 5"
    )
    
    # 7. Slug Field with Vlaidator
    slug = models.SlugField(
        validators=[validate_slug],
        help_text="Only letters numbers, underscore or hyphens"
    )
    
    # 8. Custom Email Field with validate_email
    another_email = models.EmailField(
        validators=[validate_email],
        help_text="A second email field using validate_email"
    )
    
    # 9. File extension validator (e.g., only PDF or DOCX)
    resume = models.FileField(
        upload_to='resumes/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx']), file_size],
        blank=True,
        null=True,
        help_text="Upload a .pdf or .docx file"
    )
    
    def __str__(self):
        return f"{self.username} - {self.email}"