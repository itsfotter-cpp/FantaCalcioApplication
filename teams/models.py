from leagues.models import Leagues
from django.db import models
from leagues.models import Leagues

# Create your models here.
class Teams(models.Model):
    idteam = models.AutoField(db_column='idTeam', primary_key=True)  # Field name made lowercase.
    teamname = models.CharField(db_column='TeamName', max_length=100)  # Field name made lowercase.
    firstfantacoach = models.CharField(db_column='FirstFantaCoach', max_length=100)  # Field name made lowercase.
    secondfantacoach = models.CharField(db_column='SecondFantaCoach', max_length=45, blank=True, null=True)  # Field name made lowercase.
    crediti = models.CharField(db_column='Crediti', max_length=45)  # Field name made lowercase.
    id_league = models.ForeignKey(Leagues, models.DO_NOTHING, db_column='id_league', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Teams'
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

class Quotazioni(models.Model):
    idquotazioni = models.AutoField(db_column='IDQuotazioni', primary_key=True)  # Field name made lowercase.
    ruolo = models.CharField(db_column='Ruolo', max_length=2)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=100)  # Field name made lowercase.
    squadra = models.CharField(db_column='Squadra', max_length=50)  # Field name made lowercase.
    quotazioneattuale = models.CharField(db_column='QuotazioneAttuale', max_length=10)  # Field name made lowercase.
    quotazioneiniziale = models.CharField(db_column='QuotazioneIniziale', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Quotazioni'
        verbose_name = 'Quotazione'
        verbose_name_plural = 'Quotazioni'

class Players(models.Model):
    idplayer = models.AutoField(db_column='IDPlayer', primary_key=True)  # Field name made lowercase.
    ruolo = models.CharField(db_column='Ruolo', max_length=5)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=100)  # Field name made lowercase.
    costo = models.CharField(db_column='Costo', max_length=10)  # Field name made lowercase.
    id_team = models.ForeignKey(Teams, models.DO_NOTHING, db_column='id_team')

    class Meta:
        managed = False
        db_table = 'Players'
        verbose_name = "Player"
        verbose_name_plural = "Players"