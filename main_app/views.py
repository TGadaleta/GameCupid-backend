from rest_framework.views import APIView
from .models import Profile, Game, Platform, Profile_Match, Profile_Block
from rest_framework.response import Response
from rest_framework import generics
from .serializers import PlatformSerializer, Profile_BlockSerializer, Profile_MatchSerializer, GameSerializer, Genre_ScoresSerializer, ProfileSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the gamecupid api home route!'}
    return Response(content)
  
class Profile(generics.ListAPIView):
  serializer_class = ProfileSerializer

  def get_queryset(self):
    user = self.request.user
    return Profile.objects.filter(user=user)
  
class ProfileEdit(generics.RetrieveUpdateAPIView):
  serializer_class = ProfileSerializer

  def get_queryset(self):
    user = self.request.user
    return Profile.objects.filter(user=user)

  def perform_update(self, serializer):
    profile = self.get_object()
    if profile.user != self.request.user:
      raise PermissionDenied({'message': 'You do not have permission to edit this profile.'})
    serializer.save()

class UserDelete(generics.DestroyAPIView):
  serializer_class = ProfileSerializer

  def get_object(self):
    return self.request.user
  
class ProfileGamesList(generics.RetrieveAPIView):
  serializer_class = GameSerializer

  def get_queryset(self):
    profile_id = self.get_object()
    return Game.objects.filter(profile_id=profile_id)
  
class ProfileGamesEdit(generics.RetrieveUpdateAPIView):
  serializer_class = GameSerializer

  def get_queryset(self):
    profile_id = self.get_object()
    return Game.objects.filter(profile_id=profile_id)

class ProfilePlatformsList(generics.RetrieveAPIView):
  serializer_class = PlatformSerializer

  def get_queryset(self):
    profile_id = self.get_object()
    return Platform.objects.filter(profile_id=profile_id)
  
class ProfilePlatformsEdit(generics.RetrieveUpdateAPIView):
  serializer_class = PlatformSerializer

  def get_queryset(self):
    profile_id = self.get_object()
    return Platform.objects.filter(profile_id=profile_id)

class ProfileMatchesList(generics.RetrieveUpdateAPIView):
  serializer_class = Profile_MatchSerializer

  def get_queryset(self):
    profile_id = self.get_object()
    return Profile_Match.objects.filter(profile_id=profile_id)
  
class ProfileBlocksList(generics.RetrieveUpdateAPIView):
  serializer_class = Profile_BlockSerializer

  def get_queryset(self):
    profile_id = self.get_object()
    return Profile_BLock.objects.filter(profile_id=profile_id)
  
class GenreScores(generics.ListAPIView):
  serializer_class = Genre_ScoresSerializer

  def get_queryset(self):
    profile_id = self.get_object()
    return GenreScores.objects.filter(profile_id=profile_id)
  
class GenreScoresEdit(generics.RetrieveUpdateAPIView):
  serializer_class = Genre_ScoresSerializer

  def get_queryset(self):
    profile_id = self.get_object()
    return GenreScores.objects.filter(profile_id=profile_id)