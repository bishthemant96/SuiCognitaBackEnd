from django.db import models


class GenresMovies(models.Model):
    id = models.IntegerField(primary_key=True)
    movie_id = models.IntegerField(blank=True, null=True)
    genre_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genres_movies'
