from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #automaticamente cuando se crea
    last_updated = models.DateTimeField(auto_now=True) #automaticamente cuando se edita

    def __str__(self):
        return f"{self.movie.name} - {self.created_at}"
