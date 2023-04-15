from django.db import models

class Vacancy(models.Model):
    name = models.CharField(max_length=250)