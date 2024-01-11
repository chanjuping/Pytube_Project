import os
from pytube import YouTube
from colorama import init, Fore

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def download_video(url, quality_pref="highest", folder="PytubeVideos"):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution() if quality_pref == "highest" else \
                 yt.streams.get_lowest_resolution() if quality_pref == "lowest" else \
                 yt.streams.filter(res=quality_pref).first()

        os.makedirs(folder, exist_ok=True)
        title = yt.title.replace(' ', '_')
        print(Fore.YELLOW + 'Downloading video...')
        file_extension = stream.subtype
        file_name = f"{title}_{quality_pref}.{file_extension}"
        stream.download(folder, filename=file_name)
        print(Fore.GREEN + f'\nDownload success! Saved to {folder}/{file_name}')
        return True
    except Exception as e:
        print(Fore.RED + f'An error has occurred: {e}\nPlease try again.')
        return False

def main():
    clear()

    while True:
        url = input(Fore.CYAN + 'Insert URL: ')
        quality = input(Fore.CYAN + 'Enter video quality preference (highest/lowest/720p/1080p, etc.): ')

        if download_video(url, quality):
            break

if __name__ == "__main__":
    main()
