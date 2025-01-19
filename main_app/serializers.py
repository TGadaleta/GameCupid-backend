from rest_framework import serializers
from .models import (Profile, Profile_Match, Profile_BLock, Game, Platform, Genre_Scores, )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class Profile_MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile_Match
        fields = '__all__'

class Profile_BLockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile_BLock
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

class Genre_ScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre_Scores
        fields = '__all__'




