from django.db import models
from django.contrib.auth.models import User
from tests.models import Test

class Vacancy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250, default='')

class Skill(models.Model):
    user = models.ForeignKey(Vacancy, on_delete=models.CASCADE)

class Survey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
