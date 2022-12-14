# Generated by Django 4.0.6 on 2022-07-18 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=50)),
                ('startdate', models.DateField()),
                ('deadline', models.DateField()),
                ('date_of_completion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TasksToPersons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('responsible_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_one.persons')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_one.tasks')),
            ],
        ),
    ]
