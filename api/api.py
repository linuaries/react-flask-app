import time
from datetime import datetime
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='../build', static_url_path='/')
CORS(app)  # Enable CORS for all routes

@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/time')
def get_current_time():
    try:
        current_time = datetime.utcnow().isoformat() + 'Z'  # ISO 8601 format with UTC timezone
        return jsonify({'time': current_time})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
