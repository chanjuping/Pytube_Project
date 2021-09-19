from pytube import YouTube
while True:
    #For user to insert video's url
    input_url = (input('Insert url: '))
    #Displaying an error if the provided url isn't valid
    try:
        youtube = YouTube(input_url)
        print(f'Downloading link: {input_url}')
        print(f'Downloading video: {youtube.title}')
    except:
        print('An error has occurred, please try again.\n')
        continue
    #To download video, followed up by the destination of the download
    youtube.streams.first().download("")
    print('Download success!')
    #Asking the user whether they would like to continue or not
    quit_continue = (input('Would you like to continue? (Y)es/(N)o \n> ')).lower()
    if quit_continue == 'n':
        print('Thank you for using our programme, have a nice day!')
        break
    elif quit_continue == 'y':
        print('')
        continue
