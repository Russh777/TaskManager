from django.urls import path, include
from .views import TasksView, newUsers, deleteUser, newTasks, deleteTask, \
    newResponsible,deleteResponsible, updateUser, updateTask, user_login

urlpatterns = [
    path('login', user_login),
    path('taskview', TasksView.as_view()),
    path('createuser', newUsers),
    path('deleteuser', deleteUser),
    path('createtask', newTasks),
    path('deletetask', deleteTask),
    path('createresponsible', newResponsible),
    path('deleteresponsible', deleteResponsible),
    path('updateuser', updateUser),
    path('updatetask', updateTask)
]