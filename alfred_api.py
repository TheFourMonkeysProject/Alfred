__author__ = 'matt.livingston'
from flask import Flask
from flask import render_template
from system_services.diagnostics import AlfredDiagnostics
from speech.alfred_speech import AlfredSpeech
from utils.date_time_utils import SpeechHelpers
import json
from flask import render_template
from flask import request
from flask import jsonify
import datetime
import os
import random

from PIL import Image
from io import BytesIO
from flask import redirect
from flask import url_for
from flask import session


app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/alfred')
def home():
     return render_template('home.html')


@app.route('/speak', methods=['POST'])
def speak():
    alfred = AlfredSpeech()
    data = request.get_json()
    message = data["message"]

    if message == "alfred":
        greeting = SpeechHelpers()

        alfred.respond(greeting.determine_greeting(datetime.datetime.now()) + ", sir")
    else:
        alfred.respond("I am Alfred.")

    return jsonify(data)


@app.route('/getimage', methods=['POST'])
def get_image():
    try:
        if request.method =='POST':
            file = request.files['file']
            user = request.headers.get('user')

        if file:
            # filename = secure_filename(file.filename)
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
            file.save(os.path.join("C:\AlfredImages", "1-user" + "_" + str(random.random()) + ".jpg"))

    except Exception as e:
        print(str(e))

    return jsonify({"i": "test"})


@app.route('/cpu_count')
def get_cpu_count():

    count = 0
    try:
        count = AlfredDiagnostics.get_cpu_count()
    except Exception as e:
        print(e)

    return json.dumps("count:" + str(count))


@app.route('/disk_usage')
def get_disk_usage():

    count = 0
    try:
        count = AlfredDiagnostics.get_disk_usage()
    except Exception as e:
        print(e)

    return json.dumps("count:" + str(count))


if __name__ == '__main__':
    app.debug = True
    app.run('127.0.0.1')

