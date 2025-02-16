# Spotify Playlist Downloader

This Python script allows you to download user-made **public Spotify playlists** to your local system. It is run via the command line by executing `driver.py`.

## Requirements

**Download this repository on your machine.**
Before running the script, ensure that you have installed the required dependencies. Installing the dependencies in a virtual environment is recommended. Follow [this](https://www.youtube.com/watch?v=Y21OR1OPC9A) tutorial to create and activate a virtual environment.

To install the required libraries, use the following command:

```bash
pip install -r requirements.txt
```

You are also required to have the following credentials:

1. Spotify Client ID
2. Spotify Client Secret

In order to get these credentials follow [this](https://www.youtube.com/watch?v=0fhkkkRuUxw) tutorial.

Create a `.env` file in the working directory and add these in the file:

```
SPOTIFY_CLIENT_ID="your_client_id"
SPOTIFY_CLIENT_SECRET="your_client_secret"
```

### Navigate to the project directory

```bash
cd spotify-playlist-downloader
```

### Run the Script

```bash
python driver.py
```

## Things to remember

1. Do not have a directory named "Songs" on your desktop (Windows only)
2. Only use **User-made and Public playlists**.
3. **DO NOT USE PLAYLISTS MADE BY SPOTIFY**
