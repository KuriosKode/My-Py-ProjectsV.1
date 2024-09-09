print("YT video playlist Dowloader...")


from pytube import  YouTube

def download_playlist(url,download_path):
    playlist =  playlist(url)

    print(f'Downloading playlist : {playlist.title}')

    for video in playlist.videos:
        print(f'Downloading {video.title}...')
                                            
    video.streams.get_highest_resolution().download(download_path)
    print(f'Download Finished')

    if __name__=="__main__":
         url =  "enter your url here"

         download_path = "insert download path here"

        #  Download the playlist...
download_playlist(url,download_path)