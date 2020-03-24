import os
from downloader import *
import pafy as p
import os
def converter():
    from pydub import AudioSegment
    if len(os.listdir())>10:
        cleaner()
    for i in os.listdir():
        if i.endswith('webm'):
            AudioSegment.from_file(i).export(i[:-5]+'.mp3', format="mp3")
            os.remove(i)
def d(x):
    os.chdir(os.getcwd()+'/songs')
    video=p.new(name_converter(x))
    best=video.getbestaudio()
    print("########DOWNLOADING SONG#########")
    best.download()
    return video.title
def m(x):
    c_s=d(x)
    converter()
    return c_s
def stream(x):
    video=p.new(name_converter(x))
    best=video.getbestaudio()
    return best.url
def cleaner():
    for i in os.listdir():
        if i.endswith('mp3'):
            os.remove(i)

    
    