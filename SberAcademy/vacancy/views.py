from django.shortcuts import render
from .models import Vacancy
from django.http import JsonResponse, HttpResponse
# Create your views here.
def browse(request):
    return render(request, 'vacancy/vacancy.html')

def get_vacancies(request):
    vac = Vacancy.objects.all()
    vac = list(vac.values())
    return JsonResponse(vac, safe=False)
    