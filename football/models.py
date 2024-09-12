# football/models.py
from django.db import models

class Area(models.Model):
    areaname = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    teamname = models.CharField(max_length=100)
    area = models.ForeignKey(Area, related_name="teams", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Player(models.Model):
    Playername = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    team = models.ForeignKey(Team, related_name="players", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name="home_matches", on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name="away_matches", on_delete=models.CASCADE)
    match_date = models.DateTimeField()
    homeTeam_goal = models.IntegerField()
    awayTeam_goal = models.IntegerField()

    def __str__(self):
        return f'{self.home_team} vs {self.away_team}'
