from django.urls import path
from . import views

urlpatterns = [
    path('browse', views.browse),
    path('browse_tests', views.browse_tests),
    path('get_tests', views.get_tests_by_filter),
    path('get_tasks', views.get_tasks_by_filter),
    path('get_test', views.get_test),
    path('complete_test', views.complete_test)
    
]