from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'age', 'level']
        labels = {
            'first_name': "Student's First Name",
            'email': "Student's Email Address"
        }
        help_texts = {
            'level': "Select your current academic level."
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name.'
            })
        }
        
    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 1 or age > 120:
            raise forms.ValidationError("Age should be between 1 and 120")
        return age
    
    def clean_level(self):
        level = self.cleaned_data['level']
        levels = [100, 200, 300, 400, 500]
        if level not in levels:
            raise forms.ValidationError("Invalid level")
        return level
    
    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get("age")
        level = cleaned_data.get("level")
        
        if age is not None and level is not None:
            if level == 100 and age < 16:
                self.add_error("age", "Students in level 100 must be at least 16 years old.")
        return cleaned_data