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
    path('get_all_contacts/', views.get_all_contacts, name='get_all_contacts'),
    path('<int:contact_id>/get_a_contact/', views.get_a_contact, name='get_a_contact'),
]
