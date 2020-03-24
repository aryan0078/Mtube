from flask import Flask,redirect, url_for, request, render_template,send_file
from downloader import *
from converter import *
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
			m(name)
			return render_template("download.html")
		else:
			#r={'720p':'1280x720','480p':'720x480','144p':'256x144'}
			#r=r[quality]
			link=downloadlinks(name_converter(name))
			return redirect(link)
@app.route('/return-files/')
def return_files_tut():
	try:
		return send_file(mp3f(), attachment_filename=mp3f(),as_attachment=True)
	except Exception as e:
		return str(e)
app.run()
