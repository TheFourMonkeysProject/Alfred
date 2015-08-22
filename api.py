__author__ = 'matt.livingston'
from flask import Flask
from system_services.diagnostics import AlfredDiagnostics
import json



app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/alfred')
def home():
    return json.dumps("Hello: Sir")


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
    app.run('0.0.0.0', port=80)

