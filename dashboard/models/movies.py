from django.db import models

class Movies(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    clicks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'
