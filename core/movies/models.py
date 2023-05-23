from django.db import models

# Create your models here.
class Movie(models.Model):
    #Nombre pelicula valor único
    name = models.CharField(max_length=225, unique=True) 
    year = models.IntegerField()#Campo requerido () vacío
    synopsis = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name