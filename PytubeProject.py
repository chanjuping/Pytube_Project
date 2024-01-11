from pytube import YouTube
from colorama import init, Fore

init(autoreset=True)

def get_user_input():
    url = input('Insert URL: ')
    quality_preference = input('Enter video quality preference (highest/lowest/720p/1080p, etc.): ')
    destination = input('Enter custom download destination (press Enter for current directory): ')
    return url, quality_preference, destination

def download_video(url, quality="highest", destination=""):
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

        # Download the selected stream to the specified destination or the current working directory
        video_stream.download(destination)
        print(Fore.GREEN + 'Download success!')
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
        url, quality, custom_destination = get_user_input()

        # Download video and check if successful
        if download_video(url, quality, custom_destination):
            # Ask the user if they want to continue or exit
            quit_continue = input('Would you like to continue? (Y)es/(N)o \n> ').lower()

            if quit_continue == 'n':
                print(Fore.CYAN + 'Thank you for using our program. Have a nice day!')
                break
            elif quit_continue == 'y':
                print('')
                continue
            else:
                # Handle invalid input
                print(Fore.YELLOW + 'Invalid input. Please enter either "Y" or "N".\n')
                continue

if __name__ == "__main__":
    main()
