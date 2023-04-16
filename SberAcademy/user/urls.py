from django.urls import path
from . import views

urlpatterns = [
    path('logout', views.logout_user),
    path('profile/<int:user_id>', views.profile),
    path('mentor_survey', views.mentor_survey),
    path('get_notifications', views.get_notifications),
    path('get_surveys', views.get_surveys),
    path('mentor_surveys', views.mentor_survey),
    path('delete_survey', views.delete_survey),
    path('accept_survey', views.accept_survey)
    
]