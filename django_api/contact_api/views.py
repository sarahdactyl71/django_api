# from django.shortcuts import render
#
# # Create your views here.

from django.http import HttpResponse

from django.shortcuts import render

from .models import Contact

def index(request):
    latest_contact_list = Contact.objects.order_by('-email')[:5]
    context = {'latest_contact_list': latest_contact_list}
    return render(request, 'contact_api/index.html', context)

def detail(request, contact_id):
    return HttpResponse("You're looking at contact %s." % contact_id)

def results(request, contact_id):
    response = "You're looking at the results of contact %s."
    return HttpResponse(response % contact_id)
