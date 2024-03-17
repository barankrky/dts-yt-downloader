import pytube
import userpaths
from pathlib import Path
from pytube.cli import on_progress
from pytube.exceptions import RegexMatchError

download_path = str(Path.home)

def DownloadVideo(videoUrl):
    try:
        video_client = pytube.YouTube(videoUrl, on_progress_callback=on_progress)
        video_stream = video_client.streams.get_highest_resolution()
        video_stream.download(output_path=download_path)
        return("Download complete, check the Downloads folder")
    except RegexMatchError:
        return("URL is wrong or video not found. Please enter a valid Youtube URL.")

#boyna başarılı bir şekilde dolandı.