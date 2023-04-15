from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=30, choices=[('Соискатель', 'Соискатель'), ('Ментор', 'Ментор'), ('Работодатель', 'Работодатель'), ('Заказчик', 'Заказчик')])
    contacts = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    exp = models.IntegerField()
    
    
class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    skill = models.CharField(max_length=20)
    exp = models.IntegerField()