from django.urls import path

from . import views

app_name = 'contact_api'
urlpatterns = [
    # ex: /contact_api/
    path('', views.index, name='index'),
    # ex: /contact_api/5/
    path('<int:contact_id>/', views.detail, name='detail'),
    # ex: /contact_api/5/results/
    path('<int:contact_id>/results/', views.results, name='results'),
    # ex: /contact_api/get_all_contacts/
    path('get_all_contacts/', views.get_all_contacts, name='get_all_contacts'),
    # ex: /contact_api/1/get_a_contact/
    path('<int:contact_id>/get_a_contact/', views.get_a_contact, name='get_a_contact'),
    # ex: /contact_api/
    path(regex='get_lists_of_contacts/(?P<full_name>\w{1,50})/$', views.get_lists_of_contacts, name='get_lists_of_contacts'),
]
