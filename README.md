# YouTube Multi Converter

Converts a batch of links from a text file to desired output.

## Prequisites

You will need to download `ffmpeg` and set it up in your environment variables.
You can download ffmpeg here: https://ffmpeg.org/download.html or by using a package manager.

## How to use

Download the `.exe` file in the release page, then create a new environment variable with the path to the `.exe` file.
Prepare a `.txt` file with a link on each line, for example:

```
https://www.youtube.com/watch?v=[link1]
https://www.youtube.com/watch?v=[link2]
https://www.youtube.com/watch?v=[link3]
...
```

Then run the command:

`yt-mv [filename] [output_format]`

To see more options or docs, run `--help`.
