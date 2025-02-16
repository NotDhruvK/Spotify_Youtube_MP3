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
    '''
        This function is used to get the spotify token based on Cliend ID and Client Secret

        params:
            NONE
        returns:
            token: String
    '''
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

    # print(token)
    return token


def get_auth_header(token):
    '''
        This function just reformats the token into the required string
        returns:
            String
    '''
    return {"Authorization": "Bearer " + token}


def get_playlist_url():
    '''
        This takes in the Spotify playlist link and then returns the Spotify Playlist ID
        returns:
            playlist_id: String
    '''
    url = input("Enter the URL of the Spotify playlist: ")
    playlist_id = url[34:56]

    return playlist_id


def get_playlist_tracks(token, playlist_id):
    '''
        This function gets the tracks of a spotify playlist and returns it in a list format.
        params:
            token: String
            playlist_id: string
        returns:
            json_results: dictionary object
    '''
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?fields=items%28added_by.id%2Ctrack%28name%29%29"
    headers = get_auth_header(token)
    result = requests.get(url, headers=headers)
    json_results = json.loads(result.content)

    # print(json_results)
    return json_results


def json_to_list(json_results):
    '''
        This function converts the dictionary object into a list object
        params:
            json_results: Dictionary
        returns:
            song_names: List
    '''
    song_names = []
    for result in json_results["items"]:
        # print(result["track"]["name"])
        song_names.append(result["track"]["name"])  

    return song_names  


def get_user_playlists(token, user_id):
    '''
        This is a test funtion which was written in order to get the Spotify user information
        params:
            token: String
            user_id: String
        returns: 
            json_results: Dictionary Object
    '''
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = get_auth_header(token)
    result = requests.get(url, headers=headers)
    json_results = json.loads(result.content)  
    
    # print(json_results)
    return json_results


def get_spotify_songs():
    '''
        This function is the main driver function which will be used to get the final spotify song list 
        params:
            NONE
        returns: 
            song_names: List
    '''
    token = get_token()
    playlist_id = get_playlist_url()
    get_playlist_tracks(token, user_id)
    json_results = get_playlist_tracks(token, playlist_id)

    song_names = json_to_list(json_results)
    print("These are the songs in this playlist: ")
    for song in song_names:
        print("\t" + song)
    
    return song_names


if __name__ == "__main__":
    get_spotify_songs()