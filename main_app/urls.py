from django.urls import path
from .views import Home, Profile, ProfileEdit, UserDelete, ProfileGamesList, ProfilePlatformsList, ProfileGamesEdit, ProfilePlatformsEdit, ProfileMatchesList, ProfileMatchesDelete, ProfileBlocsList, GenreScores, GenreScoresEdit

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/', Profile.as_view(), name='profile'),
    path('profile/edit/', ProfileEdit.as_view(), name='profile-edit'),
    path('profile/games/', ProfileGamesList.as_view(), name='profile-games'),
    path('profile/platforms/', ProfilePlatformsList.as_view(), name='profile-platforms'),
    path('profile/games/edit', ProfileGamesEdit.as_view(), name='profile-games-edit'),
    path('profile/platforms/edit', ProfilePlatformsEdit.as_view(), name='profile-platforms-edit'),
    path('profile/matches/', ProfileMatchesList.as_view(), name='profile-matches'),
    path('profile/matches/delete', ProfileMatchesDelete.as_view(), name='profile-matches-delete'),
    path('profile/blocks/', ProfileBlocsList.as_view(), name='profile-blocks'),
    path('genre-scores/', GenreScores.as_view(), name='genre-scores'),
    path('genre-scores/edit/', GenreScoresEdit.as_view(), name='genre-scores-edit'),
    path('delete-user/<int:user_id>/', UserDelete, name='delete_user'),

]