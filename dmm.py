from twitter import app
from flask import Flask

@app.route('/do')
def do():
    return "1"


app.run(host="0.0.0.0", port=5000, debug=True)
