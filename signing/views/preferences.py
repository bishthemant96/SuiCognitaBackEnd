#Standard Packages
from rest_framework.views import APIView
from rest_framework.response import Response

#Models
from dashboard.models.users import Users

#MainClass
class Preferences(APIView):
    def post(self, request):
        id = request.POST['id']
        preference1 = request.POST['preference1']
        preference2 = request.POST['preference2']
        preference3 = request.POST['preference3']
        code = 404

        try:
            tuple = Users.objects.get(id=id)
            tuple.preference1 = preference1
            tuple.preference2 = preference2
            tuple.preference3 = preference3
            tuple.save()

            code = 200

        except Exception as e:
            code = 404

        return Response(status = code)
