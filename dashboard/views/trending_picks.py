#Standard Packages
from rest_framework.views import APIView
from rest_framework.response import Response

#Models
from dashboard.models.users import Users
from dashboard.models.ratings import Ratings
from dashboard.models.movies import Movies
from dashboard.models.genres_movies import GenresMovies
from dashboard.models.genres import Genres

#Serializers
from dashboard.serializers.movies_serializer import MoviesSerializer

#Additional Packages
from collections import Counter

#MainClass
class TrendingPicks(APIView):
    def get(self, request, id):
        movie_set = Movies.objects.all().order_by('-clicks')[:3]
        print(movie_set)


        dataset = {}
        ratings_arr = []
        rating_arr_movie = []
        genres = [[],[],[]]
        iterator = -1
        for item in movie_set:
            iterator = iterator+1
            try:
                user_rating = Ratings.objects.get(user_id=id, movie_id = item.id)
                ratings_arr.append(user_rating.rating)
                rating_arr_movie.append(item.id)

            except Ratings.DoesNotExist:
                ratings_arr.append(0)
                rating_arr_movie.append(item.id)

            genre_tuples = GenresMovies.objects.filter(movie_id=item.id)
            genre_list = []
            for item in genre_tuples:
                genre_list.append(Genres.objects.get(id=item.genre_id).name)

            genres[iterator] = genre_list

        seriailized = MoviesSerializer(movie_set, many=True)
        dataset['data'] = seriailized.data
        dataset['ratings'] = ratings_arr
        dataset['genres'] = genres
        return Response(dataset)
