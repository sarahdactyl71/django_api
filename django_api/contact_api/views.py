import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render, redirect
from .models import Contact, ContactsForm
from django.conf import settings

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


#VIEWS FOR API ENDPOINTS

from django.http import JsonResponse

@csrf_exempt
def api_index(request):
    contacts = Contact.objects.all().values()
    return JsonResponse({'contacts': list(contacts)})

@csrf_exempt
def api_show(request, contact_id):
    contact = Contact.objects.filter(pk=contact_id).values()
    return JsonResponse({'contact': list(contact)})

@csrf_exempt
def api_post(request):
    creds = get_user_creds(request)
    if creds['username'] == settings.ALLOWED_USER and creds['password'] == settings.ALLOWED_PASS:
        info = parse_json_for_data(request)
        # import code; code.interact(local=dict(globals(), **locals()))
        contact = Contact(full_name = info['full_name'],
                          email = info['email'],
                          address = info['address'],
                          phone = info['phone'],
                          last_edited_by = creds['username'])
        contact.save()
        saved_contact = Contact.objects.filter(pk=contact.id).values()
        return JsonResponse({'contact': list(saved_contact)})
    else:
        return HttpResponse("Not Authorized to access this endpoint")

@csrf_exempt
def api_edit(request, contact_id):
    creds = get_user_creds(request)
    if creds['username'] == settings.ALLOWED_USER and creds['password'] == settings.ALLOWED_PASS:
        contact = Contact.objects.filter(pk=contact_id).values()
        info = parse_json_for_data(request)
        contact.update(full_name = info['full_name'],
                       email = info['email'],
                       address = info['address'],
                       phone = info['phone'],
                       last_edited_by = creds['username'])
        return JsonResponse({'contact': list(contact)})
    else:
        return HttpResponse("Not Authorized to access this endpoint")

@csrf_exempt
def api_delete(request, contact_id):
    creds = get_user_creds(request)
    if creds['username'] == settings.ALLOWED_USER and creds['password'] == settings.ALLOWED_PASS:
        contact = Contact.objects.filter(pk=contact_id)
        contact.delete()
        return HttpResponse("Contact has been deleted.")
    else:
        return HttpResponse("Not Authorized to access this endpoint")

@csrf_exempt
def api_list(request):
    r = json.loads(request.body)
    email = r['email']
    contacts = Contact.objects.filter(email__startswith=email).values()
    return JsonResponse({'contacts': list(contacts)})

#Helper methods

def parse_json_for_data(request):
    r = json.loads(request.body)
    full_name = r['full_name']
    email = r['email']
    address = r['address']
    phone = r['phone']
    return {'full_name': full_name, 'email': email, 'address': address, 'phone': phone}

def get_user_creds(request):
    username = request.META['HTTP_USERNAME']
    password = request.META['HTTP_PASSWORD']
    return {'username' : username, 'password': password}
