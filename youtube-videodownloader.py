import yt_dlp

def download_video(url, quality_choice):
    # Define options for yt-dlp
    ydl_opts = {
        'format': quality_choice,  # Quality choice specified by user
        'outtmpl': '%(title)s.%(ext)s',  # Output file name will be the video title
        'noplaylist': True,  # Only download the single video, not the playlist
    }

    try:
        # Create a YoutubeDL object with the options defined above
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video in {quality_choice} quality...")
            ydl.download([url])
            print("Download completed successfully!")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Input video URL from the user
    url = input("Enter the YouTube video URL: ")

    # Fetch available formats and qualities using yt-dlp
    with yt_dlp.YoutubeDL() as ydl:
        result = ydl.extract_info(url, download=False)

    # Display available formats and resolutions
    formats = result.get('formats', [])
    available_qualities = {}
    print("Available qualities:")

    for i, fmt in enumerate(formats, 1):
        if fmt.get('vcodec') != 'none':  # Only consider video formats (skip audio-only formats)
            quality = fmt.get('format_note', 'unknown')
            available_qualities[quality] = fmt
            print(f"{i}. {quality} ({fmt.get('height', 'N/A')}p)")

    # Ask the user for the desired quality
    quality_choice = input("Enter the quality you want to download (e.g., 1080p, best, worst): ")

    # Check if the quality exists in the available options
    if quality_choice in available_qualities:
        download_video(url, available_qualities[quality_choice]['format_id'])
    else:
        print("Invalid choice. Please select a valid quality.")

if __name__ == "__main__":
    main()
