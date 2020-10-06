# helloTest.py
# at the end point / call method hello which returns "hello world"

from flask import Flask, request, render_template, url_for, redirect
#used to interface with filesystem
import os 

import pandas as pd

app = Flask(__name__)

#renders basic upload form
@app.route("/")
def hello():
  return render_template('uploadForm.html')

#this URL recieves input from the user and does something with it.
@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'inputFile' in request.files:
        inputFile = request.files['inputFile']
        if inputFile.filename != '':            
            inputFile.save(os.path.join('./dataUpload', inputFile.filename))
    return redirect(url_for('hello'))


if __name__ == '__main__':
  app.run(host='0.0.0.0')