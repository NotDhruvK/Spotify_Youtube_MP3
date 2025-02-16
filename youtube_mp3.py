from pytubefix import YouTube
import os

def download_audio(song_link, out_path):
    '''
        This function downloads the audio from the provided Youtube link
        params:
            song_link: String. The link to the videos that is to be downloaded.
            out_path: String. The path of your preffered download location.
    '''
    yt = YouTube(f"{song_link}")
    video = yt.streams.filter(only_audio=True).first()

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    try:
        # download the file
        out_file = video.download(output_path=out_path)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'

        # Check if the file already exists
        if os.path.exists(new_file):
            print(f"File {new_file} already exists, generating a unique name.")
            # Add a suffix to the filename to make it unique
            i = 1
            while os.path.exists(f"{base}_{i}.mp3"):
                i += 1
            new_file = f"{base}_{i}.mp3"

        # Rename the file to the new name
        os.rename(out_file, new_file)

        # result of success
        print(yt.title + " has been successfully downloaded.")

    except Exception as e:
        print(f"An error occured: {e}")