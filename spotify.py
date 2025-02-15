import requests
from dotenv import load_dotenv
import os
import base64
import json

load_dotenv()
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
user_id = os.getenv("SPOTIFY_USER_ID")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]

    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def get_playlist_tracks(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=items%28added_by.id%2Ctrack%28name%29%29"
    headers = get_auth_header(token)
    result = requests.get(url, headers=headers)
    json_results = json.loads(result.content)
    print(json_results)


def get_user_playlists(token, user_id):
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = get_auth_header(token)
    result = requests.get(url, headers=headers)
    json_results = json.loads(result.content)  
    print(json_results)

playlist_id = '4doZOuUtOWTDDFIo177NUB'

if __name__ == "__main__":
    token = get_token()
    #get_playlist_tracks(token, user_id)
    get_playlist_tracks(token, playlist_id)
