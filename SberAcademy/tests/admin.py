from django.contrib import admin
from .models import Test, Question, Task  
# Register your models here.

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Task)