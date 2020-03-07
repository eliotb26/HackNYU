from flask import Flask, render_template, jsonify
import test
from main import detect_document_with_newLine
app = Flask(__name__)


# @app.route('/', methods=['POST', 'GET'])
@app.route("/")
def hello():
    return render_template('TestWebsite.html')

@app.route("/test_one")
def test():
    return(detect_document_with_newLine())