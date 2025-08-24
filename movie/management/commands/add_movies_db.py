from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json

class Command(BaseCommand):
    help = 'Load movies from movie_descriptions.json into the Movie model'

    def handle(self, *args, **kwargs):
        # Construct the full path to the JSON file
        #Recuerde que la consola está ubicada en la carpeta DjangoProjectBase.
        #El path del archivo movie_descriptions con respecto a DjangoProjectBase sería la carpeta anterior
        json_file_path = 'movie/management/commands/movies.json' 
        
        # Load data from the JSON file
        with open(json_file_path, 'r') as file:
            movies = json.load(file)
        
        # Add products to the database
        for i in range(min(100, len(movies))):
            movie = movies[i]
            exist = Movie.objects.filter(title=movie.get('title', '')).first()
            if not exist:
                try:
                    Movie.objects.create(
                        title=movie.get('title', ''),
                        director=movie.get('director', 'Desconocido'),
                        image='movies/images/default.jpg',
                        url=movie.get('url', ''),
                        genre=movie.get('genre', ''),
                        year=movie.get('year', None),
                    )
                except Exception as e:
                    print(f"Error creando película: {movie.get('title', '')} - {e}")
            else:
                try:
                    exist.director = movie.get('director', 'Desconocido')
                    exist.image = 'movies/images/default.jpg'
                    exist.url = movie.get('url', '')
                    exist.genre = movie.get('genre', '')
                    exist.year = movie.get('year', None)
                    exist.save()
                except Exception as e:
                    print(f"Error actualizando película: {movie.get('title', '')} - {e}")