import json
from Userdata import User
from tokenizer import Tokenizer


class Data:

    def __init__(self, filename: str):
        self.filename = filename
        self.userbase = []  # initializes a class variable containing a list of User objects

    def read(self):
        with open(self.filename) as fp:
            data = json.load(fp)  # convert string to dictionary
            for i in data:
                self.userbase.append(
                    User(
                        i['username'],
                        i['password'],
                        i['email'])
                )

    def write(self):
        with open(self.filename, 'w') as out_fp:
            json.dump([{
                'username': user.name,
                'password': user.password,
                'email': user.email}
                for user in self.userbase], out_fp)
            out_fp.close()


class

# class JsonEncoderWithIterablesDefault(json.JSONEncoder):
