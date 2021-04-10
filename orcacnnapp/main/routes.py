from flask import Blueprint

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

import logging

from flask import current_app

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')


@main.route('/home', methods=['GET', 'POST'])
def get_input_image():
    if request.method == 'GET':
        return render_template('home.html')

    if request.method == 'POST':
        if 'audio_file' not in request.files:
            flash('No file was uploaded.')  # TODO: catch error
            return redirect(request.url)

    uploaded_file = request.files['audio_file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
            return "Invalid upload", 400  # TODO: do proper error handling
        uploaded_file.save(os.path.join(
            current_app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('upload.upload_file_and_display',  filename=filename))
    flash('No file was uploaded.')  # TODO: catch error
    return redirect(request.url)


@main.route('/about')
def about():
    return render_template('about.html')
