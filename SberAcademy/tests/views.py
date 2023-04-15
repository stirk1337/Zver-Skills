from django.shortcuts import render
from .models import Test, Task
from user.models import TaskResult, TestResult
from django.contrib.auth.models import User
import datetime
from datetime import datetime
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
import math
import ast
import re
import json

def test(request, test_id):
    test = Test.objects.get(id=test_id)
    return render(request, 'tests/test.html', {'test': test})

def browse(request):
    return render(request, 'tests/browse.html')

def browse_tests(request):
    return render(request, 'tests/browse_tests.html')

@login_required(login_url='/user/login/')
def get_tests_by_filter(request):
    #block = request.GET.get('block')
    tests = Test.objects.all()
    tests = tests.filter(random=False)
    data = list(tests.values())
    for i, test in enumerate(tests):
        test_result = test.testresult_set.all()
        if len(test_result) > 0:
            test_result = test_result.get(user=request.user)
            data[i]['result'] = test_result.result
        else:
            data[i]['result'] = None
    #if block:
    #    goals = goals.filter(block=block)
    return JsonResponse(data, safe=False)

@login_required(login_url='/user/login/')
def get_tasks_by_filter(request):
    #block = request.GET.get('block')
    tasks = Task.objects.all()
    data = list(tasks.values())
    for i, task in enumerate(tasks):
        task_result = task.taskresult_set.all()
        if len(task_result) > 0:
            task_result = task_result.get(user=request.user)
            data[i]['result'] = task_result.result
        else:
            data[i]['result'] = None
    #if block:
    #    goals = goals.filter(block=block)
    return JsonResponse(data, safe=False)

@login_required(login_url='/user/login/')
def get_test(request):
    test = Test.objects.get(id=request.GET.get('test_id'))
    test_dict = model_to_dict(test)
    questions = test.question_set.all()
    questions = questions.values('question', 'opt1', 'opt2', 'opt3', 'opt4')
    test_dict['questions'] = []
    for q in questions:
        test_dict['questions'].append(q)
    return JsonResponse(test_dict)

@login_required(login_url='/user/login/')
def complete_test(request):
    test = Test.objects.get(id=request.GET.get('test_id'))
    answers = request.GET.get('answers').split(',')
    test_dict = model_to_dict(test)
    questions = test.question_set.all()
    rights = 0
    for i, q in enumerate(questions):
        if str(q.right) == str(answers[i]):
            rights =+ 1
    points = int(rights / len(questions) * 100)
    if len(test.testresult_set.all().filter(user=request.user)) == 0:
        test_result = TestResult(user=request.user, test=test, result=points)
        test_result.save()
    return JsonResponse(points, safe=False)