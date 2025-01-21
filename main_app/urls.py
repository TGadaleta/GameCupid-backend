from django.urls import path
from .views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/', Profile.as_view(), name='profile'),
    path('profile/edit/', ProfileEdit.as_view(), name='profile-edit'),
    path('profile/delete/', ProfileDelete.as_view(), name='profile-delete'),
    path('profile/games/', ProfileGamesList.as_view(), name='profile-games'),
    path('profile/platforms/', ProfilePlatformsList.as_view(), name='profile-platforms'),
    path('profile/games/edit', ProfileGamesEdit.as_view(), name='profile-games-edit'),
    path('profile/platforms/edit', ProfilePlatformsEdit.as_view(), name='profile-platforms-edit'),
    path('profile/games/delete', ProfileGamesDelete.as_view(), name='profile-games-delete'),
    path('profile/platforms/delete', ProfilePlatformsDelete.as_view(), name='profile-platforms-delete'),
    path('profile/matches/', ProfileMatchesList.as_view(), name='profile-matches'),
    path('profile/matches/delete', ProfileMatchesDelete.as_view(), name='profile-matches-delete'),
    path('profile/blocs/', ProfileBlocsList.as_view(), name='profile-blocs'),
    path('profile/blocs/delete', ProfileBlocsDelete.as_view(), name='profile-blocs-delete'),
    path('game/', Game.as_view(), name='game'),
    path('game/edit/', GameEdit.as_view(), name='game-edit'),
    path('game/delete/', GameDelete.as_view(), name='game-delete'),
    path('platform/', Platform.as_view(), name='platform'),
    path('platform/edit/', PlatformEdit.as_view(), name='platform-edit'),
    path('platform/delete/', PlatformDelete.as_view(), name='platform-delete'),
    path('genre-scores/', GenreScores.as_view(), name='genre-scores'),
    path('genre-scores/edit/', GenreScoresEdit.as_view(), name='genre-scores-edit'),




]