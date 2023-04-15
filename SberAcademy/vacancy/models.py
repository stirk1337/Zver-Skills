from django.db import models
from django.contrib.auth.models import User

class Vacancy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

class Skill(models.Model):
    user = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    