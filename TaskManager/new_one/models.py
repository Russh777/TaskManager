from django.db import models

class Persons(models.Model):
    name = models.TextField()

    def __str__(self):
        return "%s" % (self.name)

class Tasks(models.Model):
    task = models.TextField()
    startdate = models.DateField()
    deadline = models.DateField()
    def __str__(self):
        return "%s" % (self.task)

class TasksToPersons(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    responsible_person = models.ForeignKey(Persons, on_delete=models.CASCADE)
    comment = models.TextField()



