from flask import Flask,redirect, url_for, request, render_template,send_file
from downloader import *
from converter import *
app=Flask(__name__)
import os
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
			global c_s
			c_s=m(name)
			
			return render_template("download.html",sr=stream(name))
		else:
			#r={'720p':'1280x720','480p':'720x480','144p':'256x144'}
			#r=r[quality]
			link=downloadlinks(name_converter(name))
			return redirect(link)
@app.route('/return-files/')
def return_files_tut():
	try:
		f=os.getcwd()+'/'+c_s
		return send_file(f+'.mp3', attachment_filename=f+'.mp3',as_attachment=True)
	except Exception as e:
		return str(e)
app.run(port=8000)
