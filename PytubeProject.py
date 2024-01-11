import os
from pytube import YouTube
from colorama import init, Fore

init(autoreset=True)
print(Fore.BLUE + 'PytubePro v1.0')

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def get_input():
    return input(Fore.CYAN + 'Insert URL: '), input(Fore.CYAN + 'Quality (high/low/720p/1080p, etc.): ')

def download(url, quality="highest", folder="PytubeVideos"):
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
        print(Fore.GREEN + f'\nSuccess! Saved to {folder}/{file_name}')
        return True
    except Exception as e:
        print(Fore.RED + f'\nAn error has occurred: {e}\nPlease try again.')
        return False

def main():
    clear()
    url, quality = get_input()

    while not download(url, quality):
        pass

if __name__ == "__main__":
    main()
