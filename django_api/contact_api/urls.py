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


    # ex: /contact_api/api_index/
    path('api_index/', views.api_index, name='api_index'),
    # ex: /contact_api/1/api_show/
    path('<int:contact_id>/api_show/', views.api_show, name='api_show'),
    # ex: /api_post/
    path('api_post/', views.api_post, name='api_post'),
    # ex: /api_edit/
    path('<int:contact_id>/api_edit/', views.api_edit, name='api_edit'),
    # ex: /api_delete/
    path('<int:contact_id>/api_delete/', views.api_delete, name='api_delete'),
    # ex: /api_list/
    path('api_list/', views.api_list, name='api_list'),
]
