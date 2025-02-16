'''
    Nothing Works in ths code so far. 
    We have tried using Pafy and pytube.
'''
from pytubefix import YouTube
import os

def download_audio(song_link, out_path):
    yt = YouTube(f"{song_link}")
    video = yt.streams.filter(only_audio=True).first()

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # download the file
    out_file = video.download(output_path=out_path)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")


userName = os.getenv('username')

DOWNLOAD_PATH = f'C:/Users/{userName}/Desktop'
url = 'https://www.youtube.com/watch?v=PizHX6Kuy1M'

if __name__ == "__main__":
    download_audio("https://www.youtube.com/watch?v=3l53hACPeYI", DOWNLOAD_PATH)
    