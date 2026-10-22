from django.shortcuts import render
from .forms import ContactForm
# Create your views here.

def contact_view(request):
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print(form.errors)
            
    return render(request, 'contacts/contact.html', {'form': form})