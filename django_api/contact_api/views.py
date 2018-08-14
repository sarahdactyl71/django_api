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

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

def detail(request, contact_id):
    try:
        contact = Contact.objects.get(pk=contact_id)
    except Contact.DoesNotExist:
        raise Http404("Contact does not exist")
    return render(request, 'contact_api/detail.html', {'contact': contact})

def results(request, contact_id):
    response = "You're looking at the results of contact %s."
    return HttpResponse(response % contact_id)
