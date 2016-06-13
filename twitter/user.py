from db import DB
from schema import ProfilesApi

class User:

    def insertProfileApi(self, dict_data):
        ob = ProfilesApi()
        ob.twitter_handle = dict_data['twitter_handle']
        ob.key_consumer = dict_data['key_consumer']
        ob.secret_consumer = dict_data['secret_consumer']
        ob.key_access = dict_data['key_access']
        ob.secret_access = dict_data['secret_access']
        row = ob
        ob_db = DB()
        ob_db.add_row(row)
    """
    def getProfileApi(self):

        table = "profiles_api"
        column = "id_twitter, key_consumer, secret_consumer, key_access, secret_access"
        order = "timestamp"
        condition = "ORDER BY "+order+" LIMIT 0,1"

        ob = DB()
        id_row, list_rows = ob.querySelect(table, column, condition)

        dict_auth = {}
        try:
            dict_auth['id_twitter'] = list_rows[0][0]
            dict_auth['key_consumer'] = list_rows[0][1]
            dict_auth['secret_consumer'] = list_rows[0][2]
            dict_auth['key_access'] = list_rows[0][3]
            dict_auth['secret_access'] = list_rows[0][4]
        except:
            print "Error: authentication tokens missing in database"

        return dict_auth

    def getTokensApi(self, id_twitter):

        table = "profiles_api"
        column = "id_twitter, key_consumer, secret_consumer, key_access, secret_access"
        condition = "WHERE id_twitter='"+id_twitter+"'"

        ob = DB()
        id_row, list_rows = ob.querySelect(table, column, condition)
        dict_auth = {}
        try:
            dict_auth['id_twitter'] = list_rows[0][0]
            dict_auth['key_consumer'] = list_rows[0][1]
            dict_auth['secret_consumer'] = list_rows[0][2]
            dict_auth['key_access'] = list_rows[0][3]
            dict_auth['secret_access'] = list_rows[0][4]
        except:
            print "Error: authentication tokens missing in database"

        return dict_auth
    """
if __name__ == "__main__":
    dict_data = {}
    dict_data['key_consumer'] = "5vc4GEXUzY7jFAYefgzwQVqGU"
    dict_data['secret_consumer'] = "x0WhWwqcMYGKVfVe6lBO3LE2FjMlkSRszXYWgzl55c1nTOj3jY"
    dict_data['key_access'] = "4844933649-4NIkjCdA3OJdPbZOnLSa333UsMDZz35cuCcQXE5"
    dict_data['secret_access'] =  "f4fHPEXo8b34Kf4HhVPGTr7poy5c8f3sK2HoHsBU6Kwbp"

    ob = User()
    ob.insertProfileApi(dict_data)

    """
    #ob.getProfileApi()
    print ob.getTokensApi("drew_groove")
    """