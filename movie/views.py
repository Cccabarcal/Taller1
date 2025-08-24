import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64

def statistics(request):
    matplotlib.use('Agg')  
    years = Movie.objects.values_list('year', flat=True).distinct().order_by('year')
    movie_counts_by_year = {}
    for year in years:
        movie_counts_by_year[year] = Movie.objects.filter(year=year).count()
    # Películas sin año
    count_no_year = Movie.objects.filter(year__isnull=True).count()
    if count_no_year > 0:
        movie_counts_by_year["None"] = count_no_year

    bar_width = 0.5
    bar_spacing = 0.5
    bar_positions = range(len(movie_counts_by_year))


    plt.bar(bar_positions, movie_counts_by_year.values(), width=bar_width, align='center')
    plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)
    plt.xlabel('Year')
    plt.ylabel('Number of Movies')
    plt.title('Number of Movies Released by Year')
    plt.tight_layout()

    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    # Encode the image to base64
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'statistics.html', {'graphic': graphic})

from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
        searchTerm = None  
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})

def about(request):
    return render(request, 'about.html')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})