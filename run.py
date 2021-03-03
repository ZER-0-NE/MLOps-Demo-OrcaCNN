import os, sys, glob
import cv2

from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image


UPLOAD_FOLDER = 'uploads/'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_EXTENSIONS'] = ['.wav']


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		uploaded_file = request.files['file']
		filename = secure_filename(uploaded_file.filename)
		if filename != '':
			file_ext = os.path.splitext(filename)[1]
			if file_ext not in app.config['UPLOAD_EXTENSIONS']:
				abort(400)
			uploaded_file.save(uploaded_file.filename)
		
		return redirect(url_for('home'))
	return render_template('upload.html')

@app.route('/about')
def about():
	return render_template('about.html')



if __name__ == '__main__':
	app.run(debug = True)


