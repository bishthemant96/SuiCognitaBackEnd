from rest_framework import serializers
from dashboard.models.movies import Movies

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('id', 'title','clicks')
