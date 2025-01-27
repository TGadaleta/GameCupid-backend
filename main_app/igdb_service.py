import requests
from django.conf import settings

def get_igdb_token():
    """Obtain a new IGDB token using Twitch credentials."""
    token_url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": settings.TWITCH_CLIENT_ID,
        "client_secret": settings.TWITCH_CLIENT_SECRET,
        "grant_type": "client_credentials",
    }
    token_response = requests.post(token_url, data=params)
    if token_response.status_code == 200:
        return token_response.json().get("access_token")
    return None

def search_games(query):
    """Search for games in IGDB by query string."""
    access_token = get_igdb_token()
    if not access_token:
        return []

    endpoint = "https://api.igdb.com/v4/games"
    headers = {
        "Client-ID": settings.TWITCH_CLIENT_ID,
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json"
    }

    data = f"""fields name, genres; search "{query}"; limit 20;"""
    response = requests.post(endpoint, headers=headers, data=data)
    if response.status_code == 200:
        games = response.json()
        game_names_and_genres = []
        for game in games:
            genre_names = []
            genre_ids = game.get('genres', [])
            if genre_ids:
                genre_endpoint = "https://api.igdb.com/v4/genres"
                genre_data = f"fields name; where id = ({','.join(map(str, genre_ids))});"
                genre_response = requests.post(genre_endpoint, headers=headers, data=genre_data)
                if genre_response.status_code == 200:
                    genres = genre_response.json()
                    genre_names = [genre['name'] for genre in genres]
            game_names_and_genres.append((game['name'], genre_names))
            games_json = [
                {"title": game_name, "genre": genre_names}
                for game_name, genre_names in game_names_and_genres
            ]
        return games_json
    else:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Failed to fetch games from IGDB: {response.status_code} - {response.text}")


