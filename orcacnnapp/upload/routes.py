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

from PreProcessing import preprocess_chunk_img


upload = Blueprint('upload', __name__)


@upload.route('/upload', methods=['GET', 'POST'])
def upload_file():
    filename = request.args['filename']
    preprocess_chunk_img.main(classpath='uploads',
                              resampling=44100, chunks=1, silent=False)

    # remove the uploaded file once images are created
    os.remove("uploads/"+filename)
    return "Uploaded successfully"
    # fig = Figure()
    # axis = fig.add_subplot(1, 1, 1)
    # axis.set_title("title")
    # axis.set_xlabel("x-axis")
    # axis.set_ylabel("y-axis")
    # axis.grid()
    # axis.plot(range(5), range(5), "ro-")

    # # Convert plot to PNG image
    # pngImage = io.BytesIO()
    # FigureCanvas(fig).print_png(pngImage)

    # # Encode PNG image to base64 string
    # pngImageB64String = "data:image/png;base64,"
    # pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    # return render_template("upload.html", image=pngImageB64String)
