from rest_framework.views import APIView
from .models import Profile, Game, Platform, Profile_Match, Profile_Block
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
  
class ProfileList(generics.ListAPIView): #get all profiles
  serializer_class = ProfileSerializer

  def get_queryset(self):
    user = self.request.user
    return Profile.objects.filter(user=user)
  
class ProfileDetailView(APIView): #get one profile
    def get(self, request, user_id):
        try:
            # Fetch the profile by user.id
            profile = Profile.objects.get(user_id=user_id)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response(
                {"error": "Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )
  
class ProfileEdit(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
      return Profile.objects.filter(user_id=self.request.user.id)

    def get_object(self):
      profile = Profile.objects.get(user_id=self.request.user.id)
      if profile.user != self.request.user:
        raise PermissionDenied("You are not allowed to edit this profile.")
      return profile

class UserDelete(generics.DestroyAPIView):
  serializer_class = ProfileSerializer

  def get_object(self):
    return self.request.user
  
class ProfileGamesCreate(generics.CreateAPIView):
  serializer_class = GameSerializer
  permission_classes = [permissions.IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(profile_id=self.request.user.profile)
  
class ProfileGamesList(generics.ListAPIView):
  serializer_class = GameSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    return Game.objects.filter(profile_id=self.request.user.profile)

class ProfileGamesEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'  # Specifies that the primary key will be used in the URL

    def get_queryset(self):
        # Restrict queryset to games owned by the current user's profile
        return Game.objects.filter(profile_id=self.request.user.profile)

    def perform_update(self, serializer):
        # Ensure the game belongs to the user before updating
        game = self.get_object()
        if game.profile_id != self.request.user.profile:
            raise PermissionDenied("You do not have permission to edit this game.")
        serializer.save()

    def perform_destroy(self, instance):
        # Ensure the game belongs to the user before deleting
        if instance.profile_id != self.request.user.profile:
            raise PermissionDenied("You do not have permission to delete this game.")
        instance.delete()

class ProfilePlatformsListCreate(generics.ListCreateAPIView): # RetrieveAPIView it was this but now its ListAPIView
  serializer_class = PlatformSerializer
  permission_classes = [permissions.IsAuthenticated]
  
  def get_queryset(self):
    profile = Profile.objects.get(user_id=self.request.user.id)
    print(profile.id)
    return Platform.objects.filter(profile_id=profile.id)

  def perform_create(self, serializer):
    serializer.save(profile_id=self.request.user.profile)
  
class ProfilePlatformsEdit(generics.RetrieveUpdateAPIView):
  serializer_class = PlatformSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    return Platform.objects.filter(profile_id=self.request.user.profile)
  
  def perform_update(self, serializer):
    platform = self.get_object()
    if platform.profile_id != self.request.user.profile:
      raise PermissionDenied("You do not have permission to edit this platform.")
    serializer.save()

  def perform_destroy(self, instance):
    if instance.profile_id != self.request.user.profile:
      raise PermissionDenied("You do not have permission to delete this platform.")
    instance.delete()

class ProfileMatchCreateView(generics.CreateAPIView):
    queryset = Profile_Match.objects.all()
    serializer_class = Profile_MatchSerializer
    permission_classes = [permissions.IsAuthenticated]
  
    def perform_create(self, serializer):
        profile_id = self.request.user.profile
        serializer.save(profile_id=profile_id)

class ProfileMatchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile_Match.objects.all()
    serializer_class = Profile_MatchSerializer
    permission_classes = [permissions.IsAuthenticated]
  
class ProfileBlockCreateView(generics.CreateAPIView):
    serializer_class = Profile_BlockSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(profile_id=self.request.user.profile)
  
class ProfileBlockDetailView(generics.RetrieveDestroyAPIView):
    queryset = Profile_Block.objects.all()
    serializer_class = Profile_BlockSerializer
    permission_classes = [permissions.IsAuthenticated]
  
class GenreScoresEdit(generics.RetrieveUpdateAPIView):
  serializer_class = Genre_ScoresSerializer

  def get_queryset(self):
    profile_id = self.get_object()
    return GenreScores.objects.filter(profile_id=profile_id)