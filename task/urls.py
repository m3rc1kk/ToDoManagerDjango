from django.urls import path

from .views import *

urlpatterns = [
    path('list/', TaskList.as_view(), name = 'task-list'),
    path('create/', TaskCreate.as_view(), name = 'task-create'),
    path('edit/<int:pk>/', TaskEdit.as_view(), name = 'task-edit'),
    path('complete/<int:pk>/', TaskComplete.as_view(), name= 'task-complete'),
    path('main/', MainPage, name= 'main-page'),
]