# from django.shortcuts import render
#
# # Create your views here.

from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render

from .models import Contact

def index(request):
    latest_contact_list = Contact.objects.order_by('-email')[:5]
    context = {'latest_contact_list': latest_contact_list}
    return render(request, 'contact_api/index.html', context)

def detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'contact_api/detail.html', {'contact': contact})

def results(request, contact_id):
    response = "You're looking at the results of contact %s."
    return HttpResponse(response % contact_id)


#playing around with JsonResponse

from django.http import JsonResponse

def get_all_contacts(request):
    contacts = Contact.objects.all()
    return JsonResponse({'contacts': contacts})

def get_a_contact(request, contact_id):
    contact = Contact.objects.filter(id=contact_id)
    return JsonResponse({'contact': contact})

def create_a_contact(request):
    questions = Question.objects.all()
    return JsonResponse({'questions': questions})

def edit_a_contact(request):
    questions = Question.objects.all()
    return JsonResponse({'questions': questions})

def delete_a_contact(request):
    questions = Question.objects.all()
    return JsonResponse({'questions': questions})

def get_lists_of_contacts(request):
    Question.objects.filter(question_text__startswith='What')
    return JsonResponse({'questions': questions})
