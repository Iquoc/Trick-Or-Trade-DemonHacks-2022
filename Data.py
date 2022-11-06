from abc import ABC
import json
from tokenizer import Tokenizer


class Data(ABC):
    @abc.abstractmethod
    def get_data(self):
        pass

    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def write(self, input_data):
        pass


class UserData(Data):

    def __init__(self, filename: str):
        self.filename = filename
        self.userbase = dict()  # initializes a class variable containing a list of User objects

    def get_data(self) -> dict:
        return self.userbase

    def read(self):
        with open(self.filename) as fp:
            self.userbase = json.load(fp)
            # for i in data:

            # self.userbase = json.load(fp)
            # data = json.load(fp)  # convert string to dictionary
            # self.userbase.update(data)  # adds the dictionary of person1(name: , password: , etc: etc.)

    def write(self, input_data):
        with open(self.filename, 'a') as out_fp:
            # json.dump(input_data, out_fp)
            user = input_data
            json.dump([{
                'username': user.name,
                'password': user.password,
                'email': user.email}
                for data in user], out_fp)
            out_fp.close()


class ListingData(Data):

    def __init__(self, filename: str):
        self.filename = filename
        self.listings = dict()  # initializes a class variable containing a list of User objects

    def get_data(self):
        return self.listings

    def read(self):
        with open(self.filename) as fp:
            self.userbase = json.load(fp)

    def write(self, input_data):
        with open(self.filename, 'a') as out_fp:
            data = json.load(out_fp)
            if input_data.user in data:
                temp = data[input_data.user]
                temp.update(input_data)
                json.dump(temp, out_fp)  # updates the already existing dictionary to include input_data
            else:
                json.dump(input_data, out_fp)  # creates new dictionary
            out_fp.close()


def create_user_data_process(filename: str) -> UserData:
    return UserData(filename)


def create_listing_data_process(filename: str) -> ListingData:
    return ListingData(filename)

# class JsonEncoderWithIterablesDefault(json.JSONEncoder):
