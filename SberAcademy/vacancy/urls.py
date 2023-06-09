from django.urls import path
from . import views

urlpatterns = [
    path('browse', views.browse),
    path('get_vacancies', views.get_vacancies),
    path('test', views.test),
    path('start_test', views.start_test),
    path('complete_test', views.complete_test),
    path('test/<int:vacancy_id>', views.test),
    path('test_vac', views.test_vac)
]