from django.contrib import admin
from .models import User, Skill, TestResult, TaskResult

admin.site.register(User)
admin.site.register(Skill)
admin.site.register(TestResult)
admin.site.register(TaskResult)
# Register your models here.
