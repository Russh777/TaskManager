from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from .models import TasksToPersons,Persons,Tasks
from .forms import CreateUserForm, CreateTaskForm, CreateResponsible, LoginForm
from django.contrib.auth import authenticate, login
import logging

logger = logging.getLogger(__name__)

class TasksView(generic.ListView):
    def get(self, request):
        return render(request, 'new_one/view_task.html', {'TasksToPersons': TasksToPersons.objects.all(),
                                                          'Persons': Persons.objects.all(),
                                                          'Tasks': Tasks.objects.all()})
@csrf_exempt
def newUsers(request):
    if request.method == "GET":
        return render(request, 'new_one/create_user.html')
    elif request.method == "POST":
        CreateUserForm(request.POST).save()
        logger.info('User added: ' + request.POST.get('name'))
        return redirect('http://127.0.0.1:8000/taskmanager/taskview')

def updateUser(request):
    if request.method == "GET":
        return render(request, 'new_one/update_user.html', {'Persons': Persons.objects.all()})
    elif request.method == "POST":
        update = Persons.objects.get(id=request.POST.get('select'))
        info = str(Persons.objects.get(id=request.POST.get('select')))
        update.name = request.POST.get('name')
        update.save()
        logger.info('User updated: ' +
                    info + ' on ' +
                    request.POST.get('name'))
        return redirect('http://127.0.0.1:8000/taskmanager/taskview')

def deleteUser(request):
    if request.method == "GET":
        return render(request, 'new_one/delete_user.html', {'Persons': Persons.objects.all()})
    elif request.method == "POST":
        d = Persons.objects.get(id=request.POST.get('select'))
        info = str(Persons.objects.get(id=request.POST.get('select')))
        d.delete()
        logger.info('User deleted: ' + info)
        return redirect('http://127.0.0.1:8000/taskmanager/taskview')

@csrf_exempt
def newTasks(request):
    if request.method == "GET":
        return render(request, 'new_one/create_task.html')
    elif request.method == "POST":
        CreateTaskForm(request.POST).save()
        logger.info('User added new task: ' + request.POST.get('task'))
        return redirect('http://127.0.0.1:8000/taskmanager/taskview')

def deleteTask(request):
    if request.method == "GET":
        return render(request, 'new_one/delete_task.html', {'Tasks': Tasks.objects.all()})
    elif request.method == "POST":
        d = Tasks.objects.get(id=request.POST.get('select'))
        info = str(Tasks.objects.get(id=request.POST.get('select')))
        d.delete()
        logger.info('User deleted: ' + info)
        return redirect('http://127.0.0.1:8000/taskmanager/taskview')

def updateTask(request):
    if request.method == "GET":
        return render(request, 'new_one/update_task.html', {'Tasks': Tasks.objects.all()})
    elif request.method == "POST":
        update = Tasks.objects.get(id=request.POST.get('select'))
        info = str(Tasks.objects.get(id=request.POST.get('select')))
        update.task = request.POST.get('task')
        update.startdate = request.POST.get('startdate')
        update.deadline = request.POST.get('deadline')
        update.save()
        logger.info('User updated: ' +
                    info + ' on ' +
                    request.POST.get('task'))
        return redirect('http://127.0.0.1:8000/taskmanager/taskview')

def newResponsible(request):
    if request.method == "GET":
        return render(request, 'new_one/create_responsible.html', {'Persons': Persons.objects.all(),
                                                          'Tasks': Tasks.objects.all()})
    elif request.method == "POST":
        TasksToPersons(
            task = Tasks.objects.get(id=request.POST.get('task')),
            responsible_person = Persons.objects.get(id=request.POST.get('responsible_person')),
            comment = request.POST['comment']
        ).save()
        return redirect('http://127.0.0.1:8000/taskmanager/taskview')

def deleteResponsible(request):
    if request.method == "GET":
        return render(request, 'new_one/delete_responsible.html', {'Tasks': TasksToPersons.objects.all()})
    elif request.method == "POST":
        d = TasksToPersons.objects.get(id=request.POST.get('task'))
        d.delete()  # Удалить пост из БД
        return redirect('http://127.0.0.1:8000/taskmanager/taskview')

@csrf_exempt
def user_login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'new_one/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect ('taskview')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    # else:
    #     form = LoginForm()
    # return render(request, 'new_one/login.html', {'form': form})
