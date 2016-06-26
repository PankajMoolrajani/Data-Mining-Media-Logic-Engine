from flask import Flask, request
from user import User
from authentication import Authentication
from db import DB
app = Flask(__name__)

from twitter import app


class Follow:

    @app.route("/follow", methods=['POST'])
    def followUser():
        try:
            req_json = request.get_json()
        except Exception, e:
            print e

        profile_api = req_json['profile_api']
        profile_user = req_json['profile_user']

        endpoint = "https://api.twitter.com/1.1/friendships/create.json?screen_name="+profile_user+"&follow=true"
        api_handler = Authentication().twitter(profile_api)
        res, data = api_handler.request(endpoint, "POST")
        return data




