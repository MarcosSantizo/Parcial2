from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(default='usuario@correo.com')
    edad = models.PositiveIntegerField(default=18)


    def __str__(self):
        return self.nombre
