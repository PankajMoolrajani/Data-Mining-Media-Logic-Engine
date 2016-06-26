from db import DB
from schema import ProfilesApi
from flask import Flask, request

from authentication import Authentication
import urlparse

app = Flask(__name__)

from twitter import app

class User:
    @app.route("/profiles/api/create", methods=['POST'])
    def createProfileApi():
        try:
            req_json = request.get_json()
        except Exception, e:
            print e

        ob = ProfilesApi()
        ob.twitter_handle = req_json['twitter_handle']
        ob.key_consumer = req_json['key_consumer']
        ob.secret_consumer = req_json['secret_consumer']
        ob.key_access = req_json['key_access']
        ob.secret_access = req_json['secret_access']
        row = ob
        ob_db = DB()
        ob_db.add_row(row)

        return "added"

    @app.route("/profiles/users/get/retweeters", methods=['GET'])
    def getRetweetersId():
        tweet_id= request.args.get('tweet_id')
        profile_api = request.args.get('profile_api')
        thandle = Authentication().twitter(profile_api)
        return "in dev"
