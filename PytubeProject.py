import os
from pytube import YouTube
from colorama import init, Fore

init(autoreset=True)

def get_user_input():
    url = input(Fore.CYAN + 'Insert URL: ')
    quality_preference = input(Fore.CYAN + 'Enter video quality preference (highest/lowest/720p/1080p, etc.): ')
    return url, quality_preference

def download_video(url, quality="highest", folder="PytubeVideos"):
    try:
        youtube = YouTube(url)
        print(f'Downloading link: {url}')
        print(f'Downloading video: {youtube.title}')

        # Get the appropriate stream based on quality preference
        if quality == "highest":
            video_stream = youtube.streams.get_highest_resolution()
        elif quality == "lowest":
            video_stream = youtube.streams.get_lowest_resolution()
        else:
            video_stream = youtube.streams.filter(res=quality).first()

        # Create the folder if it doesn't exist
        os.makedirs(folder, exist_ok=True)

        # Download the selected stream to the specified destination or the current working directory
        video_stream.download(folder)
        print(Fore.GREEN + f'Download success! Saved to {folder}/')
        return True
    except Exception as e:
        print(Fore.RED + f'An error has occurred: {e}\nPlease try again.')
        return False

def show_progress(stream, chunk, file_handle, bytes_remaining):
    # Display download progress in percentage
    percent = (100 * (stream.filesize - bytes_remaining)) / stream.filesize
    print(f"\rDownloading... {percent:.1f}%", end='', flush=True)

def main():
    while True:
        url, quality = get_user_input()

        # Download video and check if successful
        if download_video(url, quality):
            break

if __name__ == "__main__":
    main()
