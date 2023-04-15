from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=100, default='')
    random = models.BooleanField(default=False)
    description = models.CharField(max_length=100, default='')
    skill = models.CharField(max_length=20)
    

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    opt1 = models.CharField(max_length=100)
    opt2 = models.CharField(max_length=100)
    opt3 = models.CharField(max_length=100)
    opt4 = models.CharField(max_length=100)
    right = models.CharField(max_length=100, default='')
    skill = models.CharField(max_length=100, default='')

class Task(Test):
    difficulty = models.CharField(choices=[('Легкая', 'Легкая'), ('Средняя', 'Средняя'), ('Сложная', 'Сложная')], max_length=15)