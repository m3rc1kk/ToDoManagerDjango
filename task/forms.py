from django import forms
from .models import TaskModel


class TaskForm(forms.ModelForm):
    complete_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    class Meta:
        model = TaskModel
        fields = ['content', 'complete_date']
        
        