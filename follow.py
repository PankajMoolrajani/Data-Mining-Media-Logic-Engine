import os
import app_config
import csv

from flask import Blueprint , request
from flask_cors import CORS

from authentication import Authentication


api_twitter_follow= Blueprint('api_twitter_follow', __name__)
CORS(api_twitter_follow)



class Follow:


    @api_twitter_follow.route("/follow", methods=['POST'])
    def followUser(self):
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


    @api_twitter_follow.route("/health", methods=['GET'])
    def health(self):
        return 'health_status: OK'


@api_twitter_follow.route('/follow/bulk/csv', methods=['POST'])
def followBulkCsv():
    file = request.files['file']
    job_name=request.form['job_name']
    print job_name
    print "success"
    try:
        file_path = os.path.join(app_config.filepath, file.filename)
        print file_path
        file.save(file_path)
        with open(file_path, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

        return "FILE_SAVED"
    except Exception as ex:
        print (ex)
        return "FILE_NOT_SAVED"
