from rest_framework import serializers
from .models import Game, Genre, Platform, Publisher, Developer, GameInstance

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class GameInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameInstance
        fields = '__all__'
        