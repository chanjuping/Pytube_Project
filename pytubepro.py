import os
from pytube import YouTube

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def download_video(url, quality="high", folder="PytubeVideos"):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution() if quality == "high" else yt.streams.filter(res=quality).first() or yt.streams.filter(res="360p").first()

        file_name = f"{yt.title.replace(' ', '_')}_{quality}.{stream.subtype}"
        os.makedirs(folder, exist_ok=True)

        print('\nDownloading...')
        stream.download(folder, filename=file_name)
        print(f'\nSuccess! Saved to {folder}/{file_name}')
        return True
    except Exception as e:
        print(f'\nError: {e}\nPlease try again.')
        return False

if __name__ == "__main__":
    clear()
    print('PytubePro')

    while not download_video(input('\nYouTube URL: '), input('\nQuality (high/low/720p/1080p, etc.):')):
        pass
