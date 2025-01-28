from rest_framework import serializers
from .models import (Profile, Profile_Match, Profile_Block, Game, Platform, Genre_Scores, User)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Add a password field, make it write-only

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    
    def create(self, validated_data):
      user = User.objects.create_user(
          username=validated_data['username'],
          email=validated_data['email'],
          password=validated_data['password']  # Ensures the password is hashed correctly
      )
      
      return user

class Profile_MatchSerializer(serializers.ModelSerializer):
    profile_id = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    match_profile_id = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())

    class Meta:
        model = Profile_Match
        fields = ['id', 'profile_id', 'match_profile_id', 'date_matched']

    def create(self, validated_data):
        return Profile_Match.objects.create(**validated_data)

class Profile_BlockSerializer(serializers.ModelSerializer):
    profile_id = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    blocked_profile_id = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())

    class Meta:
        model = Profile_Block
        fields = ['id', 'profile_id', 'blocked_profile_id', 'date_blocked']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'genre', 'fav_rank']

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['brand', 'tag']

class Genre_ScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre_Scores
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    Games = GameSerializer(many=True, read_only=True)
    platforms = PlatformSerializer(many=True, read_only=True)
    profile_match = Profile_MatchSerializer(many=True, read_only=True)
    profile_block = Profile_BlockSerializer(many=True, read_only=True)
    genre_Scores = Genre_ScoresSerializer(many=True, read_only=True)
    

    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'gender', 'city', ]
    
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