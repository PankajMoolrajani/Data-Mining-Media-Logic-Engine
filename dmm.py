import app_config

from flask_cors import CORS
from flask import Flask
from authentication import api_authentication
from follow import api_twitter_follow


app = Flask(__name__)
app.register_blueprint(api_authentication, url_prefix='/auth')
app.register_blueprint(api_twitter_follow)
CORS(app)


@app.route('/')
def slash():
    return "DMM Logic Engine !"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
