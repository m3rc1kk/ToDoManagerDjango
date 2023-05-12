from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from task.models import TaskModel
from .forms import *
from django.contrib.auth import login
from django.views import generic


def UserInfo(request):
    count = TaskModel.objects.filter(is_complete = 0, author = request.user).count()
    context = { 
        'count': count
    }
    return render (request, 'user/info_user.html', context)

def RegisterUser(request):


    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/task/list/')
    else:
        form = RegisterUserForm()
    context = {
        'form' : form , 
    
    }
    return render(request, 'user/register_user.html', context)


class LoginUser(LoginView):
    template_name = 'user/login_user.html'
class LogoutUser(LogoutView):
    next_page = '/task/main/'


def UpdateInfoUser(request):
    if request.method == 'POST':
        
        form = UpdateUserInfoForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/task/list/')
    else:
        form = UpdateUserInfoForm(instance=request.user)
    return render(request, 'user/update_info.html', {'form': form})