from flask import Blueprint

import os
import sys
import glob

from flask import Flask, flash, request, redirect, url_for, render_template, Response, render_template_string
from flask import send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image

import io
import base64

from io import BytesIO
import os
import glob
import argparse


import logging

from PreProcessing import preprocess_chunk_img
from flask import current_app

WIDTH = 640
HEIGHT = 640

upload = Blueprint('upload', __name__)


@upload.route('/upload', methods=['GET', 'POST'])
def upload_file_and_display():
    filename = request.args['filename']
    preprocess_chunk_img.main(classpath='uploads',
                              resampling=44100, chunks=1, silent=False)

    # remove the uploaded file once images are created
    try:
        os.remove("uploads/"+filename)
    except Exception as e:
        pass # on refresh

    images = []
    for root, dirs, files in os.walk(current_app.config['IMAGE_FOLDER']):
        for filename in [os.path.join(root, name) for name in files]:
            if not filename.endswith('.png'):
                continue
            im = Image.open(filename)
            w, h = im.size
            aspect = 1.0*w/h
            if aspect > 1.0*WIDTH/HEIGHT:
                width = min(w, WIDTH)
                height = width/aspect
            else:
                height = min(h, HEIGHT)
                width = height*aspect
            images.append({
                'width': int(width),
                'height': int(height),
                'src': filename
            })
    return render_template('upload.html', **{
        'images': images
    })


@upload.route('/<path:filename>')
def image(filename):
    try:
        im = Image.open(filename)
        io = BytesIO()
        im.save(io, format='PNG')
        return Response(io.getvalue(), mimetype='image/jpeg')

    except IOError:
        return render_template('errors/404.html'), 404

    return send_from_directory(current_app.config['IMAGE_FOLDER'], filename)
