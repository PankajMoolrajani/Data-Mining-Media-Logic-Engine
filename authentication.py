import oauth2 as oauth
import random
import hashlib
import string

from flask import Blueprint , request
from flask_cors import CORS

from schema import ProfilesApi
from db import DB

api_authentication = Blueprint('api_authentication', __name__)
CORS(api_authentication)


class Authentication:
    def __init__(self):
        pass

    def twitter(self, profile_api):

        session = DB().session()
        row = session.query(ProfilesApi).filter_by(twitter_handle=profile_api).first()
        key_consumer = row.key_consumer
        secret_consumer = row.secret_consumer
        key_access = row.key_access
        secret_access = row.secret_access

        consumer = oauth.Consumer(key=key_consumer, secret=secret_consumer)
        access_token = oauth.Token(key=key_access, secret=secret_access)
        client = oauth.Client(consumer, access_token)

        return client


@api_authentication.route('/token/get', methods=['POST'])
def getAuthToken():
        if request.form['email'] != 'admin@gmail.com' or request.form['password'] != '123':
            return "INVALID CREDENTIALS. PLEASE TRY AGAIN"
        else:
            token = hashlib.sha256()
            token.update(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6)))
            token.digest()
            return token.digest()


if __name__ == "__main__":
    ob = Authentication()
    ob.twitter()
