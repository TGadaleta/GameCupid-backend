from django.urls import path
from .views import Home, ProfileList, ProfileEdit, UserDelete, ProfileGamesList, ProfilePlatformsListCreate, ProfileGamesEdit, ProfilePlatformsEdit, ProfileMatchDetailView, ProfileBlockDetailView, GenreScoresEdit, CreateUserView, LoginView, VerifyUserView, ProfileDetailView, ProfileGamesCreate, ProfileMatchCreateView, ProfileBlockCreateView

urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('users/register/', CreateUserView.as_view(), name='register'), #creates user and profile
    path('users/login/', LoginView.as_view(), name='login'), #logs in user and returns token
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'), #verifies token
    path('users/<int:user_id>/', UserDelete.as_view(), name='delete_user'), #deletes user and profile and subsequent data
    path('profile/', ProfileList.as_view(), name='profile'), #lists all profiles
    path('profile/<int:user_id>/', ProfileDetailView.as_view(), name='profile'), #displays profile
    path('profile/<int:user_id>/edit/', ProfileEdit.as_view(), name='profile-edit'), #edits profile
    path('profile/games/', ProfileGamesList.as_view(), name='user-games'), #lists all games on profile
    path('profile/games/add/', ProfileGamesCreate.as_view(), name='profile-games-add'), #adds games to profile
    path('profile/games/<int:pk>/edit/', ProfileGamesEdit.as_view(), name='profile-games-edit'), #edits and deletes games on profile
    path('profile/platforms/<int:pk>/', ProfilePlatformsListCreate.as_view(), name='profile-platforms'), #lists and creates platforms on profile
    path('profile/platforms/<int:pk>/edit/', ProfilePlatformsEdit.as_view(), name='profile-platforms-edit'), #edits and deletes platforms on profile
    path('profile/match/add/', ProfileMatchCreateView.as_view(), name='profile-match-add'), #creates a match
    path('profile/match/<int:pk>/', ProfileMatchDetailView.as_view(), name='profile-matches'), #displays matches
    path('profile/block/add/', ProfileBlockCreateView.as_view(), name='profile-block-add'), #creates a block
    path('profile/block/<int:pk>/', ProfileBlockDetailView.as_view(), name='profile-block-detail-combined'), #displays, updates and deletes blocks
    path('genre-scores/edit/', GenreScoresEdit.as_view(), name='genre-scores-edit'), #retrieves and edits genre scores
    
]