import os
import app_config
from twitter import app
from flask_cors import CORS, cross_origin
from flask import Flask, render_template,redirect,url_for,request,session,flash
from functools import wraps
from datetime import timedelta

app = Flask(__name__)
CORS(app)
app.secret_key = "key1234"
app.config['UPLOAD_FOLDER'] = app_config.filepath


@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=20)


@app.route('/')
def slash():
    return "DMM Logic Engine"


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return "SESSIONOUT"

    return wrap


@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    session.pop('logged_in', None)
    return "LOGOUT"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['email'] != 'admin@gmail.com' or request.form['password'] != '123':
            return "INVALID CREDENTIALS. PLEASE TRY AGAIN"
        else:
            session['logged_in'] = True
            return "PASS"
    else:
        return "GET_REQUEST"





@app.route('/filesave', methods=['POST', 'GET'])
def filesave():
    file = request.files['file']
    print "success"
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        print file_path
        file.save(file_path)
        return "FILE_SAVED"
    except Exception as ex:
        print (ex)
        return "FILE_NOT_SAVED"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
