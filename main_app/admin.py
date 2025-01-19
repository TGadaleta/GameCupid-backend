from django.contrib import admin

# Register your models here.
from .models import Profile, Profile_BLock, Profile_Match, Game, Platform, Genre_Scores

admin.site.register(Profile)
admin.site.register(Profile_BLock)
admin.site.register(Profile_Match)
admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Genre_Scores)