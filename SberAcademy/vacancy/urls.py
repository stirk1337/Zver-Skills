from django.urls import path
from . import views

urlpatterns = [
    path('browse', views.browse),
    path('get_vacancies', views.get_vacancies)
]