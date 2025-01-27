from .models import Profile, Game
from .models import Profile_Block

def match_profiles(user_id):
    
    current_profile = Profile.objects.get(id=user_id)
    current_profile_games = Game.objects.filter(profile_id=current_profile.id)
    current_profile_genres = set()
    for game in current_profile_games:
        current_profile_genres.update(game.genre)

    matching_profiles = []

    blocked_profiles = Profile_Block.objects.filter(profile_id=current_profile.id).values_list('blocked_profile_id', flat=True)

    for profile in Profile.objects.exclude(id=user_id).exclude(id__in=blocked_profiles):
        profile_id = profile.id
        profile_games = Game.objects.all().filter(profile_id=profile_id)
        profile_genres = set()
        for game in profile_games:
            profile_genres.update(game.genre)
            if current_profile_genres.intersection(profile_genres):
                matching_profiles.append(profile)
                break

    return matching_profiles