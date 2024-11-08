from django.db import models


class plandestudio(models.Model):
    idPlan = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()

    def __str__(self):
        return self.name


class Curso(models.Model):
    idCurso = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()

    def __str__(self):
        return self.name
    

