import youtube_dl
import fade

title=fade.fire("""
█▀▀ █░█ █▀█ █▄░█ █▄▀ ░ █▀▀ █▀█ █▄░█ █░█
█▄▄ █▀█ █▄█ █░▀█ █░█ ▄ █▄▄ █▄█ █░▀█ ▀▄▀
Made by Erwin.""")
print(title)
print("""1 - mp3
2 - mp4""")

choice = input("[Type]:")

if choice == 1:
    type_v = False
else:
    type_v = True

def main():
    try:
        
        video_url = input("[Link]:")
        video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)

        filename = (f"{video_info['title']}.mp3")
        
        options={
            'format':'bestaudio/best',
            'keepvideo':choice,
            'outtmpl':filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        print(f"Succesfully downloaded {filename}. Location: where is 'Chonker_conv.exe'.")
        main()
    except:
        print(fade.fire(f"Failed to download '{filename}'"))
        main()


main()