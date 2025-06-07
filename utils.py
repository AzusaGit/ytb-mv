import os
import shutil
import sys
from pathlib import Path

from tqdm import tqdm
import ytdlp

def read_links_from_file(file_path: str) -> list[str]:
    """
    Reads a .txt file line by line and returns a list of links.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("file not found")

    with open(file_path, encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]
    
def start_conversion(links: list[str], fmt: str, output_path: str, quality: str):
    """
    Converts each link using ytdlp.
    """
    Path(output_path).mkdir(parents=True, exist_ok=True)
    print("Starting conversion...")

    for link in tqdm(links, desc="Downloading"):
        try:
            ytdlp.download_convert(link, output_path, fmt, quality)
        except Exception as e:
            print(f"error with link {link}: {e}")


def find_ffmpeg():
    """
    Adds FFmpeg binary path to environment PATH.
    """
    ffmpeg_path = shutil.which("ffmpeg")
    if ffmpeg_path is None:
        print("error: FFmpeg not found. Checked path:", ffmpeg_path)
        sys.exit(1)

    return ffmpeg_path