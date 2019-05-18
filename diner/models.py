from django.db import models

# Create your models here.

class Plato(models.Model):
    nombre = models.CharField(max_length=12, null=False, blank=False)
    disp = models.IntegerField(null=False, blank=False)
    fecha_disp = models.DateField(null=False, blank=False)
    descrip = models.TextField(max_length=60, null=False, blank=False)

    def __str__(self):
        return '{} - {}'.format(self.nombre, self.disp)


class Estudiante(models.Model):
    nombre = models.CharField(max_length=12, null=False, blank=False)
    apellido = models.CharField(max_length=12)
    ci = models.IntegerField(primary_key=True, unique=True, null=False, blank=False)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)


class User(models.Model):
    username = models.CharField(max_length=12, null=False, blank=False)
    password = models.CharField(max_length=12, null=False, blank=False)


class SolicitudPlato(models.Model):
    fecha_sol = models.DateField(null=False, blank=False)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.DO_NOTHING)
    plato = models.ForeignKey(Plato, null=False, blank=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{} {} {}'.format(self.fecha_sol, self.estudiante, self.plato)
