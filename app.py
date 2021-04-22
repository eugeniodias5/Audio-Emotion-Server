import os

from flask import Flask, request
from werkzeug.utils import secure_filename

from live_predictions import LivePredictions

live_predictions = LivePredictions()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    filename = './' + secure_filename(file.filename)
    file.save(filename)
    sentiment = live_predictions.make_predictions(filename)
    os.remove(filename)

    return sentiment
