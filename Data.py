import json
from tokenizer import Tokenizer


class Data:

    def __init__(self, filename: str):
        self.filename = filename
        self.userbase = dict()  # initializes a class variable containing a list of User objects

    def get_userbase(self) -> dict:
        return self.userbase

    def read(self):
        with open(self.filename) as fp:
            self.userbase = json.load(fp)
            # for i in data:

            # self.userbase = json.load(fp)
            # data = json.load(fp)  # convert string to dictionary
            # self.userbase.update(data)  # adds the dictionary of person1(name: , password: , etc: etc.)

    def write(self, data):
        with open(self.filename, 'a') as out_fp:
            json.dump(data, out_fp)
            # json.dump([{
            #     'username': user.name,
            #     'password': user.password,
            #     'email': user.email}
            #     for user in self.userbase], out_fp)
            out_fp.close()


def create_data_process(filename: str) -> Data:
    return Data(filename)

# class JsonEncoderWithIterablesDefault(json.JSONEncoder):
