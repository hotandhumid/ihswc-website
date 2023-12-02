from django.contrib import admin
from .models import TestFileModel, JudgeModel1, JudgeModel2, JudgeModel3

# Register your models here.

admin.site.register(TestFileModel)
admin.site.register(JudgeModel1)
admin.site.register(JudgeModel2)
admin.site.register(JudgeModel3)