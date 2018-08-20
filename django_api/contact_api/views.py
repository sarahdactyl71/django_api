# from django.shortcuts import render
#
# # Create your views here.

from django.http import HttpResponse

import json

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import get_object_or_404, render, redirect

from django.forms import ModelForm

from .models import Contact

from django.contrib.auth import authenticate, login, logout

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('contact_api:index')
        else:
            HttpResponse("Sorry, that account has been disabled")
    else:
        HttpResponse("Invalid Login Creds")

def logout_view(request):
    logout(request)
    return redirect('contact_api:login')

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

@csrf_exempt
def api_post(request):
    r = json.loads(request.body)
    full_name = r['full_name']
    email = r['email']
    address = r['address']
    phone = r['phone']
    # check for validation, uniqueness, contacts with same name, phone numbers beyond numbers etc.
    contact = Contact(full_name = full_name, email = email, address = address, phone = phone)
    contact.save()
    saved_contact = Contact.objects.filter(pk=contact.id).values()
    return JsonResponse({'contact': list(saved_contact)})

@csrf_exempt
def api_edit(request, contact_id):
    contact = Contact.objects.filter(pk=contact_id).values()
    r = json.loads(request.body)
    full_name = r['full_name']
    email = r['email']
    address = r['address']
    phone = r['phone']
    contact.update(full_name = full_name, email = email, address = address, phone = phone)
    return JsonResponse({'contact': list(contact)})

@csrf_exempt
def api_delete(request, contact_id):
    contact = Contact.objects.filter(pk=contact_id)
    contact.delete()
    return JsonResponse({'contact': list(contact)})

@csrf_exempt
def api_list(request):
    r = json.loads(request.body)
    email = r['email']
    contacts = Contact.objects.filter(email__startswith=email).values()
    return JsonResponse({'contacts': list(contacts)})
