import requests
import wget
import pafy as pa
from bs4 import BeautifulSoup as soup
def name_converter(x):
	p=requests.get('https://www.youtube.com/results?search_query={}'.format('+'.join(x.split())))
	soupp=soup(p.text,'html.parser')
	lis = soupp.findAll('a', attrs={'class':'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link'})
	o=str(lis)[220:280]
	import re
	a = re.search(r'\b(watch)\b',o)
	return 'https://www.youtube.com/watch?v={}'.format(o[a.start()+8:a.start()+19])

def downloadlinks(x,mp3=False):
	v= pa.new(x)
	
	if mp3==True:
		s=v.getbestaudio()
		return s.url
	s = v.getbestvideo()
	#p={}
	#for s in streams:
		#p.update({s.resolution:s.url})
	return s.url

