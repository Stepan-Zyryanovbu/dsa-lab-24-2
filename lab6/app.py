from flask import Flask, jsonify
import os

app = Flask(__name__)
port = int(os.environ.get('FLASK_RUN_PORT', 5001))

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "port": port})

@app.route('/process')
def process():
    return jsonify({"message": "Processed", "port": port})