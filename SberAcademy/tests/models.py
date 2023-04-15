from django.db import models

class Test(models.Model):
    difficulty = models.CharField(choices=[('Легкая', 'Легкая'), ('Средняя', 'Средняя'), ('Сложная', 'Сложная')], max_length=15)
    skill = models.CharField(max_length=20)

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    true1 = models.CharField(max_length=100)
    false1 = models.CharField(max_length=100)
    false2 = models.CharField(max_length=100)
    false3 = models.CharField(max_length=100)
