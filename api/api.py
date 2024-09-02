import time
from flask import Flask, jsonify  # Add jsonify import
from datetime import datetime  # Add datetime import

app = Flask(__name__, static_folder='../build', static_url_path='/')


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/time')
def get_current_time():
    try:
        current_time = datetime.now(datetime.timezone.utc).isoformat() + 'Z'  # ISO 8601 format with UTC timezone
        return jsonify({'time': current_time})
    except Exception as e:
        return str(e), 500  # Add error handling response
