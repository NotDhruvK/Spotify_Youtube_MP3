import os
from dotenv import load_dotenv
from spotify import get_spotify_songs
from list_youtube_links import add_lyrics, search_for_song
from youtube_mp3 import download_audio

if __name__ == "__main__":
    load_dotenv()
    userName = os.getenv("username")

    # Make a directory name "Songs" on the desktop
    temp_path = f"C:/Users/{userName}/Desktop/Songs"
    os.makedirs(temp_path)
    DOWNLOAD_PATH = temp_path

    song_list = get_spotify_songs()
    update_song_list = add_lyrics(song_list)

    for song in update_song_list:
        link = search_for_song(song)
        download_audio(link, DOWNLOAD_PATH)
