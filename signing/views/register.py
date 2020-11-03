#StandardPackages
from rest_framework.views import APIView
from rest_framework.response import Response

#Models
from dashboard.models.users import Users
from dashboard.models.occupations import Occupations

#MainClass
class Register(APIView):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        age = request.POST['age']
        gender = request.POST['gender']
        zip_code = request.POST['zip_code']
        occupation_id = request.POST['occupation_id']

        code = 404
        try:
            user_tuple = Users.objects.create(  username=username,
                                            password=password,
                                            age=age,
                                            gender=gender,
                                            zip_code=zip_code,
                                            occupation_id=occupation_id
                                            )

            data = {}
            data['user_id'] = user_tuple.id
            data['occupation_id'] = user_tuple.occupation_id
            occupation_tuple = Occupations.objects.get(id=user_tuple.occupation_id)
            data["occupation_name"] = occupation_tuple.name
            code = 200
        except Exception as e:
            code = 404

        return Response(data, status=code)
