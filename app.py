from flask import Flask, render_template, jsonify
import test

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        <insert python script here>

    return render_template('index.html')
