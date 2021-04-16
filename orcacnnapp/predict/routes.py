import os
import shutil

from flask import request, render_template, Response, current_app
from flask import send_from_directory
from flask import Blueprint
from PIL import Image

from io import BytesIO
from orcacnnapp.predict import predict
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


predict_blueprint = Blueprint('predict_from_model', __name__)
WIDTH = 640
HEIGHT = 640

@predict_blueprint.route('/predict', methods=['GET', 'POST'])
def predict_from_model():
    predict.predict(model_path='models/julyNew_adam-84-0.08.h5',
                 test_path='PreProcessed_image/PreProcessed_audio/uploads/')
    images = []
    for root, dirs, files in os.walk(current_app.config['PREDICT_FOLDER']):
        for filename in [os.path.join(root, name) for name in files]:
            if not filename.endswith('.png'):
                continue
            im = Image.open(filename)
            w, h = im.size
            aspect = 1.0 * w / h
            if aspect > 1.0 * WIDTH / HEIGHT:
                width = min(w, WIDTH)
                height = width / aspect
            else:
                height = min(h, HEIGHT)
                width = height * aspect
            images.append({
                'width': int(width),
                'height': int(height),
                'src': filename
            })
    return render_template('predict.html', **{
        'images': images
    })

@predict_blueprint.route('/<path:filename>')
def image(filename):
    try:
        im = Image.open(filename)
        io = BytesIO()
        im.save(io, format='PNG')
        return Response(io.getvalue(), mimetype='image/jpeg')

    except IOError:
        return render_template('errors/404.html'), 404

    return send_from_directory(current_app.config['IMAGE_FOLDER'], filename)
