import pip
import os
from flask import Flask, render_template,redirect,url_for,request,session,flash
from functools import wraps
from datetime import timedelta


app = Flask(__name__)
app.secret_key="key1234"
app.config['UPLOAD_FOLDER']='C:/opt/IBM/WebSphere/Profiles/data/pdf_report/'

@app.before_request
def before_request():
     session.permanent = True
     app.permanent_session_lifetime =timedelta(minutes=20)
 



def login_required(f):
    error=None
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return f(*args,**kwargs)
        else:
            error='Please login first'
            return render_template("login.html", error=error)
    return wrap




@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    session.pop('logged_in',None)
    error="You are logged out"
    return render_template("login.html", error=error)
     
         
@app.route('/login', methods=['POST', 'GET'])
def login():
    error=None
    if request.method=='POST':
       if request.form['email']!='admin@gmail.com' or request.form['password']!='123':
           error="Invalid Credentials. Please try again"
       else:
           session['logged_in']=True
           return render_template("dashboard.html")
    return render_template("login.html", error=error)


@app.route('/do')
@login_required
def do():
    return render_template("dashboard.html")
 
 
@app.route('/filesave', methods=['POST', 'GET'])
@login_required
def filesave():
    file=request.files['file']
    print "success"
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        print file_path
        file.save(file_path)
        return "1"
    except Exception as ex:
      print (ex)		  
      return "2"
         
@app.route('/')
def hello_world():
      return render_template("login.html")


if __name__ == '__main__':
      app.run(host="0.0.0.0", port=5050)




 
