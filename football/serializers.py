# football/serializers.py
from rest_framework import serializers
from .models import Match, Team, Player, Area

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'areaname']

class TeamSerializer(serializers.ModelSerializer):
    area = AreaSerializer()

    class Meta:
        model = Team
        fields = ['id', 'teamname', 'area']

    def create(self, validated_data):
        area_data = validated_data.pop('area')
        
        area, created = Area.objects.get_or_create(**area_data)
        
        team = Team.objects.create(area=area, **validated_data)
        return team

class PlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = Player
        fields = ['id', 'Playername', 'position', "team"]

    def create(self, validated_data):
        team_data = validated_data.pop('team')
        team_serializer = TeamSerializer(data=team_data)
        team_serializer.is_valid(raise_exception=True)
        team = team_serializer.save()
        player = Player.objects.create(team=team, **validated_data)
        return player
        

class MatchSerializer(serializers.ModelSerializer):
    home_team = TeamSerializer()
    away_team = TeamSerializer()

    class Meta:
        model = Match
        fields = ['id', 'home_team', 'away_team', 'match_date', 'homeTeam_goal', 'awayTeam_goal'] 
    
    def create(self, validated_data):
        home_team_data = validated_data.pop('home_team')


        away_team_data = validated_data.pop('away_team')

        home_team_serializer = TeamSerializer(data=home_team_data)
        home_team_serializer.is_valid(raise_exception=True)
        home_team = home_team_serializer.save()

        away_team_serializer = TeamSerializer(data=away_team_data)
        away_team_serializer.is_valid(raise_exception=True)
        away_team = away_team_serializer.save()

        # Createing the Match object with the related teams
        match = Match.objects.create(
            home_team=home_team,
            away_team=away_team,
            **validated_data
        )
        return match
    
