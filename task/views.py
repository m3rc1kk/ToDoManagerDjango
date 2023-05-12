from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views import View
from .permissions import AuthorPermissionsMixin
from .forms import TaskForm
from .models import TaskModel
from django.contrib.auth.mixins import LoginRequiredMixin



class TaskList(LoginRequiredMixin, generic.ListView):
    template_name = 'task/tasklist.html'
    model = TaskModel
    
    def get_context_data(self,**kwargs):
        
        # В первую очередь получаем базовую реализацию контекста
        context = super(TaskList, self).get_context_data(**kwargs)
        
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        context['task_count'] = TaskModel.objects.filter(is_complete = 0, author = self.request.user).count()
        
        return context
    

class TaskCreate(LoginRequiredMixin, generic.CreateView):
    model = TaskModel
    form_class = TaskForm
    success_url = reverse_lazy('task-list')
    def post(self, request):
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('task-list')
        else:
            form = TaskForm()
        return render(request, 'task/taskmodel_form/html', {'form': form})


class TaskEdit(AuthorPermissionsMixin, generic.UpdateView):
    model = TaskModel
    template_name = 'task/taskmodel_update_form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task-list')


class TaskComplete(View):
    def get(self, request, pk):
        task_model = TaskModel.objects.get(pk = pk)
        task_model.is_complete = 1
        task_model.save(update_fields=["is_complete"])
        return redirect('task-list')


def MainPage(request):
    return render(request, 'task/main_page.html')