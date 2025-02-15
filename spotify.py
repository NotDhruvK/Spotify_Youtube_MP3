import requests
from dotenv import load_dotenv

load_dotenv()

PLAYLIST_LINK = f'https://open.spotify.com/playlist/4doZOuUtOWTDDFIo177NUB?si=1518fba482b745ac&pt=1c295cf9e518c5019586614edf0500f8'
playlist_id = '4tf4C2HPkZtlM6XSkRz6im'

response = requests.get(f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks', auth=('dhruvadam@gmail.com','!Xobile1510'))
print(response.json())
