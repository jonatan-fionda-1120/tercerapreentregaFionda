from django.db import models

# Create your models here.

class Contacto(models.Model):
     nombre=models.CharField(max_length=50)
     apellido=models.CharField(max_length=50)
     email=models.EmailField()
     mensaje=models.CharField(max_length=50)
     def __str__(self):
        return f"{self.nombre} - {self.email} - {self.apellido} - {self.mensaje}"


class Psicologos(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    especialidad=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email} - {self.especialidad}"


class Especialidades(models.Model):
    tipo=models.CharField(max_length=50)
    def __str__(self):
        return self.tipo
    


