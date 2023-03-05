from django.contrib import admin
from .models import (
    myProjects,
)
# Register your models here.
@admin.register(myProjects)
class myProjectsAdmin(admin.ModelAdmin):
    pass