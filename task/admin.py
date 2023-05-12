from django.contrib import admin

from task.models import TaskModel


@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'complete_date', 'is_complete']