from pytube import YouTube

video_url = input("Enter the YouTube video URL: ")
yt = YouTube(video_url)

available_streams = yt.streams.filter(progressive=True)
print("Available video quality options:")
for i, stream in enumerate(available_streams, start=1):
    print(f"{i}. {stream.resolution}")

while True:
    try:
        choice = int(input("Enter the number of the desired video quality (e.g., 1 for 360p, 2 for 480p, ): "))
        if 1 <= choice <= len(available_streams):
            selected_stream = available_streams[choice - 1]
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")

download_path = "../videos"    # enter the path where you want to save the mp4 video file

selected_stream.download(output_path=download_path)

print("Downloading Started!")

print(f"Video downloaded to {download_path}")
