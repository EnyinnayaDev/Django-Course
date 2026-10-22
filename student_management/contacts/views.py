from django.shortcuts import render
from .forms import ContactForm
# Create your views here.

def contact_view(request):
    form = ContactForm()
    success_message = ""
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data['name']
            success_message = f"Thank you {name} for your message. We will get back to you soon."
        else:
            print(form.errors)
            
    return render(request, 'contacts/contact.html', {'form': form, 'success_message': success_message})