from django.urls import path

from . import views

app_name = 'contact_api'
urlpatterns = [
    # ex: /contact_api/
    path('', views.index, name='index'),
    # ex: /contact_api/create
    path('create/', views.create, name='create'),
    # ex: /contact_api/update
    path('<int:contact_id>/update/', views.update, name='update'),
    # ex: /contact_api/delete
    path('<int:contact_id>/delete/', views.delete, name='delete'),
    # ex: /contact_api/5/
    path('<int:contact_id>/', views.show, name='show'),


    # ex: /contact_api/get_all_contacts/
    path('get_all_contacts/', views.get_all_contacts, name='get_all_contacts'),
    # ex: /contact_api/1/get_a_contact/
    path('<int:contact_id>/get_a_contact/', views.get_a_contact, name='get_a_contact'),
    # ex: /api_post/
    path('api_post/', views.api_post, name='api_post'),
    # ex: /api_edit/
    path('<int:contact_id>/api_edit/', views.api_edit, name='api_edit'),
]
