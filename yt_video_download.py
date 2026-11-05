import yt_dlp
import os

url = input("Enter the URL of the YouTube video: ").strip()

if not url:
    print("Please enter a valid video URL.")
else:
    os.makedirs("downloads", exist_ok=True)

    ydl_opts = {
        "format": "best",
        "outtmpl": "downloads/%(title)s.%(ext)s",
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Download completed!")

    except Exception as error:
        print(f"Something went wrong: {error}")