from django.contrib import admin
from .models import UserAccount, Skill, TestResult, TaskResult

admin.site.register(UserAccount)
admin.site.register(Skill)
admin.site.register(TestResult)
admin.site.register(TaskResult)
# Register your models here.
