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
		#print(name)
		
		if quality=='mp3':
			global c_s
			os.chdir(os.getcwd()+'/songs')
			for i in os.listdir():
				print(i)
				if i==namel(name):
					return render_template("download.html",sr=stream(name),fn=namel(name))
			#c_s=m(name)
			return '<h1>test</h1>'
			#return render_template("download.html",sr=stream(name),fn=namel(name))
		else:
			link=downloadlinks(name_converter(name))
			return redirect(link)
@app.route('/multi')
def multi():
	if request.method=='POST':
		name=request.form['name']
		#print(name)
		return render_template("download.html",sr=stream(name))

@app.route('/return-files/<name>')
def return_files_tut(name):
	try:
		f=os.getcwd()+'/'+name
		return send_file(f, attachment_filename=f,as_attachment=True)
	except Exception as e:
		return str(e)

app.run()