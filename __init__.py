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
		if quality=='mp3':
			link=link_extractor(name_converter(name),mp3=True)
			return redirect(link)
		else:
			link=link_extractor(name_converter(name),quality)
			return redirect(link)

app.run()
