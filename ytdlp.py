import os

from yt_dlp import YoutubeDL

def download_convert(link: str, output_path: str, format: str, quality: str):
    """
    Download and convert links to the desired output format
    """
    ydl_config = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": format,
            "preferredquality": quality,
        }],
        "quiet": True,
    }

    with YoutubeDL(ydl_config) as ydl:
        ydl.download([link])
