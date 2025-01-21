from django.urls import path
from .views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('profile/', Profile.as_view(), name='profile'),
    path('profile/edit/', ProfileEdit.as_view(), name='profile-edit'),
    path('profile/delete/', ProfileDelete.as_view(), name='profile-delete'),
    path('profile/games/', ProfileGames.as_view(), name='profile-games'),
    path('profile/platforms/', ProfilePlatforms.as_view(), name='profile-platforms')
]