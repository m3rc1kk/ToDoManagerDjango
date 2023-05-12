from django.db import models
from django.contrib.auth.models import User

class TaskModel(models.Model):
    content = models.CharField(max_length=25, verbose_name= 'Задача', null = True)
    complete_date = models.DateTimeField(verbose_name='Дата выполнения')
    is_complete = models.BooleanField(default=False, verbose_name='Выполнено')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, verbose_name='Автор')
    
    class Meta:
        db_table = 'TaskModel'
        ordering = ['complete_date']

