from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.


def index(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {
        'contacts': contacts
    })


def add_contact(request):
    if request.method == 'POST':
        data = request.POST
        new_contact = Contact(
            full_name=data.get('fullname'),
            relationship=data.get('relationship'),
            email=data.get('email'),
            phone_number=data.get('phone-number'),
            address=data.get('address')
        )
        new_contact.save()

        return redirect('/')

    return render(request, 'new.html')


def contact_profile(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contact-profile.html', {
        'contact': contact
    })
