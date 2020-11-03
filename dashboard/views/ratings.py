#Standard Packages
from rest_framework.views import APIView
from rest_framework.response import Response

#Models
from dashboard.models.ratings import Ratings

#MainClass
class Rating(APIView):
    def get(self, request):
        return Response()

    def post(self, request):
        user_id = request.POST['user_id']
        movie_id = request.POST['movie_id']
        rating = request.POST['rating']
        print(request.POST)
        code = 404

        try:
            print("T")
            user_rating = Ratings.objects.get(user_id=user_id, movie_id=movie_id)
            user_rating.rating = rating
            user_rating.save()
            code = 200

        except Exception as e:
            print("E")
            Ratings.objects.create( user_id = user_id,
                                    movie_id = movie_id,
                                    rating = rating)
            code = 200

        return Response(status = code)
