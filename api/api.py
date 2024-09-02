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
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return jsonify({'time': current_time})
    except Exception as e:
        return str(e), 500  # Add error handling response

if __name__ == '__main__':
    app.run(debug=True)