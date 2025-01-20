from rest_framework import serializers
from .models import (Profile, Profile_Match, Profile_BLock, Game, Platform, Genre_Scores, )
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password', write_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        profile = Profile.objects.create(user=user, **validated_data)
        return profile
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            for attr, value in user_data.items():
                setattr(instance.user, attr, value)
            instance.user.save()

    def delete(self, instance):
        user = instance.user
        instance.delete()
        user.delete
        

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




