'''
    Nothing Works in ths code so far. 
    We have tried using Pafy and pytube.
'''
from pytube import YouTube
import os

userName = os.getenv('username')
#print(userName)

DOWNLOAD_PATH = f'C:/Users/{userName}/Desktop'

url = 'https://www.youtube.com/watch?v=PizHX6Kuy1M'
video = YouTube(url)

video = video.streams.get_audio_only()
video.download()