from twitter import app
from flask_cors import CORS, cross_origin
from flask import Flask

app = Flask(__name__)
CORS(app)

@app.route('/')
def slash():
    return "DMM Logic Engine"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
