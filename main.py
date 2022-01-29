import urllib.request
from pytube import YouTube
import os
import re



#GETTING USER INPUT
query=input("Enter Query ").split()
str=""
for i in query:
    str=str+i+"+"
print(f"showing results for the query {str}")

#GETTING URL
pattern=r"watch\?v=(\S{11})"
html=urllib.request.urlopen(f"https://www.youtube.com/results?search_query={str}")
videoID=re.findall(pattern,html.read().decode())


for i in range(10):
    url=f"https://www.youtube.com/watch?v={videoID[i]}"
    vid=YouTube(url)
    s=f"{i+1}. "+f"{vid.title}"
    print(s)

req=int(input("Enter the serial number of the video you're looking for: "))
urlfinal=f"https://www.youtube.com/watch?v={videoID[req-1]}"
myvid=YouTube(urlfinal)

format=input("Do you want a video or an audio file? ")
if(format=="video"or format=="VIDEO" or format=="Video" or format=="mp4"):
    fm=".mp4"
elif(format=="audio"or format=="AUDIO" or format=="Audio" or format=="mp3"):
    fm=".mp3"
else:
    print("Wrong input :(")

if (fm==".mp4"):
    myvid=myvid.streams.get_highest_resolution()
elif(fm==".mp3"):
    myvid=myvid.streams.get_by_itag(140)



myvid.download(filename=f"{myvid.title}.{fm}")

print("Your file is ready")

