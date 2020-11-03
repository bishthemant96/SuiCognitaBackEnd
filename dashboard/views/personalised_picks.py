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
class PersonalisedPicks(APIView):
    def get(self, request, id):
        user_tuple = Users.objects.get(id=id)
        user_set = Users.objects.filter(occupation_id=user_tuple.occupation_id)|Users.objects.filter(age=22)

        id_set = []
        for tuple in user_set:
            id_set.append(tuple.id)

        good_ratings_set = Ratings.objects.filter(user_id__in=id_set, rating__range=[4,6])
        bad_ratings_set = Ratings.objects.filter(user_id__in=id_set, rating__range=[-1,2])

        high_rating_set = []
        for tuple in good_ratings_set:
            high_rating_set.append(tuple.movie_id)

        low_rating_set = []
        for tuple in bad_ratings_set:
            low_rating_set.append(tuple.movie_id)

        unique_high_set = set(high_rating_set)
        unique_low_set = set(low_rating_set)

        counted_high_set = Counter(high_rating_set)
        counted_low_set = Counter(low_rating_set)

        recommended_list = []
        recommended_dict = {}
        for item in unique_high_set:
            if item in unique_low_set:
                if(counted_high_set[item]-(1.5*counted_low_set[item])>0):
                    recommended_dict[item] = counted_high_set[item]/counted_low_set[item]
            elif counted_high_set[item]>=20:
                recommended_dict[item] = counted_high_set[item]

        sorted_by_value = sorted(recommended_dict.items(), key=lambda kv: kv[1], reverse=True)


        dataset = {}
        ratings_arr = []
        rating_arr_movie = []
        genres = [[],[],[]]
        iterator = -1
        for item in sorted_by_value[:3]:
            iterator = iterator+1
            recommended_list.append(item[0])
            try:
                user_rating = Ratings.objects.get(user_id=id, movie_id = item[0])
                ratings_arr.append(user_rating.rating)
                rating_arr_movie.append(item[0])

            except Ratings.DoesNotExist:
                ratings_arr.append(0)
                rating_arr_movie.append(item[0])

            genre_tuples = GenresMovies.objects.filter(movie_id=item[0])
            genre_list = []
            for item in genre_tuples:
                genre_list.append(Genres.objects.get(id=item.genre_id).name)

            genres[iterator] = genre_list

        movie_list = Movies.objects.filter(id__in=recommended_list)
        seriailized = MoviesSerializer(movie_list, many=True)

        rating_array = [x for _,x in sorted(zip(rating_arr_movie,ratings_arr))]
        genres_array = [x for _,x in sorted(zip(rating_arr_movie,genres))]
        dataset['data'] = seriailized.data
        dataset['ratings'] = rating_array
        dataset['genres'] = genres_array
        print(dataset)
        return Response(dataset)
