from django.shortcuts import render
from .models import Vacancy
# Create your views here.
def browse(request):
    return render(request, 'vacancy/vacancy.html')

def get_vacancies(request):
    vac = Vacancy.objects.all()
    