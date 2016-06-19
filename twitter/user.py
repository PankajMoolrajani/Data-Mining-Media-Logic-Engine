from db import DB
from schema import ProfilesApi
from flask import Flask, request
import urlparse

app = Flask(__name__)

from twitter import app

class User:

    @app.route("/profiles/api/create", methods=['POST'])
    def createProfileApi():
        print "create profile"
        try:
            dict_data = request.get_json()
            print  dict_data
        except Exception, e:
            print e
        ob = ProfilesApi()
        ob.twitter_handle = dict_data['twitter_handle']
        ob.key_consumer = dict_data['key_consumer']
        ob.secret_consumer = dict_data['secret_consumer']
        ob.key_access = dict_data['key_access']
        ob.secret_access = dict_data['secret_access']
        row = ob
        ob_db = DB()
        ob_db.add_row(row)

        return "added"

    @app.route("/profiles/users/get/retweeters", methods=['GET'])
    def getRetweetersId():
        print "retweeters"
        tweet_id= request.args.get('tweet_id')
        profile_api = request.args.get('profile_api')
        ob = User()
        thandle = ob.authentication(profile_api)
        print thandle
        print profile_api
        print tweet_id


    def authentication(self, profile_api):
        ob = ProfilesApi()
        session = DB().session()
        row = session.query(ProfilesApi).filter_by(twitter_handle=profile_api).first()
        print row.twitter_handle
        return "ok"
