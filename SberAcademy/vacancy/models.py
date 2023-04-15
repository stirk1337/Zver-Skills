from django.db import models
from django.contrib.auth.models import User
from tests.models import Test

class Vacancy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, default='')

class Skill(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100, default='')

class Survey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)

class SkillResult(models.Model):
    skill = models.CharField(max_length=100)
    points = models.IntegerField(max_length=100)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
