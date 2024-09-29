import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'best',  # best quality format
        'outtmpl': './%(title)s.%(ext)s'  # output directory and filename format
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

video_url = 'https://www.youtube.com/watch?v=6c2m0RjwRPY'
download_video(video_url)