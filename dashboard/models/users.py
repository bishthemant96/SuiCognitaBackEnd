from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    occupation_id = models.IntegerField(blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=16, blank=True, null=True)
    username = models.CharField(unique=True, max_length=16, blank=True, null=True)
    preference1 = models.IntegerField(blank=True, null=True)
    preference2 = models.IntegerField(blank=True, null=True)
    preference3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
