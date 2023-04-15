from django.db import models
from django.contrib.auth.models import User
from tests.models import Test, Task
from django.core.validators import MaxValueValidator, MinValueValidator

class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=30, choices=[('Соискатель', 'Соискатель'), ('Ментор', 'Ментор'), ('Работодатель', 'Работодатель'), ('Заказчик', 'Заказчик')])
    contacts = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    
class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    skill = models.CharField(max_length=20)
    exp = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    result = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

class TaskResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    result = models.BooleanField(default=False)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)