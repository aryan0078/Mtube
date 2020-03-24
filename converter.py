import os
from downloader import *
import pafy as p
def webmf():
    for i in os.listdir():
        if i.endswith('webm'):
            return i
def mp3f():
    for i in os.listdir():
        if i.endswith('mp3'):
            return i
def converter(y):
    from pydub import AudioSegment
    os.remove(mp3f())
    x=webmf()
    
    AudioSegment.from_file(x).export(y+'.mp3', format="mp3")
def d(x):
    video=p.new(name_converter(x))
    best=video.getbestaudio()
    print("########DOWNLOADING SONG#########")
    best.download()  
    return video.title  
def m(x):
   
    converter(d(x))
    os.remove(webmf())
    return mp3f()


    
    