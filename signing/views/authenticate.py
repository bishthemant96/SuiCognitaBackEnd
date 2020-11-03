#Standard Packages
from rest_framework.views import APIView
from rest_framework.response import Response

#Models
from dashboard.models.users import Users
from dashboard.models.occupations import Occupations

#MainClass
class Authenticate(APIView):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        code = 404

        user_tuple = Users.objects.get(username=username)
        if user_tuple.password==password:
            data = {}
            data["id"] = user_tuple.id
            data["occupation_id"] = user_tuple.occupation_id
            occupation_tuple = Occupations.objects.get(id=user_tuple.occupation_id)
            data["occupation_name"] = occupation_tuple.name
            data["username"] = username
            code = 200
            
        else:
            code = 404

        return Response(data, status = code)
