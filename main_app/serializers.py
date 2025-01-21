from rest_framework import serializers
from .models import (Profile, Profile_Match, Profile_Block, Game, Platform, Genre_Scores, )
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']  # Ensures the password is hashed correctly
      )
      
      return user

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(source='user.password', write_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True) # Make the user field read-only to prevent nested user creation

    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'gender', 'city', 'location']
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        profile = Profile.objects.create(user=user, **validated_data)
        return profile
    
    def update(self, instance, validated_data):
        # Handle nested user fields
        user_data = validated_data.pop('user', {})
        user = instance.user
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()

        # Handle Profile fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance

class Profile_MatchSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Profile_Match
        fields = '__all__'

class Profile_BlockSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Profile_Block
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