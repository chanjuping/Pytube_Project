import os
from pytube import YouTube
from colorama import init, Fore

init(autoreset=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input():
    url = input(Fore.CYAN + 'YouTube URL: ')
    quality_preference = input(Fore.CYAN + 'Quality (high/low/720p/1080p): ')
    return url, quality_preference

def download_video(url, quality="high", folder="PytubeVideos"):
    try:
        youtube = YouTube(url)

        # Get the appropriate stream based on quality preference
        if quality == "high":
            video_stream = youtube.streams.get_highest_resolution()
        elif quality == "low":
            video_stream = youtube.streams.get_lowest_resolution()
        else:
            video_stream = youtube.streams.filter(res=quality).first()

        # Create the folder if it doesn't exist
        os.makedirs(folder, exist_ok=True)

        # Replace spaces with underscores in the video title
        video_title = youtube.title.replace(' ', '_')

        print(Fore.YELLOW + 'Downloading...')

        # Download the selected stream to the specified destination or the current working directory
        video_stream.download(folder, filename=video_title + '.' + video_stream.subtype)

        print(Fore.GREEN + f'\nSucess! Saved to {folder}/{video_title}.{video_stream.subtype}')
        return True
    except Exception as e:
        print(Fore.RED + f'An error has occurred: {e}\nPlease try again.')
        return False

def main():
    clear_terminal()

    while True:
        url, quality = get_user_input()

        # Download video and check if successful
        if download_video(url, quality):
            break

if __name__ == "__main__":
    main()
