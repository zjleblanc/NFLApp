import os
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask Dockerized'

@app.route('/example', methods=['POST'])
def examplePost():
    data = request.get_json()
    print data
    return jsonify(data)

@app.route('/init', methods=['POST'])
def init():
    os.system('python initTestDb.py')
    return 'NFLDB Initialized'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')