import os
import sys
import utils

import argparse

SUPPORTED_FORMATS = ["mp3", "wav", "aac", "flac", "m4a"]

def main():
    parser = argparse.ArgumentParser(description="Batch download and convert YouTube links from a text file.")

    parser.add_argument("file", help="Input file path (.txt only)")
    parser.add_argument("format", choices=SUPPORTED_FORMATS, help="Output audio format")
    parser.add_argument("-o", "--output", default="./", help="Output directory path")
    parser.add_argument("-q", "--quality", default="192", help="Audio quality (e.g. 192)")

    args = parser.parse_args()

    if not args.file.lower().endswith(".txt"):
        print("error: input file must have a .txt extension")
        sys.exit(1)

    try:
        links = utils.read_links_from_file(args.file)
    except Exception as e:
        print(f"error: {e}")
        sys.exit(1)

    utils.start_conversion(links, args.format, args.output, args.quality)

if __name__ == "__main__":
    # Set ffmpeg
    os.environ["PATH"] += utils.find_ffmpeg()
    main()