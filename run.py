import os
import sys
import glob

from flask import Flask, flash, request, redirect, url_for, render_template
from flask import send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image

import io
import base64

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import os
import glob
import argparse
import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np

from PreProcessing import preprocess_chunk_img
import logging

UPLOAD_FOLDER = 'uploads/'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_EXTENSIONS'] = ['.wav', '.WAV']

logging.getLogger('matplotlib.font_manager').disabled = True


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/home', methods=['GET', 'POST'])
def get_input_image():
    if request.method == 'GET':
        return render_template('home.html')

    if request.method == 'POST':
        if 'audio_file' not in request.files:
            flash('No file was uploaded.') # TODO: catch error
            return redirect(request.url)

    uploaded_file = request.files['audio_file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            return "Invalid upload", 400  # TODO: do proper error handling
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('upload_file',  filename=filename))
    flash('No file was uploaded.')  # TODO: catch error
    return redirect(request.url)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    filename = request.args['filename']
    preprocess_chunk_img.main(classpath=f'uploads/{filename}',
                              resampling=44100, chunks=1, silent=False)
    # return "Uploaded successfully"
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("title")
    axis.set_xlabel("x-axis")
    axis.set_ylabel("y-axis")
    axis.grid()
    axis.plot(range(5), range(5), "ro-")

    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return render_template("upload.html", image=pngImageB64String)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
