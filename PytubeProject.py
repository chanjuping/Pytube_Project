import os
from pytube import YouTube
from colorama import init, Fore

init(autoreset=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input():
    url = input(Fore.CYAN + 'YouTube URL: ')
    quality_preference = input(Fore.CYAN + 'Quality (high/low/720p/1080p, etc.): ')
    return url, quality_preference

def download_video(url, quality="highest", folder="PytubeVideos"):
    try:
        youtube = YouTube(url)

        if quality == "high":
            video_stream = youtube.streams.get_highest_resolution()
        elif quality == "low":
            video_stream = youtube.streams.get_lowest_resolution()
        else:
            video_stream = youtube.streams.filter(res=quality).first()

        os.makedirs(folder, exist_ok=True)

        video_title = youtube.title.replace(' ', '_')

        print(Fore.YELLOW + 'Downloading...')

        file_extension = video_stream.subtype
        video_quality_name = quality.replace('/', '_').replace(' ', '_')
        video_title_with_quality = f"{video_title}_{video_quality_name}.{file_extension}"

        video_stream.download(folder, filename=video_title_with_quality)

        print(Fore.GREEN + f'\nDownload success! Saved to {folder}/{video_title_with_quality}')
        return True
    except Exception as e:
        print(Fore.RED + f'An error has occurred: {e}\nPlease try again.')
        return False

def main():
    clear_terminal()

    while True:
        url, quality = get_user_input()

        if download_video(url, quality):
            break

if __name__ == "__main__":
    main()
