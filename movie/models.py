from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movies/images/')
    url = models.URLField(max_length=200)

    