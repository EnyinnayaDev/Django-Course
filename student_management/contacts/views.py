from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
# Create your views here.

def contact_view(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data['name']
            messages.success(request, f"Thank you {name} for your message. We will get back to you soon.")
            return redirect('contact')
        else:
            print(form.errors)
            
    return render(request, 'contacts/contact.html', {'form': form})