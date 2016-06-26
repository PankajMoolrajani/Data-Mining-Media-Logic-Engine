import oauth2 as oauth
import json
from schema import ProfilesApi
from db import DB

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

if __name__ == "__main__":
    ob = Authentication()
    ob.twitter()
