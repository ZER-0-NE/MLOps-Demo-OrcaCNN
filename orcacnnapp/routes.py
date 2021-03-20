from flask import request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
import os
from PreProcessing import preprocess_chunk_img
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import base64

from orcacnnapp import app


