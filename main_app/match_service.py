from .models import Profile, Game

def match_profiles(user_id):
    
    current_profile = Profile.objects.get(id=user_id)
    current_profile_games = Game.objects.filter(profile_id=current_profile.id)
    current_profile_genres = set()
    for game in current_profile_games:
        current_profile_genres.update(game.genre)

    matching_profiles = []

    for profile in Profile.objects.exclude(id=user_id):
        profile_id = profile.id
        profile_games = Game.objects.all().filter(profile_id=profile_id)
        profile_genres = set()
        for game in profile_games:
            profile_genres.update(game.genre)
            if current_profile_genres.intersection(profile_genres):
                matching_profiles.append(profile)
                break

    return matching_profiles