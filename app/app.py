from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
from werkzeug import secure_filename
import os
from model.predict import *
import collections
import json



app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/files/"



@app.route("/")
def index():
    filenames = os.listdir('static/files')
    return render_template('index.html', files=filenames)

@app.route('/uploader', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['file']
      f.save(app.config["UPLOAD_FOLDER"] + secure_filename(f.filename))

      return redirect("/")

@app.route('/calc', methods = ['POST'])
def calc():
    if request.method == 'POST':
        f = request.form.get('dataset')
        results = get_results(f)
        count = collections.Counter(results)
        count1=count.items()
        #return json.dumps(list(results))

 

        return render_template('predict.html', results=count1)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
