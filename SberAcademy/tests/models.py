from django.db import models

class Test(models.Model):
    difficulty = models.CharField(choices=[('Легкая', 'Легкая'), ('Средняя', 'Средняя'), ('Сложная', 'Сложная')], max_length=15)
    skill = models.CharField(max_length=20)

class Question(models.Model):
    test = models.OneToOneField(Test, on_delete=models.CASCADE, primary_key=True)
    true1 = models.CharField(max_length=20)
    false2 = models.CharField(max_length=20)
    false2 = models.CharField(max_length=20)
    false3 = models.CharField(max_length=20)
