from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Leagues(models.Model):
    idleague = models.AutoField(db_column='idLeague', primary_key=True)  # Field name made lowercase.
    leaguename = models.CharField(db_column='LeagueName', max_length=100)  # Field name made lowercase.
    teamnumber = models.CharField(db_column='TeamNumber', max_length=45)  # Field name made lowercase.
    iscritti = models.CharField(db_column='Iscritti', max_length=45, default=0)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=128)  # Field name made lowercase.
    crediti = models.CharField(db_column='Crediti', max_length=45)  # Field name made lowercase.
    id_auth_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_auth_user')

    class Meta:
        managed = False
        db_table = 'Leagues'
        verbose_name = 'League'
        verbose_name_plural = 'Leagues'