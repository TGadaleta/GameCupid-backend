from rest_framework.views import APIView
from .models import Profile, Game, Platform, Profile_Match, Profile_Block, User, Genre_Scores
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth.models import User
from .serializers import UserSerializer, PlatformSerializer, Profile_BlockSerializer, Profile_MatchSerializer, GameSerializer, Genre_ScoresSerializer, ProfileSerializer


class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })

# User Login
class LoginView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# User Verification
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the gamecupid api home route!'}
    return Response(content)
  
class ProfileView(generics.ListAPIView):
  serializer_class = ProfileSerializer

  def get_queryset(self):
    user = self.request.user.id
    return Profile.objects.filter(user=user).first()
  
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
    return Profile_Block.objects.filter(profile_id=profile_id)
  
class GenreScores(generics.ListAPIView):
  serializer_class = Genre_ScoresSerializer

  def get_queryset(self):
    profile_id = self.get_object()
    return GenreScores.objects.filter(profile_id=profile_id)
  
class GenreScoresEdit(generics.RetrieveUpdateAPIView):
  serializer_class = Genre_ScoresSerializer

  def get_queryset(self):
    profile_id = self.get_object()
    return Genre_Scores.objects.filter(profile_id=profile_id)