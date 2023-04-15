from django.db import models

class Vacancy(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

class Skill(models.Model):
    user = models.ForeignKey(Vacancy, on_delete=models.CASCADE)