from django.contrib import admin
from .models import TestFileModel, JudgeModel

# Register your models here.

admin.site.register(TestFileModel)
admin.site.register(JudgeModel)