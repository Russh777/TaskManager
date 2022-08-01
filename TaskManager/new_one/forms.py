from django import forms
from .models import Persons, Tasks, TasksToPersons

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Persons
        fields = '__all__'

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'

class CreateResponsible(forms.ModelForm):
    class Meta:
        model = TasksToPersons
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

