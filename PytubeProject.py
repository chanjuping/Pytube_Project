import os
from pytube import YouTube
from colorama import init, Fore

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def download_video(url, quality_pref="high", folder="PytubeVideos"):
    try:
        yt = YouTube(url)
        stream = (yt.streams.get_highest_resolution() if quality_pref == "high"
                  else yt.streams.get_lowest_resolution() if quality_pref == "low"
                  else yt.streams.filter(res=quality_pref).first())

        os.makedirs(folder, exist_ok=True)
        title = yt.title.replace(' ', '_')
        print(Fore.YELLOW + '\nDownloading...')
        file_name = f"{title}_{quality_pref}.{stream.subtype}"
        stream.download(folder, filename=file_name)
        print(Fore.GREEN + f'\nSuccess! Saved to {folder}/{file_name}')
        return True
    except Exception as e:
        print(Fore.RED + f'\nAn error has occurred: {e}\nPlease try again.')
        return False

def main():
    clear()

    while True:
        url = input(Fore.CYAN + 'YouTube URL: ')
        quality = input(Fore.CYAN + '\nQuality (high/low/720p/1080p, etc.): ')

        if download_video(url, quality):
            break

if __name__ == "__main__":
    main()
