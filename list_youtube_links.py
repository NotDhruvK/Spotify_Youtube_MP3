import urllib.request
from dotenv import load_dotenv
import os
import re

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
# youtube = build('youtube', 'v3', developerKey=api_key)

def add_lyrics(random_list):
    '''
        This function will add the string "lyrics" to every item in a list.
        params:
            random_list: List
        returns: 
            updated_list: List
    '''
    updated_list = []
    for item in random_list:
        item = item + " lyrics"
        updated_list.append(item)

    return updated_list


def search_for_song(song_name):
    '''
        This function returns the youtube link for the song name in the parameter
        params:
            song_name: String. The name of the song
        returns:
            final_link: The final youtube link.

    '''
    song_name = song_name.replace(" ", "+")
    html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={song_name}")
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    final_link = f"https://www.youtube.com/watch?v={video_ids[0]}"
    print(f"Got link for: {song_name}")

    return final_link
    

if __name__ == "__main__":
    random_list = ["Challeya", "Sooraj Dooba hai yaaron", "Rangisaari", "Jeena Jeena"]
    updated_list = add_lyrics(random_list)

    final_link = search_for_song("arjan vailly lyrics")
    print(final_link)