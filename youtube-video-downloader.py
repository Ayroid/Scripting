import yt_dlp as youtube_dl
from feedparser import parse
import os


def download_latest_videos(subscription_feed_url, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    feed = parse(subscription_feed_url)

    for entry in feed.entries[:5]:
        video_url = entry.link
        try:
            ydl_opts = {
                "outtmpl": f"{output_folder}/%(title)s.%(ext)s",
                "format": "best",
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            print(f"Downloaded: {entry.title}")
        except Exception as e:
            print(f"Failed to download {entry.title}! Error: {e}")


CHANNEL_NAME = "Fireship"  # Fireship Channel Name
OUTPUT_FOLDER = f"/home/ayroid/Downloads/youtube/{CHANNEL_NAME}"  # Output Folder
CHANNEL_URL = f"https://www.youtube.com/feeds/video.xml?channel_id=UCsBjURrPoezykLs9EqgamOA"  # Fireship Channel URL

download_latest_videos(
    CHANNEL_URL,
    OUTPUT_FOLDER,
)
