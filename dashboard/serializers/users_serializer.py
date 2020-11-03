from rest_framework import serializers
from dashboard.models.users import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'age','gender', 'zip_code')
