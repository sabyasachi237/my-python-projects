from pytube import YouTube

link="https://youtu.be/IMaVxKjaYD4"
youtube_1=YouTube(link)

videos= youtube_1.streams.all()
vid= list(enumerate(videos))

for i in vid:
    print(i)
strm=int(input("enter:"))
videos[strm].download()
print('successfully')