from django.db import models
from django.contrib.auth.models import User
from teams.models import Teams
from leagues.models import Leagues
# Create your models here.

class Coach(models.Model):
    idcoach = models.AutoField(db_column='idCoach', primary_key=True)  # Field name made lowercase.
    id_auth_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_auth_user')
    id_team = models.ForeignKey(Teams, models.DO_NOTHING, db_column='id_team', blank=True, null=True)
    id_league = models.ForeignKey(Leagues, models.DO_NOTHING, db_column='id_league')
    rank = models.CharField(db_column='Rank', max_length=45)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'Coach'
        verbose_name = 'Coach'
        verbose_name_plural = 'Coaches'