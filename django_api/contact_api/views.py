# from django.shortcuts import render
#
# # Create your views here.

from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render, redirect

from django.forms import ModelForm

from .models import Contact

class ContactsForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'address', 'phone']

def index(request):
    latest_contact_list = Contact.objects.order_by('-full_name')
    context = {'latest_contact_list': latest_contact_list}
    return render(request, 'contact_api/index.html', context)

def show(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'contact_api/show.html', {'contact': contact})

def create(request, template_name='contact_api/contact_form.html'):
    form = ContactsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contact_api:index')
    return render(request, template_name, {'form': form})

def update(request, contact_id, template_name='contact_api/contact_form.html'):
    contact = get_object_or_404(Contact, pk=contact_id)
    form = ContactsForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('contact_api:index')
    return render(request, template_name, {'form': form})

def delete(request, contact_id, template_name='contact_api/contact_delete.html'):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method=='POST':
        contact.delete()
        return redirect('contact_api:index')
    return render(request, template_name, {'contact': contact})


#playing around with JsonResponse

from django.http import JsonResponse

def get_all_contacts(request):
    contacts = Contact.objects.all().values()
    return JsonResponse({'contacts': list(contacts)})

def get_a_contact(request, contact_id):
    contact = Contact.objects.filter(pk=contact_id).values()
    return JsonResponse({'contact': list(contact)})

def create_a_contact(request):
    r = requests.post('http://localhost:8000/contact_api/create/', data = {'key':'value'})
    contact = Contact.objects.all()
    return JsonResponse({'contact': list(contact)})

def edit_a_contact(request, contact_id):
    contact = Contact.objects.filter(pk=contact_id).values()
    return JsonResponse({'contact': list(contact)})

def delete_a_contact(request, contact_id):
    contact = Contact.objects.filter(pk=contact_id).values()
    return JsonResponse({'contact': list(contact)})

def get_lists_of_contacts(request, full_name=None):
    contacts = Contact.objects.filter(full_name__startswith=full_name).values()
    return JsonResponse({'contacts': list(contacts)})
