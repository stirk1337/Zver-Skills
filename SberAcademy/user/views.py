from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from vacancy.models import Vacancy, Survey, SkillResult
from tests.models import Test, Question
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
import random
import ast
from user.models import Notification
from django.contrib.auth.models import User

@login_required(login_url='/user/login/')
@cache_control(no_cache=True, must_revalidate=True)
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/user/login')

@login_required(login_url='/user/login/')
def profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user/profile.html', {'user': user})

def get_surveys(request):
    surveys = Survey.objects.all()
    surv = list(surveys.values())
    for i, vac in enumerate(surv):
        vac['name'] = User.objects.get(id=vac['user_id']).username
    return JsonResponse(surv, safe=False)

def delete_survey(request):
    survey = Survey.objects.get(id=request.GET.get('survey_id'))
    survey.delete()
    return HttpResponse('Успешно')

def mentor_survey(request):
    survey = Survey.objects.get(id=request.GET.get('survey_id'))
    user = User.objects.get(id=2)
    #print(user)
    notifi = Notification(user=user, message='Вам предложено менторство ' + survey.user)
    notifi.save()
    return HttpResponse('Успешно')

def get_notifications(request):
    notifications = request.user.notification_set.all()
    print(notifications())
