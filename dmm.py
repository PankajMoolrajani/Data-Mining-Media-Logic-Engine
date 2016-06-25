import pip
from flask import Flask, render_template,redirect,url_for,request,session,flash
from functools import wraps


app = Flask(__name__)
app.secret_key="log in"


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
 
     
         
@app.route('/')
def hello_world():
      return render_template("login.html")


if __name__ == '__main__':
      app.run(host="0.0.0.0", port=5050)




 
