from django.urls import path

from . import views

urlpatterns = [
    # ex: /contact_api/
    path('', views.index, name='index'),
    # ex: /contact_api/5/
    path('<int:contact_id>/', views.detail, name='detail'),
    # ex: /contact_api/5/results/
    path('<int:contact_id>/results/', views.results, name='results'),
]
