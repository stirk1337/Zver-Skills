from django.shortcuts import render
from .models import Test
from django.contrib.auth.models import User
import datetime
from datetime import datetime
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
import math
import re


def browse(request):
    return render(request, 'tests/browse.html')

@login_required(login_url='/user/login/')
def get_tests_by_filter(request):
    #block = request.GET.get('block')
    tests = Test.objects.all()
    #if block:
    #    goals = goals.filter(block=block)
    data = list(tests.values())
    return JsonResponse(data, safe=False)
    