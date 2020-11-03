from django.db import models

class Ratings(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    movie_id = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    rated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratings'
