from django.shortcuts import get_object_or_404, render,redirect
from .forms import ContactForm
from .models import Contact

def view1(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def contact_list_view(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def delete_contact_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'delete_confirm.html', {'contact': contact})