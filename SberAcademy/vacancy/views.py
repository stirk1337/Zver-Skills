from django.shortcuts import render
from .models import Vacancy, Survey, SkillResult
from tests.models import Test, Question
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
import random
import ast
from django.contrib.auth.models import User
# Create your views here.
def browse(request):
    return render(request, 'vacancy/vacancy.html')

def get_vacancies(request):
    vacancies = Vacancy.objects.all()
    vac_skills = []
    for vac in vacancies:
        skills = vac.skill_set.all()
        ski = list(skills.values('skill'))
        skillings = []
        for s in ski:
            skillings.append(s['skill'])
        vac_skills.append(skillings)
    vacancies = list(vacancies.values())
    
    for i, vac in enumerate(vacancies):
        vac['name'] = User.objects.get(id=vac['user_id']).username
        vac['skills'] = vac_skills[i]
    return JsonResponse(vacancies, safe=False)

def test_vac(request):
    vac = Vacancy.objects.get(id=request.GET.get('vacancy_id'))
    skills = vac.skill_set.all()
    q_list = []
    test_xd = Test(name='На вакансию ' + vac.name, random=True, skill='Net', description='Тест оценит ваши знания на вакансию ' + vac.name )
    test_xd.save()
    for skill in skills:
        tests = Test.objects.all().filter(skill=skill.skill)
        for test in tests:
            questions = test.question_set.all()
            for question in questions:
                q_list.append({'question': question.question, 'opt1': question.opt1, 'opt2': question.opt2, 'opt3': question.opt3, 'opt4': question.opt4, 'right': question.right, 'skill': skill.skill})
    
    random_list = random.sample(q_list, min(len(skills)*10, len(q_list)))
    for q in random_list:
        question = Question(question=q['question'],
                            opt1=q['opt1'],
                            opt2=q['opt2'],
                            opt3=q['opt3'],
                            opt4=q['opt4'],
                            right=q['right'],
                            skill=q['skill'],
                            test=test_xd)
        question.save()
    test_dict = model_to_dict(test_xd)
    test_dict['questions'] = random_list
    return JsonResponse(test_dict)

def test(request, vacancy_id):
    return render(request, 'vacancy/vac_test.html')

def start_test(request):
    vac = Vacancy.objects.get(id=request.GET.get('vacancy_id'))
    skills = vac.skill_set.all()
    q_list = []
    test_xd = Test(name='На вакансию ' + vac.name, random=True, skill='Net', description='Тест оценит ваши знания на вакансию ' + vac.name )
    test_xd.save()
    for skill in skills:
        tests = Test.objects.all().filter(skill=skill.skill)
        for test in tests:
            questions = test.question_set.all()
            for question in questions:
                q_list.append({'question': question.question, 'opt1': question.opt1, 'opt2': question.opt2, 'opt3': question.opt3, 'opt4': question.opt4, 'right': question.right, 'skill': skill.skill})
    
    random_list = random.sample(q_list, min(len(skills)*10, len(q_list)))
    for q in random_list:
        question = Question(question=q['question'],
                            opt1=q['opt1'],
                            opt2=q['opt2'],
                            opt3=q['opt3'],
                            opt4=q['opt4'],
                            right=q['right'],
                            skill=q['skill'],
                            test=test_xd)
        question.save()
    test_dict = model_to_dict(test_xd)
    test_dict['questions'] = random_list
    return JsonResponse(test_dict)

def complete_test(request):
    test = Test.objects.get(id=request.GET.get('test_id'))
    answers = request.GET.get('answers').split(',')
    test_dict = model_to_dict(test)
    questions = test.question_set.all()
    rights = 0
    rights_dict = {}
    all_skills_dict = {}
    for i, q in enumerate(questions):
        if q.skill not in all_skills_dict:
            all_skills_dict[q.skill] = 1
        else:
            all_skills_dict[q.skill] += 1
        if str(q.right) == str(answers[i]):
            if q.skill not in rights_dict:
                rights_dict[q.skill] = 1
            else:
                rights_dict[q.skill] += 1

    for key,val in rights_dict.items():
        rights_dict[key] = int(val / all_skills_dict[key]) * 100
    #points = int(rights / len(questions) * 100)
    survey = Survey(vacancy=Vacancy.objects.get(id=request.GET.get('vacancy_id')), user=request.user)
    survey.save()
    for key,val in rights_dict.items():
        skill_point = SkillResult(skill=key, points=val, survey=survey)
        skill_point.save()

    return JsonResponse(rights_dict, safe=False)