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

UPLOAD_FOLDER = 'uploads/'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_EXTENSIONS'] = ['.wav', '.WAV']

logging.getLogger('matplotlib.font_manager').disabled = True


from orcacnnapp import routes