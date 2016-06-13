
from twitter.user import User

if __name__ == "__main__":
    dict_data = {}
    dict_data['twitter_handle'] = "drew"
    dict_data['key_consumer'] = "5vc4GEXUzY7jFAYefgzwQVqGU"
    dict_data['secret_consumer'] = "x0WhWwqcMYGKVfVe6lBO3LE2FjMlkSRszXYWgzl55c1nTOj3jY"
    dict_data['key_access'] = "4844933649-4NIkjCdA3OJdPbZOnLSa333UsMDZz35cuCcQXE5"
    dict_data['secret_access'] =  "f4fHPEXo8b34Kf4HhVPGTr7poy5c8f3sK2HoHsBU6Kwbp"

    ob = User()
    ob.insert(dict_data)