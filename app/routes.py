from . import app
from flask import jsonify

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Flask API!'})

@app.route('/hello')
def hello():
    return jsonify({'message': 'Hello, World!'})
