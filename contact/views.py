from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.


def index(request):
    contacts = Contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contact.objects.filter(full_name__icontains=search_input)

    return render(request, 'index.html', {
        'contacts': contacts,
        'search_input': search_input,
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


def edit_contact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == "POST":
        data = request.POST
        contact.full_name = data['fullname']
        contact.relationship = data['relationship']
        contact.email = data['email']
        contact.phone_number = data['phone-number']
        contact.address = data['address']
        contact.save()

        return redirect('/profile/' + str(contact.id))

    return render(request, 'edit.html', {
        'contact': contact
    })


def delete_contact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/')

    return render(request, 'delete.html', {
        'contact': contact
    })