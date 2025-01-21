from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import PlatformSerializer, Profile_BLockSerializer, Profile_MatchSerializer, GameSerializer, Genre_ScoresSerializer, ProfileSerializer

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
