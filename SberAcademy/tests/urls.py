from django.urls import path
from . import views

urlpatterns = [
    path('browse', views.browse),
    path('get_tests', views.get_tests_by_filter),
    path('get_tasks', views.get_tasks_by_filter)
    
]