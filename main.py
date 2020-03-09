from flask import Flask,redirect, url_for, request, render_template
from downloader import *
app=Flask(__name__)
@app.route('/')
def main():
	return render_template('index.html')
@app.route('/download',methods=['POST','GET'])
def download():
	if request.method=='POST':
		name=request.form['name']
		quality=request.form['service']
		print(name)
		if quality=='mp3':
			link=downloadlinks(name_converter(name),mp3=True)
			return redirect(link)
		else:
			#r={'720p':'1280x720','480p':'720x480','144p':'256x144'}
			#r=r[quality]
			link=downloadlinks(name_converter(name))
			return redirect(link)

app.run()
