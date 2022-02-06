from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(verbose_name="Prénom", max_length=30)
    last_name = models.CharField(verbose_name="Nom", max_length=30)
    email = models.EmailField(verbose_name="Email", null=False)


class Student(User):
    pass


class Coach(User):
    pass


class Project(models.Model):
    project_name = models.CharField(
        verbose_name="Titre du projet", max_length=50)
    project_duration = models.IntegerField(
        verbose_name="Durée Estimée", default=0)
    time_allocated = models.IntegerField(verbose_name="Temps Alloué")
    needs = models.TextField(verbose_name="Besoins", max_length=250)
    description = models.TextField(max_length=250)

    isValid = models.BooleanField(default=False)
    
    creator = models.OneToOneField(
        to = Student, 
        on_delete = models.CASCADE, 
        related_name = "project_owner"
    )