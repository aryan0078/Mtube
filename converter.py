import os
from downloader import *
import pafy as p
import os
class Mtube:
    def __init__(self,name):
        try:
            os.chdir('./songs')
            if len(os.listdir())>10:
                self.cleaner()
            self.name=name
            self.songurl=self.name_converter(name)
            self.filename=self.namel()
        except:
            if len(os.listdir())>10:
                self.cleaner()
            self.name=name
            self.songurl=self.name_converter(name)
            self.filename=self.namel()
        #print(self.filename)
    def name_converter(self,x):
        p=requests.get('https://www.youtube.com/results?search_query={}'.format('+'.join(x.split())))
        soupp=soup(p.text,'html.parser')
        lis = soupp.findAll('a', attrs={'class':'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link'})
        o=str(lis)[220:280]
        import re
        a = re.search(r'\b(watch)\b',o)
        return 'https://www.youtube.com/watch?v={}'.format(o[a.start()+8:a.start()+19])
    def converter(self):
        from pydub import AudioSegment
        
        for i in os.listdir():
            if i.endswith('webm'):
                AudioSegment.from_file(i).export(i[:-5]+'.mp3', format="mp3")
                os.remove(i)
    def d(self):
        video=p.new(self.songurl)
        best=video.getbestaudio()
        print("########DOWNLOADING SONG#########")
        best.download()
        return video.title
    def m(self):
        if self.check():
            return self.filename
        self.d()
        self.converter()
        return self.filename
    def namel(self):
        video=p.new(self.songurl)
        best=video.getbestaudio()
        return video.title+'.mp3'
    def stream(self):
        video=p.new(self.songurl)
        best=video.getbestaudio()
        return best.url
    def cleaner(self):
        for i in os.listdir():
            if i.endswith('mp3'):
                os.remove(i)
    def check(self):
        for i in os.listdir():
            #print(i)
            if i==self.filename:
                return True

    
    