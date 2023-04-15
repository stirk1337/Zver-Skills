from django.contrib import admin
from .models import Vacancy, Skill, Survey
# Register your models here.

admin.site.register(Vacancy)
admin.site.register(Survey)
admin.site.register(Skill)