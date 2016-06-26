import requests
import urlparse

def main(filename, app_url, profile_api):
    endpoint = urlparse.urljoin(app_url, '/follow')
    file_data = open(filename).readlines()

    json_req = {}
    json_req['profile_api'] = profile_api

    for line in file_data:
        profile_user = line
        json_req['profile_user'] = profile_user.strip()
        print json_req
        response = requests.post(endpoint, json=json_req)
        print response.raw
        print response.text
        print response.status_code

if __name__ == "__main__":
    filename = 'profile_users.csv'
    app_url = "http://localhost:5000"
    profile_api = 'drew_groove'
    main(filename, app_url, profile_api)