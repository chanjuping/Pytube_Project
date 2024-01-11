import os
from pytube import YouTube
from colorama import init, Fore

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
print(Fore.BLUE + 'PytubePro')

def get_input():
    return input(Fore.CYAN + '\nYouTube URL: '), input(Fore.CYAN + 'Quality (high/low/720p/1080p, etc.): ')

url, quality = get_input()

def download(url, quality="high", folder="PytubeVideos"):
    try:
        yt = YouTube(url)
        stream = (yt.streams.get_highest_resolution() if quality == "high"
                  else yt.streams.get_lowest_resolution() if quality == "low"
                  else yt.streams.filter(res=quality).first())

        os.makedirs(folder, exist_ok=True)
        title, subtype = yt.title.replace(' ', '_'), stream.subtype
        print(Fore.YELLOW + '\nDownloading...')
        file_name = f"{title}_{quality}.{subtype}"
        stream.download(folder, filename=file_name)
        print(Fore.GREEN + f'\nDownload success! Saved to {folder}/{file_name}')
        return True
    except Exception as e:
        print(Fore.RED + f'\nAn error has occurred: {e}\nPlease try again.')
        return False

def main():
    while not download(url, quality):
        pass

if __name__ == "__main__":
    main()
