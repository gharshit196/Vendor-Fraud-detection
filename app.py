from flask import Flask, render_template, redirect, url_for, request, session, flash, send_from_directory
from functools import wraps
import os
import pandas as pd
from werkzeug.utils import secure_filename
import easygui
import subprocess

UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = {'csv'}

dirname = os.path.dirname(__file__)
app = Flask(__name__)
app.secret_key = "secret key" #use random key generator
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
def index():

    return render_template('homepage.html')

# @app.route('/background_process_test')
# def background_process_test():
#     file_selector()
#     return ('nothing')

# def file_selector():

#     file_path = easygui.fileopenbox()
#     neo_4j_demo.backend(file_path)
#     return 0

# @app.route('/welcome')
# def welcome():
#     return render_template("welcome.html")

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error=None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid credentials. Please try again.'
#         else:
#             session['logged_in'] = True
#             flash('You were just logged in')
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)

@app.route('/uploads/<filename>')  
def uploaded_file(filename):  
   return send_from_directory(dirname,  
                              filename)

@app.route('/upload') 
#@login_required
def upload():
    return render_template('upload.html')
    #data = pd.read_csv('iris.csv') # there should be an upload option / button for this dataset in the flask webservice
    #return data.shape

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader', methods=['GET', 'POST'])  
def upload_file():  
    if 'file' not in request.files:  
        flash('No file part')
        return redirect(request.url)  
    file = request.files['file']  
    if file.filename == '': 
        flash('No selected file') 
        return redirect(request.url)  
    if file:  
        filename = secure_filename(file.filename)
        path = file.save(os.path.join(dirname, filename))
        return redirect('/visualizer') 
        # data = pd.read_csv(file)
        # return data.shape
        #return file.filename
        #return redirect('/uploads/'+file.filename)  
    return ''

@app.route('/visualizer')
def visualizer():
    return render_template('visualizer.html')

if __name__=="__main__":
    app.run(debug=True)