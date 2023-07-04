from django.contrib import admin
from .models import CreateUserModel, TestFileModel

# Register your models here.

admin.site.register(CreateUserModel)
admin.site.register(TestFileModel)