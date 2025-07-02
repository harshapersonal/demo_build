from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Flask API!'})

@app.route('/hello')
def hello():
    return jsonify({'message': 'Hello, World!'})

from app import app

if __name__ == '__main__':
    app.run(debug=True)
