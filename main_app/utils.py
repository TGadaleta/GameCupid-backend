# myapp/utils.py

from .models import Profile, Genre_Scores

def find_genre_matches_for_profile(profile):
    """
    Calculates how closely other profiles match this profile by summing
    the absolute difference in each genre score. A lower 'distance' means
    a better match.
    """
    user_genres = Genre_Scores.objects.get(profile_id=profile)
    genre_fields = [
        "pinball", "adventure", "indie", "arcade", "visual_novel",
        "card_and_board", "moba", "point_and_click", "fighting", 
        "shooter", "music", "platform", "puzzle", "racing",
        "real_time_strategy", "role_playing", "simulator", 
        "sport", "strategy", "turn_based_strategy", "tactical",
        "hand_and_slash", "quiz_trivia"
    ]

    other_profiles = Profile.objects.exclude(id=profile.id)
    matches = []

    for other in other_profiles:
        other_genres = Genre_Scores.objects.get(profile_id=other)
        distance = 0
        for field in genre_fields:
            user_score = getattr(user_genres, field)
            other_score = getattr(other_genres, field)
            distance += abs(user_score - other_score)

        matches.append({
            'profile': other,
            'distance': distance
        })

    matches.sort(key=lambda x: x['distance'])  # Low distance = better match
    return matches
