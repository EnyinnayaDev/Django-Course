from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        name = name.strip()# Remove leading and trailing whitespace
        symbols = "-'"
        if len(name) < 2:
            raise ValidationError("Name must be at least 2 characters long.")
        for char in name:
            if char.isdigit():
                raise ValidationError("Name must be a letter, no numbers")
            if not char.isalpha() and char not in symbols:
                raise ValidationError("Name must be a letter, no symbols")
        return name
    
    def clean(self):
        cleaned_data = super().clean()
        message = cleaned_data.get('message')
        email = cleaned_data.get('email')
        if message is not None and len(message) < 10:
            self.add_error("message", "Message must be at least 10 characters long.")
        if email is not None and message is not None and email.lower() in message.lower():
            self.add_error("message", "Message cannot contain the email address.")  
        if message is not None:
            message = message.split()
            for word in message:
                if len(word) >= 5:
                    break
            else:
                self.add_error("message", "Message must contain at least one word with 5 or more characters.")
        return cleaned_data